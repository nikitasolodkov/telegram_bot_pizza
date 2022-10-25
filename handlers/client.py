from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# ----------------------------------------- КЛИЕНТСКАЯ ЧАСТЬ ----------------------------------------- #
# @dp.message_handler(commands=['start', 'help'])
async def comand_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Pizza_Sheef_Nik_Bot')

# @dp.message_handler(commands=['Режим_работы', 'open'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# @dp.message_handler(commands=['Расположение', 'place'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')
    # await bot.send_message(message.from_user.id, 'ул. Колбасная 15', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Меню', 'menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)



# @dp.message_handler(lambda message: 'такси' in message.text)
# async def taxi(message: types.Message):
#     await message.answer('Такси можно заказать по номеру +777')

@dp.message_handler(lambda message: 'нло' in message.text)
async def ufo(message: types.Message):
    await message.answer('Мне не страшны НЛО!\nНа мне шапочка из фольги!')

@dp.message_handler(lambda message: message.text.startswith('такси'))
async def taxes(message: types.Message):
    await message.answer(message.text[6:])

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(comand_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы', 'open'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение', 'place'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню', 'menu'])