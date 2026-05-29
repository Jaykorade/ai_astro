import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")

APP_URL = os.getenv("APP_URL")