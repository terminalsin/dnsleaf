import requests
from dnsleaf.providers.base import DNSProvider
from dnsleaf.core.models import DNSRecord, FlushResult

class GoogleDNS(DNSProvider):
    """Google Public DNS cache flush implementation"""
    
    def __init__(self):
        super().__init__()
        self.flush_url = "https://developers.google.com/speed/public-dns/cache"
        
    def validate_record(self, record: DNSRecord) -> bool:
        return bool(record.domain and "." in record.domain)
    
    async def flush_cache(self, record: DNSRecord) -> FlushResult:
        if not self.validate_record(record):
            return FlushResult(
                success=False,
                message="Invalid domain format",
                provider="google"
            )
            
        try:
            params = {"domain": record.domain}
            if record.record_type:
                params["type"] = record.record_type
                
            response = requests.get(self.flush_url, params=params)
            response.raise_for_status()
            
            return FlushResult(
                success=True,
                message=f"Successfully flushed cache for {record.domain}",
                provider="google",
                details={"status_code": response.status_code}
            )
            
        except requests.RequestException as e:
            self.logger.error(f"Google DNS cache flush failed: {str(e)}")
            return FlushResult(
                success=False,
                message=str(e),
                provider="google"
            )

