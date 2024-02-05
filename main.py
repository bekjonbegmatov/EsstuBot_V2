# Importing aiogram modules

from aiogram import Dispatcher , Bot
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta, timezone

from heandlers.scheduler.scheduler import send_todays_data
from heandlers.scheduler.esstu_site.news_sender import send_news

# Import router from heandlers/start.py 
from heandlers.start import router
# Import Tocen from ./config.py
import config

# Main function
async def main():
    # Int the bot
    bot = Bot(token=config.TOCEN)
    dp = Dispatcher()

    
    scheduler = AsyncIOScheduler(timezone='Asia/Irkutsk')
    scheduler.add_job(func=send_todays_data,args=[bot], trigger='cron', hour=7, minute=0)
    # scheduler.add_job(func=news_sender, args=[bot], trigger='interval', seconds=10)
    scheduler.add_job(send_news, trigger='interval', seconds=10, args=[bot])

    scheduler.start()
    # Conecting router to the bot
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())