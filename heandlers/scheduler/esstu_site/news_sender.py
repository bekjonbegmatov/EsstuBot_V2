from aiogram import Bot 
from aiogram.types import Message , InputMediaPhoto , FSInputFile 
# from aiogram.types.input_file import InputFile
from parcer.news_esstu.news_parcer import ESSTU_New
from aiogram.enums.parse_mode import ParseMode
from keyboards.inline.menu_inlie import news_link_button


async def send_news(bot:Bot):
    esstu = ESSTU_New()
    if esstu.is_any_news():
        # Getting data
        data = esstu.get_data()
        image = esstu.download_image()
        caption = f"""<b>{data['title']}</b>

<code>Тип : {data['type']}</code>

{data['des1']}

{data['des2']}....

<b>{data['info']}</b>
"""
        await bot.send_photo(
            photo=FSInputFile(
                path=image,
                ),
            chat_id=5163141099,
            caption=caption,
            parse_mode=ParseMode.HTML, 
            reply_markup=news_link_button(url=data['url']))

