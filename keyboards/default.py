'''
SIZ BU YERDA ODDIY KNOPKALAR YARATA OLASIZ
'''

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    catalog = KeyboardButton("Katalog 📇")
    feedback = KeyboardButton("Bog'lanish ☎")
    settings = KeyboardButton("Sozlamalar 🛠")
    markup.add(catalog, feedback, settings)
    return markup

def registration():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    register = KeyboardButton("Ro'yxatdan o'tish 📝")
    markup.add(register)
    return markup

def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    contact = KeyboardButton("Kontaktni ulashish", request_contact=True)
    markup.add(contact)
    return markup