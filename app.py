import os
from selenium import webdriver
import telebot
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

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-sh-usage')

driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
driver.implicitly_wait(4)


launch = True


@bot.message_handler(content_types=['text'])
def get_id(message):

    if message.text.lower() == 'getid':
        bot.send_message(227722043, message)
        bot.send_message(227722043, message.message_id)
        bot.send_message(227722043, message.chat.id)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Bot works")
    bot.send_message(message.from_user.id, message.from_user.id)



@bot.message_handler(commands=['stop'])
def stop_send_girl(message):

    stop_girl()
    bot.send_message(message.from_user.id, "Send girl Bot finished work")


def stop_girl():

    global launch
    launch = False


def start_girl():

    global launch
    launch = True


@bot.message_handler(commands=['send'])
def send_girl(message):

    bot.send_message(message.from_user.id, "Send Bot works")

    start_girl()
    bot.send_message(message.from_user.id, "Start Bot is activated")
    girl()
    bot.send_message(message.from_user.id, "First girl completed")


    schedule.every(2).minutes.do(girl)

    while launch:
        schedule.run_pending()
        time.sleep(1)


def girl():

    page = random.randrange(1, 10)
    URL2 = 'https://xxx.pics/category/cute/' + str(page) + '/'
    guys = ['парни', 'ребятушки', 'братушки', 'ребятки', 'мужики', 'перцы', 'эксперты', 'экспертное сообщество', 'мои герои', 'сладкие мои', 'chicos', 'sexo masculino']
    greeting = ['здарова', 'хая', 'салам', 'салют', 'здравствуйте', 'шалом', 'бонжур', 'хэллоу', 'хей', 'буэнос диас',
                'хола', 'доброго дня', 'добрый день', 'ассалам алейкум', 'hola', 'prosperadlo', 'hola mis queridos']
    phrases = ['как вам мои чики?', 'попробуйте меня', 'какая я вкусненькая', 'смотрите на мои вишенки',
               'как вам мои изюминки?', 'я вся горю', 'початимся?', 'пообщаемся?',
               'ох, не смотри на меня так', 'мои булочки готовы для вас', 'рада тут побывать',
               'всегда готова, жду вас тут', 'порадуйте меня чем нибудь', 'я секси, да?', 'я конфетка, да?',
               'сейчас позову подружек не хуже меня', 'сегодня здесь будет жарко', 'я вся горю',
               'классный денек сегодня, да?', 'погодка не фонтан, согрейте меня', 'всем хорошего дня!',
               'всем классного дня!', 'заходите поглядеть на меня еще', 'хватит палитьтся на мои титьки', 'как я вам?', 'оцените меня экспертно', 'не сломайте об меня глаза', 'сиськи заказывали?', 'как вам мои шары?']
    emoji = ['$)', ':)', ';)', 'oO', ':**', ' ', '..', 'уух', 'мм;)']

    guys_random = random.randrange(0, len(guys))
    greeting_random = random.randrange(0, len(greeting))
    phrases_random = random.randrange(0, len(phrases))
    emoji_random = random.randrange(0, len(emoji))

    willing_phrase = f'{guys[guys_random].capitalize()} {greeting[greeting_random]}! {phrases[phrases_random].capitalize()} {emoji[emoji_random]}'

    driver.get(URL2)
    wait1 = WebDriverWait(driver, 10)

    try:
        path_to_pict = wait1.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'pcsrt-th-lightgallery-item')))
    except Exception as error:
        bot.send_message(227722043, 'Item 1 not found')
        bot.send_message(227722043, error)

    try:
        all_pict = len(path_to_pict)
        pict_random = random.randrange(0, all_pict)
        time.sleep(2)
        pict = path_to_pict[pict_random].get_attribute('data-src')
    except Exception as error:
        bot.send_message(227722043, 'Item 2 not found')
        bot.send_message(227722043, error)

    try:
        bot.send_photo(227722043, photo=pict)
        bot.send_message(227722043, willing_phrase)
    except Exception as error:
        bot.send_message(227722043, 'Final error')
        bot.send_message(227722043, error)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "it works", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url = APP_NAME + TOKEN)
    return "it worksssssssss", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

