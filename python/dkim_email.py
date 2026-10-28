"""R11-07 DKIM email signing with RSA-SHA1 (weak) via dkimpy."""
import dkim

def sign_email(message: bytes, private_key: bytes) -> bytes:
    return dkim.sign(message, b"sel", b"qx.example.com", private_key,
                     signature_algorithm=b"rsa-sha1")               # RSA-SHA1 DKIM
