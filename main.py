# Importing aiogram modules

from aiogram import Dispatcher , Bot
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta, timezone

from heandlers.scheduler.scheduler import send_todays_data , send_tomorows_data
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

    """ This is a shedulers hahahahaha !!!! """
    scheduler = AsyncIOScheduler(timezone='Asia/Irkutsk')
    # This sheduler for sending todays data in 7:00 am 
    scheduler.add_job(func=send_todays_data, args=[bot], trigger='cron', hour=7, minute=0)
    # This sheduler for sending tomorows data in 7:00 pm
    scheduler.add_job(func=send_tomorows_data, args=[bot], trigger='cron', hour=19, minute=0)
    # This sheduler for checking news in esstu.ru 
    scheduler.add_job(send_news, trigger='interval', seconds=30, args=[bot])

    scheduler.start()
    # Conecting router to the bot
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())