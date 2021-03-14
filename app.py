import os
from selenium import webdriver
import telebot
from telebot import types
from flask import Flask, request
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import *
import pickle
import schedule
import time
import random
import requests
import threading

# @siskiexpert
# -590852422 test group 2
# -506817497 test group 3
# -1001464385948 group_experts

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-sh-usage')

driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
driver.implicitly_wait(4)

group2 = -590852422
group3 = -506817497
group_experts = -1001464385948

launch = True

link_girls = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # bot.send_message(message.from_user.id, "Bot telegram_photo_phrase works")
    
    len_girls = len(link_girls)
    
    if len_girls == 0:
        get_girl_links()
        
    bot.send_message(message.from_user.id, text='Хочешь сиськи?', reply_markup=x_keyboard())
    # bot.send_message(message.from_user.id, message.from_user.id)



@bot.message_handler(commands=['send'])
def send_girl(message):
    bot.send_message(message.from_user.id, "Send Bot works")

    start_girl(message)

    # bot.send_message(message.from_user.id, "First girl completed")
    # schedule.every(50).seconds.do(run_threaded, send_ping_phrase)

    schedule.every(60).minutes.do(run_threaded, girl)
    # schedule.every(70).seconds.do(run_threaded, additional_check)
    schedule.every(180).minutes.do(run_threaded, girl_double)
    schedule.every(120).minutes.do(run_threaded, get_girl_links)

    # schedule.every(6).hours.do(girl)

    while launch:
        schedule.run_pending()
        time.sleep(1)


@bot.message_handler(commands=['send2'])
def send_girl(message):
    bot.send_message(message.from_user.id, "Send2 Bot works")
    
    len_girls = len(link_girls)
    
    if len_girls == 0:
        get_girl_links()

    girl_to_group_expert()


@bot.message_handler(commands=['send3'])
def send_girl(message):
    bot.send_message(message.from_user.id, "Send3 Bot works")

    len_girls = len(link_girls)

    if len_girls == 0:
        get_girl_links()

    girl_once_to_group2()



@bot.message_handler(commands=['stop'])
def stop_girl(message):

    global launch
    launch = False
    bot.send_message(message.from_user.id, "STOP is activated")



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    for_message = ['пока я туповат и никуя не понимаю', 'а вот и никуя', 'я просто эксперт по сиськам', 'да ладно?', 'отстань от меня человек', 'ой, всё', 'я в танке и ниипет', 'я устал, сегодня было много сисек']
    bot_message_random = random.randrange(0, len(for_message))
    bot_message = for_message[bot_message_random].capitalize()
    bot.send_message(message.chat.id, bot_message)


def start_girl(message):

    global launch
    launch = True
    bot.send_message(message.from_user.id, "Start is activated")

    get_girl_links()


def x_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Хочу', callback_data='Want')
    keyboard.add(btn1)
    btn2 = types.InlineKeyboardButton(text='Оочень хочу', callback_data='Very want')
    keyboard.add(btn2)
    btn3 = types.InlineKeyboardButton(text='Не надо, сегодня не стоит', callback_data='Cancel')
    keyboard.add(btn3)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Want":
        girl_once(call.message)

    elif call.data == "Very want":
        girl_once(call.message)

    elif call.data == "Cancel":
        msg = 'Пока пока, заходи еще ;)'
        bot.send_message(call.message.chat.id, msg)


# @bot.message_handler(func=lambda message: True)
# def send_girl_once(message):
#
#     bot.send_message(message.from_user.id, "Please wait, I am looking for sisechki")
#     girl_once(message)


def get_girl_links():
    page_random = random.randrange(1, 10)
    URL = 'https://xxx.pics/category/cute/' + str(page_random) + '/'

    page = requests.get(URL)

    if page.status_code != 200:

        while page.status_code != 200:
            page_random = random.randrange(1, 10)
            URL = 'https://xxx.pics/category/cute/' + str(page_random) + '/'
            page = requests.get(URL)

    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    all_pict_link = wait.until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'pcsrt-th-lightgallery-item')))
    # all_pict = len(path_to_pict)

    link_girls.clear()

    for item in all_pict_link:

        pict = item.get_attribute('data-src')
        page = requests.get(pict)

        pict_width = item.size["width"]

        if page.status_code == 200 and pict_width > 50:
            link_girls.append(pict)
        else:
            pass

    # len_ = len(link_girls)

   # bot.send_message(group2, f'===================== {len_}')


def phrase():
    guys = ['парни', 'ребятушки', 'братушки', 'ребятки', 'мужики', 'перцы', 'эксперты', 'экспертное сообщество',
            'мои герои', 'сладкие мои', 'chicos', 'sexo masculino']
    greeting = ['здарова', 'хая', 'салам', 'салют', 'здравствуйте', 'шалом', 'бонжур', 'хэллоу', 'хей',
                'буэнос диас',
                'хола', 'доброго дня', 'добрый день', 'ассалам алейкум', 'hola', 'prosperadlo', 'hola mis queridos']
    phrases = ['как вам мои чики?', 'попробуйте меня', 'какая я вкусненькая', 'посмотрите на мои вишенки',
               'как вам мои изюминки?', 'я вся горю', 'початимся?', 'пообщаемся?',
               'ох, не смотри на меня так', 'мои булочки готовы для вас', 'рада тут побывать',
               'всегда готова, жду вас тут', 'порадуйте меня чем нибудь', 'я секси, да?', 'я конфетка, да?',
               'сейчас позову подружек не хуже меня', 'сегодня здесь будет жарко', 'я вся горю',
               'классный денек сегодня, да?', 'погодка не фонтан, согрейте меня', 'всем хорошего дня!',
               'всем классного дня!', 'заходите поглядеть на меня еще', 'хватит палитьтся на мои титьки',
               'как я вам?', 'оцените меня экспертно', 'не сломайте об меня глаза', 'сиськи заказывали?',
               'как вам мои шары?']
    emoji = ['$)', ':)', ';)', 'oO', ':**', ' ', '..', 'уух', 'мм;)']

    guys_random = random.randrange(0, len(guys))
    greeting_random = random.randrange(0, len(greeting))
    phrases_random = random.randrange(0, len(phrases))
    emoji_random = random.randrange(0, len(emoji))

    willing_phrase = f'{guys[guys_random].capitalize()} {greeting[greeting_random]}! {phrases[phrases_random].capitalize()} {emoji[emoji_random]}'

    return willing_phrase


def phrase_once():
    guys = ['парень', 'кабан', 'братух', 'перец', 'мужик', 'эксперт', 'мой герой', 'сладкий мой', 'chico', 'парниш', 'крепыш']
    greeting = ['здарова', 'хая', 'салам', 'салют', 'здаров', 'шалом', 'бонжур', 'хэллоу', 'хей',
                'буэнос диас',
                'хола', 'доброго дня', 'добрый день', 'ассалам алейкум', 'hola', 'hola querido', 'эй']
    phrases = ['как тебе мои чики?', 'попробуй меня', 'какая я вкусненькая', 'посмотри на мои вишенки',
               'как тебе мои изюминки?', 'я вся горю', 'початимся?', 'пообщаемся?',
               'ох, не смотри на меня так', 'мои булочки готовы для тебя', 'рада тут побывать',
               'всегда готова, жду тебя тут', 'порадуй меня чем нибудь', 'я секси, да?', 'я конфетка, да?',
               'сейчас позову подружек не хуже меня', 'сегодня здесь будет жарко', 'я вся горю',
               'классный денек сегодня, да?', 'погодка не фонтан, согрей меня', 'хорошего дня!',
               'классного дня!', 'заходи поглядеть на меня еще', 'хватит палитьтся на мои титьки',
               'как я тебе?', 'оцени меня экспертно', 'не сломай об меня глаза', 'сиськи заказывал?',
               'как тебе мои шары?']
    emoji = ['$)', ':)', ';)', 'oO', ':**', ' ', '..', 'уух', 'мм;)']

    guys_random = random.randrange(0, len(guys))
    greeting_random = random.randrange(0, len(greeting))
    phrases_random = random.randrange(0, len(phrases))
    emoji_random = random.randrange(0, len(emoji))

    willing_phrase = f'{guys[guys_random].capitalize()} {greeting[greeting_random]}! {phrases[phrases_random].capitalize()} {emoji[emoji_random]}'

    return willing_phrase


def girl():
    #bot.send_message(group2, "girl starts")
    len_ = len(link_girls)

    while len_ == 0:
        time.sleep(30)

    # bot.send_message(group2, f'It`s the length of array girls in Girl() {len_}')

    pict = link_girls[random.randrange(0, len_)]

    try:
        bot.send_photo(group2, photo=pict)
    except Exception as e:
        #bot.send_message(group2, e)
        girl()

    phrase_to = phrase()
    bot.send_message(group2, phrase_to)


def girl_double():
   # bot.send_message(group2, "girl_double starts")
    len_ = len(link_girls)

    while len_ == 0:
        time.sleep(30)

    # bot.send_message(group2, f'It`s the length of array girls in Girl_double() {len_}')

    pict_to_both = link_girls[random.randrange(0, len_)]

    try:
        bot.send_photo(group2, photo=pict_to_both)
        bot.send_photo(group_experts, photo=pict_to_both)
    except Exception as e:
       # bot.send_message(group2, e)
       # bot.send_message(group3, e)
        girl_double()

    phrase_to = phrase()
    bot.send_message(group2, phrase_to)
    bot.send_message(group_experts, phrase_to)

    
    
def girl_to_group_expert():
    #bot.send_message(group2, "girl2 starts")
    len_ = len(link_girls)

    while len_ == 0:
        time.sleep(30)

    # bot.send_message(group2, f'It`s the length of array girls in Girl() {len_}')

    pict = link_girls[random.randrange(0, len_)]

    try:
        bot.send_photo(group_experts, photo=pict)
    except Exception as e:
        #bot.send_message(group2, e)
        girl_to_group_expert()

    phrase_to = phrase()
    bot.send_message(group_experts, phrase_to)


def girl_once(message):

    len_ = len(link_girls)

    while len_ == 0:
        time.sleep(30)

    pict = link_girls[random.randrange(0, len_)]
    phrase_to = phrase_once()

    # bot.send_message(message.chat.id, 'here')
    # bot.send_message(message.chat.id, message.chat.id)

    bot.send_photo(message.chat.id, photo=pict)
    bot.send_message(message.chat.id, phrase_to)


def girl_once_to_group2():
    bot.send_message(group2, 'test girl_once_to_group2')
    len_ = len(link_girls)

    while len_ == 0:
        time.sleep(30)

    pict = link_girls[random.randrange(0, len_)]
    phrase_to = phrase_once()

    # bot.send_message(message.chat.id, 'here')
    # bot.send_message(message.chat.id, message.chat.id)

    bot.send_photo(group2, photo=pict)
    bot.send_message(group2, phrase_to)


# def send_ping_phrase():
#  len_ = len(link_girls)
#  bot.send_message(group2, f'ping + {len_}')


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "it works", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_NAME + TOKEN)
    return "it worksssssssss", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
