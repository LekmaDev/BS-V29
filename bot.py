import telebot
import random
import json

bot = telebot.TeleBot('6263031696:AAEihY8-KyBsLSlXiaAY7nXZJBTbn5MePgo')

@bot.message_handler(commands=['start'])
def add_offer(message):
    bot.reply_to(message, 'Создать свою акцию напишите /new_offer\nХочите больше возможностей купите вип\nКупить вип - @itdlaloxov')

@bot.message_handler(commands=['new_offer'])
def add_offer(message):
    user_id = message.from_user.id
    with open("config.json", "r", encoding='utf-8') as f:
        config = json.load(f)
    if user_id not in config["CO"] or user_id in config["VIPTG"]:
        config["CO"].append(user_id)
        with open("config.json", "w", encoding='utf-8') as f:
            json.dump(config, f, indent=4)
        who = 0
        who = random.choice([1,16])
        Multiplier = 0
        if len(message.text.split()) <= 1:
            bot.reply_to(message, 'Используйте команду /new_offer Название Акции')
            return
        offer_data = ' '.join(message.text.split()[1:])  # Записываем все данные после пробела
        if who == 1:
            Multiplier = random.randint(200,1007)
        elif who == 16:
            Multiplier = random.randint(1,48)
        new_offer = {
            'ID': [who, 0, 0],
            'OfferTitle': offer_data,
            'Cost': 0,
            'OldCost': 0,
            'Multiplier': [Multiplier, 0, 0],
            'BrawlerID': [0, 0, 0],
            'SkinID': [0, 0, 0],
            'WhoBuyed': [],
            'Timer': 86400,
            'OfferBGR': random.choice(["offer_generic","offer_special","offer_legendary","offer_coins","offer_gems","offer_boxes","offer_finals","offer_xmas","offer_lny","offer_pin_pack","offer_chromatic","offer_archive","offer_moon_festival"]),
            'ShopType': 0,
            'ShopDisplay': 0
        }
        with open('Logic/offers.json', 'r', encoding='utf-8') as f:
            offers = json.load(f)
        offers[str(len(offers))] = new_offer
        with open('Logic/offers.json', 'w', encoding='utf-8') as f:
            json.dump(offers, f, indent=4)
        bot.reply_to(message, 'Новая акция добавлена!')
    else:
        bot.reply_to(message, 'Вы уже создали акцию!')

bot.polling()
