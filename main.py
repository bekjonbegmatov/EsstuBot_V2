# Importing aiogram modules
from aiogram import Dispatcher , Bot
import asyncio

# Import router from heandlers/start.py 
from heandlers.start import router
# Import Tocen from ./config.py
import config

# Main function
async def main():
    # Int the bot
    bot = Bot(token=config.TOCEN)
    dp = Dispatcher()
    # Conecting router to the bot
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())