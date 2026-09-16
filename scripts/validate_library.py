"""Validate source library structure; requires PyYAML. No network or writes."""
from pathlib import Path
import argparse
import importlib.util
import json
import re
import sys
from urllib.parse import unquote

import yaml


def validate(root, official=None):
    root = root.resolve()
    errors, names, indexed = [], set(), set()
    manifest = json.loads((root / 'library.json').read_text(encoding='utf-8'))
    official_check = None
    if official:
        spec = importlib.util.spec_from_file_location('official_skill_check', official)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        official_check = module.validate_skill
    for item in manifest['skills']:
        name = item['name']
        path = (root / item['path']).resolve()
        if not path.is_relative_to(root) or path == root:
            errors.append(f'Path escapes library: {name}')
            continue
        if name in names:
            errors.append(f'Duplicate name: {name}')
        names.add(name)
        indexed.add(path / 'SKILL.md')
        try:
            content = (path / 'SKILL.md').read_text(encoding='utf-8')
            match = re.match(r'^---\n(.*?)\n---\n', content, re.S)
            if not match:
                raise ValueError('Missing YAML frontmatter')
            meta = yaml.safe_load(match[1])
            if meta['name'] != name or path.name != name:
                errors.append(f'Name/folder mismatch: {name}')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) >= 64:
                errors.append(f'Invalid name: {name}')
            if not isinstance(meta.get('description'), str) or not meta['description'].strip():
                errors.append(f'Missing description: {name}')
            if meta['metadata']['version'] != item['version'] or meta['metadata']['category'] != item['category']:
                errors.append(f'Metadata/index mismatch: {name}')
            ui = yaml.safe_load((path / 'agents/openai.yaml').read_text(encoding='utf-8'))
            if not 25 <= len(ui['interface']['short_description']) <= 64:
                errors.append(f'UI description length: {name}')
            if '$' + name not in ui['interface']['default_prompt']:
                errors.append(f'UI prompt omits invocation: {name}')
            if ui.get('policy', {}).get('allow_implicit_invocation') is not True:
                errors.append(f'Unexpected invocation policy: {name}')
            template = path / 'assets/deliverable-template.md'
            if not template.is_file() or template.stat().st_size == 0:
                errors.append(f'Missing/empty deliverable template: {name}')
            if official_check:
                valid, message = official_check(path)
                if not valid:
                    errors.append(f'Official check {name}: {message}')
        except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f'{name}: {exc}')
    actual = {p.resolve() for p in root.rglob('SKILL.md')}
    if indexed != actual:
        errors.append(f'Index differs from discovered skills: {len(indexed ^ actual)} files')
    checked_links = 0
    for document in root.rglob('*.md'):
        text = document.read_text(encoding='utf-8')
        if '[TODO:' in text:
            errors.append(f'Unfinished scaffold: {document.relative_to(root)}')
        for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = raw.strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            relative = unquote(target.split('#', 1)[0])
            resolved = (document.parent / relative).resolve()
            checked_links += 1
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'Broken/escaping link: {document.relative_to(root)} -> {target}')
        for peer in re.findall(r'`\$([a-z0-9-]+)`', text):
            if peer not in names:
                errors.append(f'Unknown skill reference: {peer}')
    return dict(status='passed' if not errors else 'failed', skills=len(names),
                relative_links=checked_links, official_validator=bool(official_check), errors=errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--official-validator', type=Path)
    args = parser.parse_args()
    try:
        result = validate(args.root, args.official_validator)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = dict(status='failed', errors=[str(exc)])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
