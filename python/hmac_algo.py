import hashlib
import hmac as std_hmac
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import hmac as crypto_hmac

# # Shared test message
# message = b"Qryptive HMAC-SHA-256 test"

# print("--- Running Cryptographic Integrity Tests ---\n")

# # =====================================================================
# # TYPE 1: Python Standard Library (Recommended for normal data/APIs)
# # =====================================================================
# print("[Type 1] Python Standard Library (std_hmac)")

# # 1. Generate a strong random 32-byte key
# std_key = os.urandom(32)

# # 2. Sign the message (One-liner)
# std_tag = std_hmac.new(std_key, message, hashlib.sha256).digest()
# print(f"-> Generated Tag (Hex): {std_tag.hex()}")

# # 3. Verify the message safely (Prevents timing attacks)
# # Recompute what the tag should be
# expected_tag = std_hmac.new(std_key, message, hashlib.sha256).digest()
# is_valid = std_hmac.compare_digest(expected_tag, std_tag)

# if is_valid:
#     print("-> Status: Verification passed successfully!\n")


# =====================================================================
# TYPE 2: PyCa 'cryptography' Library (Recommended for streaming large files)
# =====================================================================
print("[Type 2] PyCa 'cryptography' Library")

# 1. Generate a strong random 32-byte key
crypto_key = os.urandom(32)

# 2. Sign the message (Streaming style via .update())
signer = crypto_hmac.HMAC(crypto_key, hashes.SHA256())
signer.update(message)
crypto_tag = signer.finalize()
print(f"-> Generated Tag (Hex): {crypto_tag.hex()}")

# 3. Verify the message safely (Raises InvalidSignature exception if it fails)
verifier = crypto_hmac.HMAC(crypto_key, hashes.SHA256())
verifier.update(message)

try:
    verifier.verify(crypto_tag)
    print("-> Status: Verification passed successfully!\n")
except Exception:
    print("-> Status: Verification failed! (Tampering detected)")
