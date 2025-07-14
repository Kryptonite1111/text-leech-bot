import os

API_ID    = os.environ.get("API_ID", "26363853")
API_HASH  = os.environ.get("API_HASH", "a3fdf866db0a77e3853a0b54ead149f7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8057461685:AAH1Q4Erfyv8ce2ZzDHd_fCseQCAqgyJqq0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
