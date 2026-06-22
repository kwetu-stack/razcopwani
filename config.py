import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "razco-pwani-local-development-secret")
    database_url = os.getenv("DATABASE_URL", "").strip()
    if database_url == "sqlite:///data/razco_pwani.db" or not database_url:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{(BASE_DIR / 'data' / 'razco_pwani.db').as_posix()}"
    else:
        SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
    REPORT_FOLDER = BASE_DIR / "reports"
