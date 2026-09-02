# Contributing

## Scope

Keep contributions inside the local, deterministic preflight boundary. Do not
add console credentials, network calls, APK upload, signing-key access, or
claims that local artifact metadata proves registration.

## Workflow

1. Create and claim a Beads issue.
2. Add or update a synthetic fixture and a deterministic test with each rule.
3. Run the focused validation commands.
4. Use a Conventional Commit that references the issue.

## Safety

Never commit real APKs, package names, signing fingerprints, release manifests,
console exports, credentials, or customer data.
