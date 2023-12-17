from aiogram import Bot, Dispatcher
from core.handlers.default import start_bot, stop_bot
from core.database.core import DataBase

from core.handlers import stats

from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('TOKEN_BOT')

db = DataBase()
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()

async def start():
        
    try:
        
    
        dp.startup.register(start_bot)
    


        #statistics
        dp.include_router(
            stats.router
        )
        
        dp.shutdown.register(stop_bot)
    
        await dp.start_polling(bot)
    finally:
        await db.on_shutdown()
    