from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    b_inline = InlineKeyboardButton('Посмотреть', url='https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D0%BE')
    b_inline2 = InlineKeyboardButton('Посмотреть', url='https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D0%BE#%D0%97%D0%B5%D0%BC%D0%BD%D0%BE%D0%B5_%D0%BD%D0%B5%D0%B1%D0%BE')
    keyboard_inline.add(b_inline, b_inline2)
    return keyboard_inline

