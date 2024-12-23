from abc import ABC, abstractmethod
import logging
from dnsleaf.core.models import DNSRecord, FlushResult

class DNSProvider(ABC):
    """Abstract base class for DNS providers"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    async def flush_cache(self, record: DNSRecord) -> FlushResult:
        """Flush DNS cache for the given record"""
        pass
    
    @abstractmethod
    def validate_record(self, record: DNSRecord) -> bool:
        """Validate if the record can be processed by this provider"""
        pass