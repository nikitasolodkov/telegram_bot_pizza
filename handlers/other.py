from aiogram import types, Dispatcher
import json, string


# ----------------------------------------- ОБЩАЯ ЧАСТЬ ----------------------------------------- #


# Пустой handler обязательно должен быть в самом конце, т.к. хэндлеры читаюстя по порядку
# @dp.message_handler()
async def language_check(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
            await message.reply('Маты запрещены')
            await message.delete()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(language_check)