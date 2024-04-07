import telebot
import logging
from telebot import types
import random
from random import choice

from model_wrapper import ModelWrapper

"""
get_text_messages - обработка любого текстового сообщения, в том числе того, что отправился при нажатии кнопки.

Методы, реализующие одноименные команды телеграм-боту:
start
help
generate
checkmodel
model
"""

TOKEN = # your token
bot = telebot.TeleBot(TOKEN)

model_wrapper = ModelWrapper() # внутри класса описание

# Базовая конфигурация: уровень логирования и формат сообщения
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@bot.message_handler(commands=['help'])
def help(message):
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} need help.")
    help_message = """Доступны следующие команды:
/start старт бота
/model выбор модели
/checkmodel посмотреть, как модель сейчас загружена
/generate сгенерировать текст по контексту (можно использовать без введения команды)
"""
    bot.send_message(message.from_user.id, help_message)


@bot.message_handler(commands=['start'])
def start(message):
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} started the conversation.")
    bot.send_message(message.from_user.id, "Привет! Для знакомства с доступными командами введите /help")


@bot.message_handler(commands=['model'])
def model(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("StatLM")
    btn2 = types.KeyboardButton("GPT")
    btn3 = types.KeyboardButton("Llama")
    markup.add(btn1, btn2, btn3)
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} wanted to choose model.")
    bot.send_message(message.from_user.id, "Выберите модель для генерации", reply_markup=markup)


@bot.message_handler(commands=['checkmodel'])
def checkmodel(message):
    current_model = model_wrapper.current_model_name
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} wanted to check current model ({str(current_model)}).")
    bot.send_message(message.from_user.id, f"Текущая модель: {str(current_model)}")


@bot.message_handler(commands=['generate'])
def generate(message):
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} wanted to talk.")
    
    bot.send_message(message.from_user.id,
                     "Введите текст (вопрос, на который нужно ответить, либо текст, который нужно продолжить)")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    logger.info(f"User_{message.from_user.id} {message.from_user.first_name} said: {message.text}.")
    if message.text in ['StatLM', 'GPT', 'Llama']:
        logger.info(f"{message.text} - current model {model_wrapper.current_model_name}.")
        status, result = model_wrapper.load(message.text, test_inference=True)
        if status:
            bot.send_message(message.from_user.id, "Подгружено")
        else:
            bot.send_message(message.from_user.id, f"Проблемы с загрузкой модели, ниже описаны ошибки.\n{result}")
    else:
        status, result = model_wrapper.generate(message.text)
        if status:
            bot.send_message(message.from_user.id, result)
        else:
            bot.send_message(message.from_user.id, f"Проблемы с генерацией, ниже описаны ошибки.\n{result}")


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
