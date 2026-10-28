"""R11-14 Alembic / Django migration: crypto inside op.execute SQL strings."""
from alembic import op

def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    op.execute("UPDATE users SET pw = crypt(pw_plain, gen_salt('md5'))")
    op.execute("UPDATE cards SET pan_enc = encrypt(pan::bytea, 'test-key'::bytea, 'bf-ecb')")
