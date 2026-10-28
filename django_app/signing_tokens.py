"""R11-02 Django signing.Signer / Dumper (HMAC-SHA1 by default) + itsdangerous."""
from django.core import signing
from itsdangerous import URLSafeTimedSerializer

def make_django_token(data):
    return signing.dumps(data, salt="qx")                          # HMAC-SHA1 under the hood

def make_itsdangerous_token(data):
    s = URLSafeTimedSerializer("test-only-secret")                 # default signer = HMAC-SHA1
    return s.dumps(data)
