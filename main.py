import logging, itertools, requests, time
from turtle import clear
from aiogram import Bot, Dispatcher, executor, types, utils
import markup as nav
from bs4 import BeautifulSoup
from urllib import response
#from db import BotDB
#
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter

bot = Bot(token="5011611505:AAG4imxGjIN3UNHc3JhuLWuKyJhBhHlSNfk")

dp = Dispatcher(bot)

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)

logging.basicConfig(level=logging.INFO)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    #if(not BotDB.user_exists(message.from_user.id)):
    #    BotDB.add_user(message.from_user.id)

    await bot.send_message(message.from_user.id, 'Привет, я бот Турист, помогу найти ближайший путь!\n\nВыбери места которые ты хочешь посетить', reply_markup=nav.mainMenu)


patrik = '~55.763873,37.592159'
krem = '~55.752004,37.617734'
tsum = '~55.761035,37.619635'
bteatr = '~55.760221,37.618561'
newarbat = '~55.751913,37.584901'
SobVas = '~55.752490,37.623205'
Hramkres = '~55.744561,37.605463'
Mgu = '~55.702612,37.530157'
Vdnx = '~55.828627,37.633823'
Parkpobeda = '~55.731222,37.506532'
ostan = '~55.819498,37.612141'
race = []





hya = 'https://yandex.ru/maps/?rtext='
mestaspisok = ['Патриаршие пруды', 'Большой театр', 'Новый Арбат', 'Кремль', 'Собор', 'Храм Христа Спасителя', 'МГУ', 'ВДНХ', 'Парк Победы', 'Останкинская']
mesta =  ('Патриаршие пруды', 'Большой театр', 'Новый Арбат', 'Кремль', 'Собор', 'Храм Христа Спасителя', 'МГУ', 'ВДНХ', 'Парк Победы', 'Останкинская')



@dp.message_handler()
async def info(message: types.Message):
    if message.text == 'Хочешь узнать что делает бот?':
        await bot.send_message(message.from_user.id, 'Он найдёт лучший маршрут из предоставленых путей')
    elif message.text == 'Меню':
        await bot.send_message(message.from_user.id, 'Ты в меню', reply_markup=nav.mainMenu)
    elif message.text == 'Достопримечательности':
        await bot.send_message(message.from_user.id, 'Выбери несколько точек которые ты хочешь посетить(Не больше трёх)', reply_markup=nav.MarshMenu)
        """Начало Точек"""
    elif message.text == 'Патриаршие пруды':
        race.append(patrik)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Кремль':
        race.append(krem)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'МГУ':
        race.append(Mgu)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Большой театр':
        race.append(bteatr)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Новый Арбат':
        race.append(newarbat)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'ВДНХ':
        race.append(Vdnx)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Храм Христа Спасителя':
        race.append(Hramkres)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Собор Василия Блаженного':
        race.append(SobVas)
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
    elif message.text == 'Парк Победы':
        race.append(Parkpobeda) 
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)    
    elif message.text == 'Останкинская телебашня':
        race.append(ostan)   
        if len(race) == 1:
            await bot.send_message(message.from_user.id, 'Выбери еще две точки', reply_markup=nav.MarshMenu)
        elif len(race) == 2:
            await bot.send_message(message.from_user.id, 'Выбери еще одну точку', reply_markup=nav.MarshMenu)
        elif len(race) == 3:
            await bot.send_message(message.from_user.id, 'Отправь мне свою локацию',reply_markup=types.ReplyKeyboardMarkup())
            @dp.message_handler(content_types=['location'])
            async def handle_location(message: types.Message):
                lat = message.location.latitude
                lon = message.location.longitude
                a1 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[1] + race[2] + '&rtt=mt'
                a2 =  hya + str(++lat) + ',' + str(++lon) + race[0] + race[2] + race[1] + '&rtt=mt'
                b1 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[2] + race[0] + '&rtt=mt'
                b2 =  hya + str(++lat) + ',' + str(++lon) + race[1] + race[0] + race[2] + '&rtt=mt'
                c1 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[0] + race[1] + '&rtt=mt'
                c2 =  hya + str(++lat) + ',' + str(++lon) + race[2] + race[1] + race[0] + '&rtt=mt'
                doroga = [a1, a2, b1, b2, c1, c2]
                timen = 10000
                put = 0
                for url in doroga:
                    response = requests.get(url)  # proxies=proxies)
                    time.sleep(0.1)
                    soup = BeautifulSoup(response.text, 'lxml')
                    quotes = soup.find_all('div', class_='masstransit-route-snippet-view__route-duration')
                    route = ''.join(itertools.filterfalse(str.isalpha, quotes[0].text))
                    print(route)
                    vremya = (int(route[0:3])*60) + int(route[3:5])
                    if timen >= vremya:
                        timen = vremya
                        put = url
                await bot.send_message(message.from_user.id, put)  
        """Конец Точек"""
    
    else:
        await bot.send_message(message.from_user.id, 'Пленку зажевало')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

