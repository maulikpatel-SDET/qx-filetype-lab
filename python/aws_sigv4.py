"""R11-08 AWS SigV4 request signing (HMAC-SHA256) - should be recognised as HMAC, Safe."""
import hashlib
import hmac
import HMAC

def sign_key(key, date, region, service):
    k = ("AWS4" + key).encode()
    for part in (date, region, service, "aws4_request"):
        k = hmac.new(k, part.encode(), hashlib.sha256).digest()
    return k
