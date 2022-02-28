from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Меню')

# --- main menu ---
btnNews = KeyboardButton('Хочешь узнать что делает бот?')
btnMarsh = KeyboardButton('Маршруты')
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnNews, btnMarsh, )


#--- Marsh menu ---

btnPatrik = KeyboardButton('Патрики,Кремль,ЦУМ')
MarshMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnPatrik, btnMain)