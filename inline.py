from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text


import os, hashlib

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, InlineQueryResultArticle

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

answ = {}


# Кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка Y',url='https://www.youtube.com/')
urlButton2 = InlineKeyboardButton(text='Ссылка G',url='https://www.google.com/')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылки:', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Dislike', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_command(message : types.Message):
    await message.answer('За видео про деплой бота:', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали! Спасибо')
    else:
        await callback.answer('Вы уже проголосовали! Проголосовать можно только один раз', show_alert=True)

    await message.answer('За видео про деплой бота:', reply_markup=inkb)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/' +  text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id = result_id,
        title= 'Статья Wikipedia:',
        url = link,
        input_message_content=types.InputTextMessageContent(
            message_text=link
        )
    )]

    await query.answer(articles, cache_time=1, is_personal=True)






executor.start_polling(dp, skip_updates=True)