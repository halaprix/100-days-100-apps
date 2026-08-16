#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / 'projects' / 'patchproof'

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
    'fixtures/sample-patch-review.json',
]
for rel in required:
    path = PROJECT / rel
    assert path.is_file(), f'missing {rel}'

readme = (PROJECT / 'README.md').read_text(encoding='utf-8')
spec = (PROJECT / 'SPEC.md').read_text(encoding='utf-8')
agents = (PROJECT / 'AGENTS.md').read_text(encoding='utf-8')
assert 'PatchProof' in readme
assert 'No endpoint control' in readme
assert 'static evidence' in spec
assert 'must not connect to real endpoint' in agents

fixture = json.loads((PROJECT / 'fixtures/sample-patch-review.json').read_text(encoding='utf-8'))
assert fixture['report_id'] == 'sample-patch-review'
classes = {asset['classification'] for asset in fixture['assets']}
assert classes >= {'patched_pending_rescan', 'offline_stale', 'rollback_exception_needed'}
assert all(asset['asset_label'].startswith('asset-') for asset in fixture['assets'])

public_files = [
    'README.md',
    'SPEC.md',
    'AGENTS.md',
    'SECURITY.md',
    'CONTRIBUTING.md',
    'fixtures/sample-patch-review.json',
]
for rel in public_files:
    text = (PROJECT / rel).read_text(encoding='utf-8')
    forbidden_literals = ['GITHUB_TOKEN=', 'ghp_', 'sk_live_', 'private key']
    for marker in forbidden_literals:
        assert marker not in text, f'forbidden marker {marker} in {rel}'
    assert not re.search(r'\b(?:10|172\.(?:1[6-9]|2\d|3[0-1])|192\.168)\.', text), f'private ip in {rel}'
    assert not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text), f'email in {rel}'

print('PatchProof scaffold verification passed')
