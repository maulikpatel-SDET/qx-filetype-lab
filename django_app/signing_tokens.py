"""R11-02 Django signing.Signer / Dumper (HMAC-SHA1 by default) + itsdangerous."""
import hashlib
from django.core import signing
from itsdangerous import URLSafeTimedSerializer

def make_django_token(data):
    # The scanner will instantly flag 'hashlib.sha1' as a vulnerability
    signer = signing.TimestampSigner(salt="qx", algorithm=hashlib.sha1)
    serialized_data = signing.JSONSerializer().dumps(data)
    return signer.sign(serialized_data)

def make_itsdangerous_token(data):
    # The scanner will flag this explicit SHA-1 configuration
    s = URLSafeTimedSerializer(
        "test-only-secret", 
        signer_kwargs={"digest_method": hashlib.sha1}
    )
    return s.dumps(data)

