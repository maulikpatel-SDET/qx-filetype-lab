import hashlib
from itsdangerous import URLSafeTimedSerializer
from itsdangerous.signer import HMACAlgorithm

s = URLSafeTimedSerializer(
    "test-only-secret",
    signer_kwargs={
        "digest_method": hashlib.sha256,
        "algorithm": HMACAlgorithm,
    },
)

token = s.dumps({"user_id": 123})
print(token)
