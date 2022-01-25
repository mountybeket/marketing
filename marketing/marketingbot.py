import config
import telebot
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smmgold-83715-default-rtdb.firebaseio.com/' })

bot = telebot.TeleBot(config.token) #должно быть в начале. Вызывает токен

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    current = db.reference("/bot/users/"+str(user_id)+"/current").get()

    bot.send_message(message.from_user.id,"Привет! Доброе пожаловать на курс «SMM курс с нуля до PRO!» 👋 \n \n Как я могу к вам обращаться?")
    db.reference("/bot/users/"+str(user_id)).update({"current": "who"})


@bot.message_handler(content_types = ['text'])
def start_dialog(message):
    user_id = message.from_user.id
    current = db.reference("/bot/users/"+str(user_id)+"/current").get()
    if current == "who":
        user_id = message.from_user.id
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔥 О нас", "🖥 О курсе")
        user_markup.row("⚡️ Программа", "👩🏻 Преподаватель")
        user_markup.row("✅ Записаться на курс")
        db.reference("/bot/users/"+str(user_id)).update({"name": message.text})
        name = db.reference("/bot/users/"+str(user_id)+"/name").get()
        bot.send_message(user_id, name + ", что тебя интересует?",reply_markup = user_markup)

        db.reference("/bot/users/"+str(user_id)).update({"current": "text"})

    elif current == "text":
        if message.text == "🔥 О нас":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("◀️ Назад")
            bot.send_photo(user_id, photo=open('4.jpg', 'rb'), caption = "Сегодня в креативе больше исключений, чем правил. То, что было круто утром – после обеда уже клише. Тренды меняются быстрее, чем ты моргаешь, а реклама похожа на что угодно кроме рекламы. \n \n GOLDSMM – это онлайн-курсы для тех, кто хочет стартовать быстро. База и авторские коллаборации с лучшими практиками рекламы, медиа, кино и искусства. Здесь ты получишь инструменты и навыки. Здесь только труд. Зато так быстрее.",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block"})

        elif message.text == "🖥 О курсе":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("◀️ Назад")
            bot.send_photo(user_id, photo=open('1.jpg', 'rb'), caption = "На курсе мы разберем возможности 8 соцсетей: от телеграма — до тиктока, ютуба и стримингов. ⚡️ \n \n За 13 занятий ты разработаешь экосистему соцсетей, карту пути клиента, идеи для коллабораций с инфлюенсерами и план продвижения своего проекта. ✅ \n \n На каждом этапе тебя будет ждать личный фидбек от методиста и поддержка от нас. В итоге у твоих проектов будет расти не только количество подписчиков, но и продажи. 💵",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block"})

        elif message.text == "⚡️ Программа":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("◀️ Назад")
            bot.send_photo(user_id, photo=open('3.jpg', 'rb'), caption = "ПРОГРАММА ⚡️ \n \n1. АКТУАЛЬНЫЕ СОЦИАЛЬНЫЕ МЕДИА И ВИЗУАЛЬНЫЕ ТРЕНДЫ \n \n2. ЧЕМ МОЖЕТ УДИВИТЬ INSTAGRAM И FACEBOOK\n \n3. TIKTOK И YOUTUBE\n \n4. АКТУАЛЬНЫЕ СОЦИАЛЬНЫЕ МЕДИА В IT И E-COM",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block"})

        elif message.text == "👩🏻 Преподаватель":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
            user_markup.row("◀️ Назад")
            bot.send_photo(user_id, photo=open('2.jpg', 'rb'), caption = " ⚡ MARIA AZBUKA ⚡ \n\nОСНОВАТЕЛЬ АГЕНТСТВА «GOLDSMM»\n\nреализовала 50+ SMM-проектов для брендов 💵\n\nработала Head of SMM в LK",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "block"})

        elif message.text == "✅ Записаться на курс":
            user_id = message.from_user.id
            keyboard = types.InlineKeyboardMarkup()
            btn_url = types.InlineKeyboardButton(text = "Записаться на курс", url = "https://www.instagram.com/")
            keyboard.add(btn_url)
            bot.send_photo(user_id, photo=open('5.jpg', 'rb'), reply_markup = keyboard)


        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

    elif current == "block":
        if message.text == "◀️ Назад":
            user_id = message.from_user.id
            user_markup = telebot.types.ReplyKeyboardMarkup(True)
            user_markup.row("🔥 О нас", "🖥 О курсе")
            user_markup.row("⚡️ Программа", "👩🏻 Преподаватель")
            user_markup.row("✅ Записаться на курс")
            name = db.reference("/bot/users/"+str(user_id)+"/name").get()
            bot.send_message(user_id, name + ", что тебя интересует?",reply_markup = user_markup)

            db.reference("/bot/users/"+str(user_id)).update({"current": "text"})

        else:
            bot.send_message(message.from_user.id,"Ошибка! Выберите из перечисленных.")

        
        

    else:
        bot.send_message(message.from_user.id,"Ошибка!")




bot.polling(none_stop=True, interval = 2) #в конце. Бесконечно.
