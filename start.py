import telebot 
import random 
import json
from Utils.Helpers import Helpers
from quests import auto_quests
import sqlite3
import subprocess
# создаем бота
admin=[1156896214,5690225560]
#5690225560 - Lekma
#1156896214 - Я макс
bot = telebot.TeleBot('5772083305:AAHL49TU8zO2DDSRrJf9aKXSj1QoQUEs_1o')
# Функция для получения списка всех акций из файла offers.json
def get_offers():
    # Читаем данные из файла offers.json
    with open("Logic/offers.json", "r",encoding='utf-8') as f:
        data = json.load(f)

    # Генерируем текстовый список всех акци
    offer_list = "Список акций:\n"
    for offer_id, offer_data in data.items():
        vault=offer_data['ShopType']
        daily=offer_data['ShopDisplay']
        current=""
        types=""
        if vault==1:current="Золото"
        elif vault==0:current="Кристаллы"
        if daily==1:types="Ежедневная"
        elif daily==0:types="Обычная"
        offer_list += f"\nАкция #{offer_id}\n"
        offer_list += f"Название: {offer_data['OfferTitle']}\n"
        offer_list += f"Тип: {types}\n"
        offer_list += f"Боец: {offer_data['BrawlerID'][0]}\n"
        offer_list += f"Скин: {offer_data['SkinID'][0]}\n"
        offer_list += f"Валюта: {current}\n"
        offer_list += f"Стоимость: {offer_data['Cost']}\n"
        offer_list += f"Множитель: {offer_data['Multiplier'][0]}\n"

    # Возвращаем текстовый список всех акций
    return offer_list
# Обработчик команды /list
@bot.message_handler(commands=['list'])
def handle_list_offers(message):
    # Получаем список всех акций из файла offers.json
    offer_list = get_offers()

    # Отправляем пользователю список всех акций
    bot.send_message(chat_id=message.chat.id, text=offer_list)
    
    
@bot.message_handler(commands=['new_offer'])
def add_offer(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, 'Используйте команду /new_offer с аргументами в формате: /new_offer <ID> <OfferTitle> <Cost> <Multiplier> <BrawlerID> <SkinID> <OfferBGR> <ShopType> <ShopDisplay>')
            return
        offer_data = message.text.split()
        new_offer = {
            'ID': [int(offer_data[1]), 0, 0],
            'OfferTitle': offer_data[2],
            'Cost': int(offer_data[3]),
            'OldCost': 0,
            'Multiplier': [int(offer_data[4]), 0, 0],
            'BrawlerID': [int(offer_data[5]), 0, 0],
            'SkinID': [int(offer_data[6]), 0, 0],
            'WhoBuyed': [],
            'Timer': 86400,
            'OfferBGR': offer_data[7],
            'ShopType': int(offer_data[8]),
            'ShopDisplay': int(offer_data[9])
        }
        with open('Logic/offers.json', 'r',encoding='utf-8') as f:
           offers = json.load(f)
        offers[str(len(offers))] = new_offer
        with open('Logic/offers.json', 'w',encoding='utf-8') as f:
           json.dump(offers, f, indent=4)
        bot.reply_to(message, 'Новая акция добавлена!')
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in admin:
        bot.reply_to(message, "/list - Посмотреть список акций.\n/new_offer - создает новую акцию.\n/remove_offer - Удалить акцию.\n/theme - Изменить всем фон\n/new_code - Добавить новый код Автора.\n/del_code - Удалить код Автора.\n/code_list - Список кодов Автора.\n/auto_shop - Обновить ежедневынй магазин.\n/add_vip - Выдать вип статус.\n/del_vip - Забрать вип статус.\n/add_gems - Выдать гемов игроку.\n/ban - Выдать бан игроку")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
@bot.message_handler(commands=['remove_offer'])
def remove_offer(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) != 2:
           bot.reply_to(message, 'Используйте команду /remove_offer с аргументом в формате: /remove_offer <ID>')
           return
        offer_id = message.text.split()[1]
        with open('Logic/offers.json', 'r', encoding='utf-8') as f:
            offers = json.load(f)
        if offer_id not in offers:
            bot.reply_to(message, f'Акция с ID {offer_id} не найдена')
            return
        offers.pop(offer_id)
        with open('Logic/offers.json', 'w', encoding='utf-8') as f:
            json.dump(offers, f)
        bot.reply_to(message, f'Акция с ID {offer_id} удалена')
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
# Определяем функцию-обработчик для команды /theme
@bot.message_handler(commands=['theme'])
def theme(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Выбери ID темы\n0 - Обычная\n1 - Новый год (Снег)\n2 - Красный новый год\n3 - От клеш рояля\n5 - Желтые панды\n6 - Фиолетовый булл\n7 - Роботы Зелёный фон\n8 - Фиолетовый фон\n9 - Пиратский фон\n11 - Футбольный фон\nИспользовать команду /theme ID")
        else:
            user_id = message.from_user.id
            theme_id = message.text.split()[1]
            conn = sqlite3.connect("database/Player/plr.db")
            c = conn.cursor()
            c.execute(f"UPDATE plrs SET theme={theme_id}")
            conn.commit()
            c.execute("SELECT * FROM plrs")
            conn.close()
            bot.send_message(chat_id=message.chat.id, text=f"Айди всех записей был изменён на {theme_id}")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
#коды автора
@bot.message_handler(commands=['new_code'])
def new_code(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /new_code Название Кода(На англ)")
        else:
            code = message.text.split()[1]
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code not in config["CCC"]:
                config["CCC"].append(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"Новый код {code}, Был добавлен!")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"Код {code} уже существует!")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")

@bot.message_handler(commands=['code_list'])
def code_list(message):
    with open('config.json', 'r') as f:
        data = json.load(f)
    code_list = '\n'.join(data["CCC"])
    bot.send_message(chat_id=message.chat.id, text=f"Список кодов: \n{code_list}")
        
        
@bot.message_handler(commands=['del_code'])
def del_code(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /del_code Название Кода")
        else:
            code = message.text.split()[1]
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code in config["CCC"]:
                config["CCC"].remove(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"Код {code}, Был удалён!")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"Код {code} не найден!")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
 #конец кодов
#Вип Старт
 
@bot.message_handler(commands=['add_vip'])
def add_vip(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /add_vip ID(Можно узнать в профиле профиле при поставке цветного ника)")
        else:
            vip_id = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if vip_id not in config["vips"]:
                config["vips"].append(vip_id)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"Вип статус был выдан игроку с ID {vip_id}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"Вип статус уже есть у ID {vip_id}")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")

		
@bot.message_handler(commands=['del_vip'])
def del_vip(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /del_vip ID(Можно узнать в профиле профиле при поставке цветного ника)")
        else:
            code = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code in config["vips"]:
                config["vips"].remove(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"Вип статус был удален у игрока с ID {code}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"Вип статус не найден у игрока с ID {code}")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")


#Конец випов
@bot.message_handler(commands=['auto_shop'])
def auto_shop(message):
    user_id = message.from_user.id
    if user_id in admin:
        with open('Logic/offers.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i in range(11): # изменяем первые 5 записей по ID
            if i <= 5:
                new_offer = {
                'ID': [8, 0, 0],
                'OfferTitle': "daily",
                'Cost': random.randint(10, 228),
                'OldCost': 0,
                'Multiplier': [random.randint(1, 100), 0, 0],
                'BrawlerID': [random.randint(1, 30), 0, 0],
                'SkinID': [0, 0, 0],
                'WhoBuyed': [],
                'Timer': 86400,
                'OfferBGR': "offer_gems",
                'ShopType': 1,
                'ShopDisplay': 1
                }
                data[i] = new_offer
            elif i > 5:
                with open('config.json', 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                skins = settings['Skins']
                random_skin = random.choice(skins)
                settings['Skins'] = skins
                with open('config.json', 'w', encoding='utf-8') as f:
                    json.dump(settings, f, indent=4, ensure_ascii=False)
                new_offer = {
                'ID': [4, 0, 0],
                'OfferTitle': "DAILY SKIN",
                'Cost': random.randint(10, 228),
                'OldCost': 0,
                'Multiplier': [0, 0, 0],
                'BrawlerID': [0, 0, 0],
                'SkinID': [random_skin, 0, 0],
                'WhoBuyed': [],
                'Timer': 86400,
                'OfferBGR': "offer_gems",
                'ShopType': 0,
                'ShopDisplay': 0
                }
                data[i] = new_offer
        with open('Logic/offers.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        auto_quests.generator()
        bot.reply_to(message, 'Акции успешно обновлены!')
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")

		
		
# add_gems
@bot.message_handler(commands=['add_gems'])
def add_gems(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /add_gems ID AMMOUNT")
        else:
            user_id = message.from_user.id
            id = message.text.split()[1]
            ammount = message.text.split()[2]
            conn = sqlite3.connect("database/Player/plr.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET gems = ? WHERE lowID = ?", (ammount, id))
            conn.commit()
            conn.close()
            bot.send_message(chat_id=message.chat.id, text=f"Игроку с айди {id} Выдали {ammount} Гемов")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
		
@bot.message_handler(commands=['ban'])
def ban(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /ban ID")
        else:
            vip_id = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if vip_id not in config["vips"]:
                config["vips"].append(vip_id)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"Бан был выдан игроку {vip_id}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"Бан уже есть у игрока {vip_id}")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
@bot.message_handler(commands=['unbanip'])
def unbanip(message):
    user_id = message.from_user.id
    if user_id in admin:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /unbanip IP")
        else:
            ip = message.text.split()[1]
            command = f"iptables -D INPUT -s {ip} -j DROP"
            try:
                subprocess.run(command, shell=True, check=True)
                bot.send_message(chat_id=message.chat.id, text=f"Разбанен {ip}")
            except subprocess.CalledProcessError as e:
                bot.reply_to(message, "Ошибка выполнения команды iptables")
    else:
        bot.reply_to(message, "Вы не являетесь администратором!")
# Запускаем бота
bot.polling()