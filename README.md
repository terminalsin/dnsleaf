![leafdns logo](/docs/logo.png)

A Python library and CLI tool for flushing DNS caches across multiple providers.

## Installation

```bash
pip install dnsleaf
```

## Supported Providers

| Provider | Documentation | Stability |
|----------|--------------|-----------|
| Cloudflare | [API Docs](https://one.one.one.one/api/) | Beta |
| Google | [Public DNS Docs](https://developers.google.com/speed/public-dns/docs/purge-cache) | Beta |

## Library Usage

```python
from dns_flush import DNSCacheFlusher, DNSRecord

async def main():
    # Initialize flusher
    flusher = DNSCacheFlusher()
    
    # Create record
    record = DNSRecord(domain="example.com", record_type="A")
    
    # Flush all providers
    results = await flusher.flush_all(record)
    
    # Or flush specific provider
    result = await flusher.flush_provider(record, "cloudflare")

```

## CLI Usage

```bash
# Flush all providers
dnsleaf flush example.com

# Flush specific provider
dnsleaf flush example.com --provider cloudflare

# Specify record type
dnsleaf flush example.com --record-type A

# Get JSON output
dnsleaf flush example.com --json-output
```