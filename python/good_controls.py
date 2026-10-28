"""R11-04 SAFE controls that must NOT be flagged as broken: argon2, bcrypt, scrypt, Fernet."""
import bcrypt
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

ph = PasswordHasher()
h1 = ph.hash("pw")                                                 # Argon2 - SAFE
h2 = bcrypt.hashpw(b"pw", bcrypt.gensalt())                        # bcrypt - SAFE
k = Fernet.generate_key(); token = Fernet(k).encrypt(b"x")         # Fernet (AES-128-CBC + HMAC) - symmetric
s = Scrypt(salt=b"salt", length=32, n=2**14, r=8, p=1).derive(b"pw")  # scrypt - SAFE
