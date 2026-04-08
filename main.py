import os
import random
import telebot


bot = telebot.TeleBot('8676742334:AAH_aE-7vk7wa-0FcvEJStwyhjhkBWRJems')
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши help чтобы увидеть все команды!")



@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Я умею:
    /hello - Приветствие
    /gas - углекислый газ
    /ledniki - Ледники
    /zavod - заводы
    /car - машины
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Напиши help чтобы узнать список команд.")

@bot.message_handler(commands=['gas'])
def send_gas(message):
    bot.reply_to(message, "Углекислый газ один из факторов из за которого глобальное потепление. Углекислый газ задерживает солнечное тепло")

@bot.message_handler(commands=['ledniki'])
def send_ledniki(message):
    with open('images\Ledniki.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Ледники таят, а из за этого поднимаеться уровень океана и глобальное потепление тоже из за них")  

@bot.message_handler(commands=['zavod'])
def send_zavod(message):
    with open('images\Zavod.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Вот фото завода из которого валит углекислый газ.")

@bot.message_handler(commands=['car'])
def send_car(message):
    with open('images\Car.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Машины это один из множества источников углекислого газа.")




bot.polling()
