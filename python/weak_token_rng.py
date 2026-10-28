"""R11-06 Security tokens built from non-crypto random instead of secrets."""
import random
import string

def reset_token(n=32):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))   # predictable token

def api_key():
    return hex(random.getrandbits(128))                                       # predictable API key
