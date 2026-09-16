"""Copy registered skills to an explicit local target; never overwrite conflicts."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import sys


def hashes(directory):
    result = {}
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlink is not supported inside a skill: {path}')
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def install(root, target, dry_run=False):
    root, target = root.resolve(), target.resolve()
    if target == root or target.is_relative_to(root):
        raise ValueError('Install target must be outside the source library')
    manifest = json.loads((root / 'library.json').read_text(encoding='utf-8'))
    plans, names = [], set()
    # Preflight every destination before any mutation.
    for item in manifest['skills']:
        name = item['name']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in names:
            raise ValueError(f'Invalid or duplicate skill name: {name}')
        names.add(name)
        source = (root / item['path']).resolve()
        if not source.is_relative_to(root) or not (source / 'SKILL.md').is_file():
            raise ValueError(f'Invalid source skill: {name}')
        destination = target / name
        if destination.is_symlink() or destination.resolve() != destination:
            raise ValueError(f'Destination redirects elsewhere: {destination}')
        expected = hashes(source)
        if destination.exists():
            if not destination.is_dir() or hashes(destination) != expected:
                raise ValueError(f'Conflicting existing skill; nothing copied: {destination}')
            action = 'identical-skip'
        else:
            action = 'copy'
        plans.append((name, source, destination, expected, action))
    copied, skipped = [], []
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)
        for name, source, destination, expected, action in plans:
            if action == 'identical-skip':
                skipped.append(name)
                continue
            # copytree refuses a destination created concurrently by another process.
            shutil.copytree(source, destination)
            if hashes(destination) != expected:
                raise RuntimeError(f'Copy verification failed; inspect partial installation: {destination}')
            copied.append(name)
    return dict(mode='dry-run' if dry_run else 'installed', target=str(target),
                copied=copied, identical_skipped=skipped,
                plan=[dict(name=p[0], action=p[4]) for p in plans])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        result = install(args.root, args.target, args.dry_run)
    except (OSError, ValueError, KeyError, RuntimeError) as exc:
        print(json.dumps(dict(status='failed', error=str(exc)), ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
