from aiogram import Bot, Dispatcher, types, executor
from config import tgToken
from keyboards.keyboard import get_keyboard_1,get_keyboard_2
from keyboards.inline_keyboard import get_inline_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from datetime import datetime


bot = Bot(token= tgToken)
dp = Dispatcher(bot)

keyboard_inline1 = InlineKeyboardMarkup(row_width=1)
b_inline1 = InlineKeyboardButton('2-ая страница', callback_data="go_to_2")
b2_inline1 = InlineKeyboardButton('Рандом число',callback_data='send_random')
keyboard_inline1.add(b_inline1,b2_inline1)

keyboard_inline2 = InlineKeyboardMarkup(row_width=1)
b_inline2 = InlineKeyboardButton('1-ая страница', callback_data="go_to_1")
b2_inline2 = InlineKeyboardButton('Время',callback_data='send_dataline')
keyboard_inline2.add(b_inline2,b2_inline2)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command= '/help', description='Команда для вывода доступных команд'),
        types.BotCommand(command='/inr',description="Для проверки инлайн клавиатуры")
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Я ЭХО бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == "Фото неба")
async def button_1_click(message: types.message):
    await bot.send_photo(message.chat.id, photo='https://www.google.com/imgres?q=berserk%20sky&imgurl=https%3A%2F%2Fexternal-preview.redd.it%2FmZDbGvIdZEInyKExlFMEpCG0perWu4EXXSt5UCdcgzI.jpg%3Fauto%3Dwebp%26s%3D80b05a2adbd4e1b705039984c457bc55ef6317cc&imgrefurl=https%3A%2F%2Fwww.reddit.com%2Fr%2FBerserk%2Fcomments%2F90u8pg%2Fgazing_up_at_the_dark_sky%2F&docid=bX2CCvJtzzHTKM&tbnid=gDxDv5HiO6FowM&vet=12ahUKEwjy062agLWGAxWbCBAIHUWlAbQQM3oECBsQAA..i&w=600&h=315&hcb=2&ved=2ahUKEwjy062agLWGAxWbCBAIHUWlAbQQM3oECBsQAA',caption="Небо",reply_markup=get_inline_keyboard())
@dp.message_handler(lambda message: message.text == "След")
async def button_2_click(message: types.message):
    await message.answer('2/2',reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == "Фото")
async def button_3_click(message: types.message):
    await bot.send_photo(message.chat.id, photo= 'https://cdn.britannica.com/95/156695-131-FF89C9FA/oak-tree.jpg?w=200&h=200&c=crop')

@dp.message_handler(lambda message: message.text == "Назад")
async def button_4_click(message: types.message):
    await message.answer("1/2", reply_markup= get_keyboard_1())
@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я готов помочь с...')

@dp.message_handler(commands='inr')
async def inr(message: types.Message):
    await message.reply("Первая клавиатура",reply_markup= keyboard_inline1)

@dp.callback_query_handler(lambda c: c.data == 'send_random')
async def send_random(callback_query: types.CallbackQuery):
    random_num = random.randint(1,100)
    await callback_query.message.answer(f'Случайное число {random_num}')

@dp.callback_query_handler(lambda c: c.data == 'send_dataline')
async def send_dataline(callback_query: types.CallbackQuery):
    times = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.edit_text(f'Время {times}')

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def next_second(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('2/2', reply_markup=keyboard_inline2)


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def next_second(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('1/2',reply_markup=keyboard_inline1)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispather):
    await set_commands(dispather.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
