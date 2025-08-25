from .base import *
import os
import urllib.parse as urlparse

SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE_ME")

# Fly מזריק את שם הדומיין כ-secret/ENV אם נגדיר; נשתמש בו ל-ALLOWED_HOSTS/CSRF
FLY_HOSTNAME = os.environ.get("FLY_HOSTNAME", "")
ALLOWED_HOSTS = [FLY_HOSTNAME] if FLY_HOSTNAME else ["*"]  # אפשר להקשיח בהמשך
if FLY_HOSTNAME:
    CSRF_TRUSTED_ORIGINS = [f"https://{FLY_HOSTNAME}"]

# ברירת מחדל: SQLite (למקרה שאין DB)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/data/db.sqlite3",
    }
}

# אם יש DATABASE_URL → נעבור ל-Postgres
db_url = os.environ.get("DATABASE_URL")
if db_url:
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(db_url)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": url.path[1:],
            "USER": url.username,
            "PASSWORD": url.password,
            "HOST": url.hostname,
            "PORT": url.port or "5432",
        }
    }

# קבצי מדיה (תמונות וכו')
MEDIA_ROOT = "/data/media"
