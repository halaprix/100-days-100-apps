#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / 'projects' / 'driveping'

required = [
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
    'fixtures/sample-drive-session.json',
]
for rel in required:
    path = PROJECT / rel
    assert path.is_file(), f'missing {rel}'

readme = (PROJECT / 'README.md').read_text(encoding='utf-8')
spec = (PROJECT / 'SPEC.md').read_text(encoding='utf-8')
assert 'background location' in readme.lower()
assert 'packet-capture' in spec.lower()
assert 'DrivePing' in readme

fixture = json.loads((PROJECT / 'fixtures/sample-drive-session.json').read_text(encoding='utf-8'))
assert fixture['session_id'] == 'sample-drive-session'
assert len(fixture['probes']) >= 3
assert {p['target'] for p in fixture['probes']} >= {'gateway', 'dns', 'https-endpoint'}

for rel in ['README.md', 'SPEC.md', 'AGENTS.md', 'SECURITY.md', 'CONTRIBUTING.md']:
    text = (PROJECT / rel).read_text(encoding='utf-8')
    forbidden = ['GITHUB_TOKEN=', 'ghp_', 'sk_live_', 'private key']
    for marker in forbidden:
        assert marker not in text, f'forbidden marker {marker} in {rel}'

print('DrivePing scaffold verification passed')
