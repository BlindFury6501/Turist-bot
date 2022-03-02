from telnetlib import KERMIT
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Меню')

# --- main menu ---
btnNews = KeyboardButton('Хочешь узнать что делает бот?')
btnMarsh = KeyboardButton('Достопримечательности')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnNews, btnMarsh, )


#--- Marsh menu ---

btnPatrik = KeyboardButton('Патриаршие пруды')
btnBteatr = KeyboardButton('Большой театр')
btnNewarbat = KeyboardButton('Новый Арбат')
btnkreml = KeyboardButton('Кремль')
btnSobVas = KeyboardButton('Собор Василия Блаженного')
btnHramkrest = KeyboardButton('Храм Христа Спасителя')
btnmgu = KeyboardButton('МГУ')
btnvdnx = KeyboardButton('ВДНХ')
btnpark = KeyboardButton('Парк Победы')
btnostank = KeyboardButton('Останкинская телебашня')
MarshMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnPatrik, btnBteatr, btnkreml, btnSobVas, btnHramkrest, btnmgu, btnvdnx, btnpark, btnostank, btnMain)
