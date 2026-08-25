# Security policy

## Reporting a vulnerability

Please report security issues privately through the repository's security
advisory channel. Do not include production URLs, cookies, authorization
headers, response bodies, or credentials in a public issue.

## Product safety boundary

VariantGuard is designed to make read-only HTTP requests. It must not store
credentials, apply Cloudflare configuration, or include full response bodies in
reports.
