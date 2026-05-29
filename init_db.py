from database.db import Base
from database.db import engine

from models.user import User
from models.password_reset_token import PasswordResetToken

Base.metadata.create_all(bind=engine)

print("Database initialized")