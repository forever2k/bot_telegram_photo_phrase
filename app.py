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
# from fake_useragent import UserAgent

#@siskiexpert
# -590852422 test group 2
# -506817497 test group 3
bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

# ua = UserAgent()
# headers = {'User-Agent': ua.random}
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-sh-usage')
# # chrome_options.add_argument(headers)
#
# driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
# driver.implicitly_wait(4)
#
# group2 = -590852422
# group3 = -506817497
# # group_experts =
#
# launch = True


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Bot telegram_photo_phrase works")
    # bot.send_message(message.from_user.id, text='Хочешь сиськи?', reply_markup=x_keyboard())
    # bot.send_message(message.from_user.id, message.from_user.id)

#
# @bot.message_handler(commands=['send'])
# def send_girl(message):
#
#     bot.send_message(message.from_user.id, "Send Bot works")
#
#     start_girl()
#     bot.send_message(message.from_user.id, "Start Bot is activated")
#
#     # girl()
#     # bot.send_message(message.from_user.id, "First girl completed")
#     #
#     schedule.every(1).minutes.do(run_threaded, girl)
#     schedule.every(3).minutes.do(run_threaded, girl_double)
#     # # schedule.every(6).hours.do(girl)
#     #
#     while launch:
#         schedule.run_pending()
#         time.sleep(1)
#
#
# @bot.message_handler(commands=['stop'])
# def stop_send_girl(message):
#
#     stop_girl()
#     bot.send_message(message.from_user.id, "Send girl Bot finished work")
#
#
# def stop_girl():
#
#     global launch
#     launch = False
#
#
# def start_girl():
#
#     global launch
#     launch = True
#
#
# def x_keyboard():
#     keyboard = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Хочу', callback_data='Want')
#     keyboard.add(btn1)
#     btn2 = types.InlineKeyboardButton(text='Оочень хочу', callback_data='Very want')
#     keyboard.add(btn2)
#     btn3 = types.InlineKeyboardButton(text='Не надо, сегодня не стоит', callback_data='Cancel')
#     keyboard.add(btn3)
#     return keyboard
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#
#     if call.data == "Want":
#         girl_once(call.message)
#
#     elif call.data == "Very want":
#         girl_once(call.message)
#
#     elif call.data == "Cancel":
#         msg = 'Пока пока'
#         bot.send_message(call.message.chat.id, msg)
#
#
# # @bot.message_handler(func=lambda message: True)
# # def send_girl_once(message):
# #
# #     bot.send_message(message.from_user.id, "Please wait, I am looking for sisechki")
# #     girl_once(message)
#
#
#
# def girl_parse():
#
#     try:
#         page = random.randrange(1, 10)
#         URL2 = 'https://xxx.pics/category/cute/' + str(page) + '/'
#         driver.get(URL2)
#         wait1 = WebDriverWait(driver, 10)
#
#         path_to_pict = wait1.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'pcsrt-th-lightgallery-item')))
#         all_pict = len(path_to_pict)
#         pict_random = random.randrange(0, all_pict)
#         time.sleep(2)
#         pict = path_to_pict[pict_random].get_attribute('data-src')
#
#         return pict
#
#     except:
#         girl_parse()
#
#
# def phrase():
#
#     guys = ['парни', 'ребятушки', 'братушки', 'ребятки', 'мужики', 'перцы', 'эксперты', 'экспертное сообщество',
#             'мои герои', 'сладкие мои', 'chicos', 'sexo masculino']
#     greeting = ['здарова', 'хая', 'салам', 'салют', 'здравствуйте', 'шалом', 'бонжур', 'хэллоу', 'хей',
#                 'буэнос диас',
#                 'хола', 'доброго дня', 'добрый день', 'ассалам алейкум', 'hola', 'prosperadlo', 'hola mis queridos']
#     phrases = ['как вам мои чики?', 'попробуйте меня', 'какая я вкусненькая', 'смотрите на мои вишенки',
#                'как вам мои изюминки?', 'я вся горю', 'початимся?', 'пообщаемся?',
#                'ох, не смотри на меня так', 'мои булочки готовы для вас', 'рада тут побывать',
#                'всегда готова, жду вас тут', 'порадуйте меня чем нибудь', 'я секси, да?', 'я конфетка, да?',
#                'сейчас позову подружек не хуже меня', 'сегодня здесь будет жарко', 'я вся горю',
#                'классный денек сегодня, да?', 'погодка не фонтан, согрейте меня', 'всем хорошего дня!',
#                'всем классного дня!', 'заходите поглядеть на меня еще', 'хватит палитьтся на мои титьки',
#                'как я вам?', 'оцените меня экспертно', 'не сломайте об меня глаза', 'сиськи заказывали?',
#                'как вам мои шары?']
#     emoji = ['$)', ':)', ';)', 'oO', ':**', ' ', '..', 'уух', 'мм;)']
#
#     guys_random = random.randrange(0, len(guys))
#     greeting_random = random.randrange(0, len(greeting))
#     phrases_random = random.randrange(0, len(phrases))
#     emoji_random = random.randrange(0, len(emoji))
#
#     willing_phrase = f'{guys[guys_random].capitalize()} {greeting[greeting_random]}! {phrases[phrases_random].capitalize()} {emoji[emoji_random]}'
#
#     return willing_phrase
#
#
# def girl():
#
#     pict_to = girl_parse()
#     phrase_to = phrase()
#
#     bot.send_photo(group2, photo=pict_to)
#     bot.send_message(group2, phrase_to)
#
#
# def girl_double():
#
#     pict_to = girl_parse()
#     phrase_to = phrase()
#
#     bot.send_photo(group2, photo=pict_to)
#     bot.send_message(group2, phrase_to)
#     bot.send_photo(group3, photo=pict_to)
#     bot.send_message(group3, phrase_to)
#
#
# def girl_once(message):
#
#     pict_to = girl_parse()
#     phrase_to = phrase()
#
#     bot.send_message(message.chat.id, 'here')
#     bot.send_message(message.chat.id, message.chat.id)
#
#     bot.send_photo(message.chat.id, photo=pict_to)
#     bot.send_message(message.chat.id, phrase())
#
#
#
# def run_threaded(job_func):
#     job_thread = threading.Thread(target=job_func)
#     job_thread.start()



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


