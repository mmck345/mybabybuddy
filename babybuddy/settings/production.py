from .base import *
import os

# --- חובה לעדכן בסודות ב-Fly (ראה בהמשך) ---
SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE_ME")

# שם הדומיין של האפליקציה שלך ב-Fly:
ALLOWED_HOSTS = [os.environ.get("FLY_HOSTNAME", "localhost")]

# מומלץ בדג'אנגו חדש:
CSRF_TRUSTED_ORIGINS = [f"https://{os.environ.get('FLY_HOSTNAME', '')}"] if os.environ.get("FLY_HOSTNAME") else []

# --- SQLite על Volume בנתיב קבוע ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/data/db.sqlite3",
    }
}

# קבצי מדיה (תמונות וכו') גם על ה-Volume
MEDIA_ROOT = "/data/media"
