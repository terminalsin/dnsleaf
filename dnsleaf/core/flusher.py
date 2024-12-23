import logging
from typing import Dict
from dnsleaf.core.models import DNSRecord, FlushResult
from dnsleaf.providers.base import DNSProvider
from dnsleaf.providers.cloudflare import CloudflareDNS
from dnsleaf.providers.google import GoogleDNS

class DNSCacheFlusher:
    """Main class for managing DNS cache flushes across multiple providers"""
    
    def __init__(self):
        self.providers: Dict[str, DNSProvider] = {
            "cloudflare": CloudflareDNS(),
            "google": GoogleDNS()
        }
        self.logger = logging.getLogger(__name__)
        
    async def flush_all(self, record: DNSRecord) -> Dict[str, FlushResult]:
        results = {}
        
        for name, provider in self.providers.items():
            try:
                results[name] = await provider.flush_cache(record)
            except Exception as e:
                self.logger.error(f"Error flushing {name} cache: {str(e)}")
                results[name] = FlushResult(
                    success=False,
                    message=f"Unexpected error: {str(e)}",
                    provider=name
                )
                
        return results
    
    async def flush_provider(self, record: DNSRecord, provider_name: str) -> FlushResult:
        provider = self.providers.get(provider_name)
        if not provider:
            return FlushResult(
                success=False,
                message=f"Unknown provider: {provider_name}",
                provider=provider_name
            )
            
        return await provider.flush_cache(record)

