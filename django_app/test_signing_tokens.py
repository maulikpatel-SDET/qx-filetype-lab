import json
import base64
from cryptography.hazmat.primitives import hashes, hmac

SECRET_KEY = b"test-only-secret"


def sign_token(data, salt=b""):
    payload = json.dumps(data, separators=(",", ":")).encode()
    encoded = base64.urlsafe_b64encode(payload).rstrip(b"=")

    signer = hmac.HMAC(SECRET_KEY, hashes.SHA256())
    signer.update(salt + encoded)
    signature = base64.urlsafe_b64encode(
        signer.finalize()
    ).rstrip(b"=")

    return encoded.decode() + "." + signature.decode()


def make_django_token(data):
    return sign_token(data, salt=b"qx:")


def make_itsdangerous_token(data):
    return sign_token(data)


print(make_django_token({"user_id": 123}))
print(make_itsdangerous_token({"user_id": 123}))
