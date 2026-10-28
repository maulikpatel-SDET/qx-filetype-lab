"""R11-01 Django settings: hardcoded SECRET_KEY, MD5 password hasher, weak session/SSL options."""
SECRET_KEY = "django-insecure-0123456789abcdef0123456789abcdef"      # hardcoded signing secret

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",                # BROKEN: MD5 for passwords
    "django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher",       # BROKEN: unsalted SHA-1
    "django.contrib.auth.hashers.Argon2PasswordHasher",             # good
]

SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
DEFAULT_HASHING_ALGORITHM = "sha1"                                  # signing uses SHA-1
