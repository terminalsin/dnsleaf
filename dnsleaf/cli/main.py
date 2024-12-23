import click
import asyncio
from dnsleaf.core.models import DNSRecord
from dnsleaf.core.flusher import DNSCacheFlusher
import json

@click.group()
def cli():
    """DNS Cache Flush CLI - Flush DNS caches across multiple providers"""
    pass

@cli.command()
@click.argument('domain')
@click.option('--record-type', '-t', help='DNS record type (A, AAAA, MX, etc.)')
@click.option('--provider', '-p', help='Specific provider to flush (cloudflare, google)')
@click.option('--json-output', '-j', is_flag=True, help='Output results in JSON format')
def flush(domain: str, record_type: str, provider: str, json_output: bool):
    """Flush DNS cache for a domain"""
    record = DNSRecord(domain=domain, record_type=record_type)
    flusher = DNSCacheFlusher()
    
    async def run_flush():
        if provider:
            result = await flusher.flush_provider(record, provider)
            results = {provider: result}
        else:
            results = await flusher.flush_all(record)
        
        if json_output:
            output = {
                name: {
                    "success": r.success,
                    "message": r.message,
                    "details": r.details
                }
                for name, r in results.items()
            }
            click.echo(json.dumps(output, indent=2))
        else:
            for name, result in results.items():
                click.echo(f"\n{name.upper()}:")
                click.echo(f"Success: {result.success}")
                click.echo(f"Message: {result.message}")
                if result.details:
                    click.echo(f"Details: {result.details}")
    
    asyncio.run(run_flush())

def main():
    cli()

if __name__ == '__main__':
    main()
