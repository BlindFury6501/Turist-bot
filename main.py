import logging
from turtle import clear
from aiogram import Bot, Dispatcher, executor, types, utils
import markup as nav
import typing


# Объект бота
bot = Bot(token="5011611505:AAG4imxGjIN3UNHc3JhuLWuKyJhBhHlSNfk")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard

@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, я бот Турист, помогу найти ближайший путь!\n\nВыбери места которые ты хочешь посетить', reply_markup= nav.mainMenu )



@dp.message_handler()
async def info(message: types.Message):
    if message.text == 'Хочешь узнать что делает бот?':
        await bot.send_message(message.from_user.id, 'Он найдёт лучший маршрут из предоставленых путей')
    elif message.text == 'Маршруты':
        await bot.send_message(message.from_user.id, 'Выбери несколько путей', reply_markup=nav.MarshMenu )
    elif message.text == 'Меню':
        await bot.send_message(message.from_user.id, 'Ты в меню', reply_markup=nav.mainMenu )
    elif message.text == 'Патрики,Кремль,ЦУМ':
        await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
        @dp.message_handler(content_types=['location'])
        async def handle_location(message: types.Message):
            lat = message.location.latitude
            lon = message.location.longitude
            reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
            await bot.send_message(message.from_user.id, 'https://yandex.ru/maps/?rtext=' + str(++lat) + ',' + str(++lon) + '~55.763873,37.592159~55.752004,37.617734~55.761035,37.619635&rtt=mt')
    else:
        await bot.send_message(message.from_user.id,'Пленку зажевало')
      

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
