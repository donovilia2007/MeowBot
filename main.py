import random
import telebot

myfile = open("token.txt", "r")
token = myfile.readline()

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я MeowBot. Добавь меня в группу!)")
@bot.message_handler(content_types='text')
def meow_message(message):
    stickers = ["CAACAgIAAxkBAAEI36xkVi-IHO1ZWOOJCYFcFJf-zIIb0wACBysAAoR8YUq2U7Hp5AUGUy8E", "CAACAgIAAxkBAAEI365kVjDgA4T7tnyMJFsdZLZ7z2DpZQACiBQAAt1UiEhq5leDRkloOC8E", "CAACAgIAAxkBAAEI37BkVjDtujHvplA34QtJogABd1lEUJ4AAlgYAAKN8mlK6l0i58byXbYvBA",
                "CAACAgIAAxkBAAEI37JkVjDxAq81VsIhjLp_JQi2cHoK1QACERcAAvB-aUox4OhdeE_1Ji8E", "CAACAgIAAxkBAAEI37RkVjDzjGFydg9YZYKlQAfVnYoZkQACQxoAAhwccEout35UFqYW8i8E", "CAACAgIAAxkBAAEI37ZkVjD2OAQCEyXazaJigPg8gs-S7wACziAAAhVKcErU-Du4zzot_i8E",
                "CAACAgIAAxkBAAEI37hkVjD57s4O-ObvcLy96BY3utIDPAAC-RoAArvIcEqXnnfEQ9chKi8E", "CAACAgIAAxkBAAEI37pkVjD7V4OZ6yTrLnyKdGjrbCKIhAACQB0AArSmcUp7T8J6NpOA0C8E", "CAACAgIAAxkBAAEI37xkVjD9XcwNAZtfwg-th6cN3YEs3gACDRsAAutlcErzh1BYTYro5y8E",
                "CAACAgIAAxkBAAEI375kVjEBZlV7DSM8MXLw44BdQMLxEAACxxgAAvcn8EpOfHUR8eeh2y8E", "CAACAgIAAxkBAAEI38BkVjEE6Bs6u307ci42OzHKYfjKugACvx0AAie4wUtUl3L1ZEL1ci8E", "CAACAgIAAxkBAAEI38JkVjEGvJJ1uy2ZgKr0WZ1669Tr9AACYBgAAgJY8Us7jaZxQbuf-i8E",
                "CAACAgIAAxkBAAEI38RkVjEKIpzkDQZ8Rg3xq_i1N1UqnwACTBsAAore-EsrFNRjHNpPoS8E", "CAACAgIAAxkBAAEI38ZkVjEMFknmnpleXMJ1eDekk-aIIgAC_BwAAlHKAUikkf5LBxHrpi8E"]
    if message.text.lower() == "мяу" or message.text.lower() == "мур":
        bot.send_sticker(message.chat.id, random.choice(stickers))

bot.infinity_polling()