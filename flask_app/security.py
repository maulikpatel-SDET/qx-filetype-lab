"""R11-03 Flask: hardcoded secret_key, passlib CryptContext with md5_crypt, bcrypt (good)."""
from flask import Flask
from passlib.context import CryptContext

app = Flask(__name__)
app.secret_key = "test-only-flask-secret-key"                      # session signing secret

pwd = CryptContext(schemes=["md5_crypt", "des_crypt", "bcrypt"], deprecated=["md5_crypt", "des_crypt"])

def hash_pw(pw: str) -> str:
    return pwd.hash(pw)
