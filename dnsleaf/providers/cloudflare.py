import requests
from dnsleaf.providers.base import DNSProvider
from dnsleaf.core.models import DNSRecord, FlushResult

class CloudflareDNS(DNSProvider):
    """Cloudflare DNS cache flush implementation using 1.1.1.1 purge tool"""
    
    def __init__(self):
        super().__init__()
        self.purge_url = "https://one.one.one.one/api/v1/purge"
        
    def validate_record(self, record: DNSRecord) -> bool:
        return bool(record.domain and "." in record.domain)
    
    async def flush_cache(self, record: DNSRecord) -> FlushResult:
        if not self.validate_record(record):
            return FlushResult(
                success=False,
                message="Invalid domain format",
                provider="cloudflare"
            )
            
        try:
            params = {
                "domain": record.domain,
                "type": record.record_type
            }
            
            response = requests.post(
                self.purge_url,
                params=params
            )
            response.raise_for_status()
            
            return FlushResult(
                success=True,
                message=f"Successfully purged cache for {record.domain}",
                provider="cloudflare",
                details=response.json()
            )
            
        except requests.RequestException as e:
            self.logger.error(f"Cloudflare cache flush failed: {str(e)}")
            return FlushResult(
                success=False,
                message=str(e),
                provider="cloudflare"
            )
