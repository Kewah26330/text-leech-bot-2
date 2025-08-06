import os

API_ID    = os.environ.get("API_ID", "23551823")
API_HASH  = os.environ.get("API_HASH", "36727c8db0a63181fe9963f605cc4ef4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7656304872:AAF_lVk_BZA1de6KDuAVdb4KwFqGp0S5WNk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
