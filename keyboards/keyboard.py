from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton('Фото неба')
    button_2 = KeyboardButton('След')
    keyboard.add(button_1,button_2)
    return keyboard

def get_keyboard_2():
    keyboard2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton('Фото')
    button_4 = KeyboardButton('Назад')
    keyboard2.add(button_3,button_4)
    return keyboard2