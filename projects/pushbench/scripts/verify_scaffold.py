#!/usr/bin/env python3
"""Ad-hoc scaffold verifier for the PushBench snapshot."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'SPEC.md',
    'AGENTS.md',
    'CHANGELOG.md',
    'LICENSE',
    'CONTRIBUTING.md',
    'SECURITY.md',
    '.github/workflows/ci.yml',
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.beads/issues.jsonl',
    'fixtures/load-profile.yml',
    'fixtures/server-matrix.json',
    'tests/golden/sample-report.md',
]
REQUIRED_EXIST_ONLY = ['scripts/verify_scaffold.py', '.snapshot.json', '.gitignore']
FORBIDDEN = ['BEGIN PRIVATE KEY', 'AWS_SECRET_ACCESS_KEY=', 'DATABASE_URL=', 'ghp_', 'sk_live_']


def main() -> int:
    missing = [path for path in REQUIRED + REQUIRED_EXIST_ONLY if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f'missing required files: {missing}')

    profile = (ROOT / 'fixtures/load-profile.yml').read_text()
    assert 'local_only: true' in profile
    assert 'localhost:8081' in profile
    assert 'public' not in profile.lower()

    matrix = json.loads((ROOT / 'fixtures/server-matrix.json').read_text())
    assert {b['id'] for b in matrix['backends']} == {'ntfy-http', 'ntfy-websocket', 'autopush-fixture'}

    snapshot = json.loads((ROOT / '.snapshot.json').read_text())
    assert snapshot['slug'] == 'pushbench'
    assert snapshot['canonical_path'] == 'projects/pushbench'
    assert snapshot['source_remote'] is None

    for rel in REQUIRED + ['.snapshot.json']:
        text = (ROOT / rel).read_text(errors='ignore')
        for marker in FORBIDDEN:
            if marker in text:
                raise SystemExit(f'forbidden marker {marker!r} in {rel}')

    readme = (ROOT / 'README.md').read_text()
    assert 'UnifiedPush' in readme
    assert 'ntfy' in readme
    assert 'Autopush' in readme
    assert 'No load tests against public' in readme

    print('PushBench scaffold verification passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
