import os
import random
import telebot


bot = telebot.TeleBot('TOKEN BOTA')
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши help чтобы увидеть все команды!")



@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Я раставил все (кроме приветствия), по моему мнению вредящее атмосфере. # Если есть грамм. ошибки извините :( #
    Я умею:
    /hello - Приветствие
    /gas - углекислый газ
    /human - человек
    /ledniki - Ледники
    /zavod - заводы
    /car - машины
    /derevo - дерево
    /coal - сгорание угля
    /biomacc - биомасса 
    /volcan - вулкан
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Напиши команду /gas чтобы узнать из за чего выбрасывается углекислый газ.")

@bot.message_handler(commands=['human'])
def send_hello(message):
    bot.reply_to(message, "Человек выделяет в среднем 18–25 литров углекислого газа в час (около 1 кг в сутки) в процессе дыхания, что является конечным продуктом метаболизма. Этот процесс обеспечивает газообмен в легких, удаляя из венозной крови. Повышенная концентрация в закрытых помещениях вызывает головную боль и усталость.")

@bot.message_handler(commands=['gas'])
def send_gas(message):
    bot.reply_to(message, "Углекислый газ выбрасывается в основном из-за сжигания ископаемого топлива (угля, нефти, газа) для энергетики и транспорта, промышленных процессов (производство цемента), а также при вырубке лесов. Естественные источники включают дыхание людей и животных, извержения вулканов и разложение органики.")

@bot.message_handler(commands=['ledniki'])
def send_ledniki(message):
    with open('images\Ledniki.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Таяние ледников — ускоряющийся из-за глобального потепления процесс, при котором ежегодно теряется около 750 млрд тонн льда, что критически повышает уровень Мирового океана и угрожает запасам пресной воды.")  

@bot.message_handler(commands=['zavod'])
def send_zavod(message):
    with open('images\Zavod.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Заводы по производству углекислого газа улавливают его из дымовых газов ТЭЦ (абсорбционно-десорбционная технология) или производят сжиганием топлива.")

@bot.message_handler(commands=['car'])
def send_car(message):
    with open('images\Car.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Автомобили с ДВС выбрасывают в среднем 4,6 метрических тонн в год, составляя 61% выбросов дорожного транспорта.")

@bot.message_handler(commands=['derevo'])
def send_car(message):
    with open('images\Derevo.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Прекращение поглощения: Живые деревья работают как «фильтры», забирая из воздуха в процессе фотосинтеза. Когда дерево срубают, этот процесс останавливается.(И когда дерево срубают оно высвобождает весь углекислый газ, накопленный за года\века.)")

@bot.message_handler(commands=['coal'])
def send_car(message):
    with open('images\Ygol.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Сжигание ископаемого топлива (угля, нефти и природного газа) — главный источник антропогенных выбросов, меняющий климат из-за парникового эффекта.")

@bot.message_handler(commands=['biomacc'])
def send_car(message):
    with open('images\Biomacca.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Сжигание биомассы — это процесс использования органических материалов (древесина, отходы с/х) для выработки тепла и электроэнергии, считающийся углеродно-нейтральным, так как растения поглощают CO₂ при жизни.")

@bot.message_handler(commands=['volcan'])
def send_car(message):
    with open('images\Volcano.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
        bot.reply_to(message, "Наземные вулканы выбрасывают ~242 млн тонн ежегодно, тогда как деятельность человека — в 40–100 раз больше.")



bot.polling()
