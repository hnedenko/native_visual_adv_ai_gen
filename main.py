import os
os.system('pip install -r requirements.txt')

from fastapi import FastAPI
app = FastAPI()

from config_manager import ConfigManager
config_manager = ConfigManager()

from modules import telegram_bots
telegram_bots.main()

os.system('uvicorn main:app --host 0.0.0.0 --port 8000 --reload')
