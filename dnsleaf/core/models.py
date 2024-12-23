from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class DNSRecord:
    """Represents a DNS record to be flushed"""
    domain: str
    record_type: Optional[str] = None

@dataclass
class FlushResult:
    """Represents the result of a cache flush operation"""
    success: bool
    message: str
    provider: str
    details: Optional[Dict] = None
