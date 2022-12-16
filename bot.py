import telebot
import codecs  
from controller import *

token = "5847204669:AAH5uVtX6Ryb4LqwSQcg2pVMoLi0Co_XXbU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Для поиска номера введите команду /find')

@bot.message_handler(commands=['find'])
def handle_text(message):
    cid = message.chat.id
    name = bot.send_message(cid, 'Введите имя для поиска:')
    bot.register_next_step_handler(name , step_Find_Name)

def step_Find_Name(message):
    cid = message.chat.id
    userFindName = message.text
    name_search(userFindName)
    with codecs.open('tmp_list', 'r', 'utf-8') as tmp_data:
        result = tmp_data.read()
    if result != '':
        bot.send_message(cid, result)
    else:
        bot.send_message(cid, 'Такого имени нет в вашей телефонной книге')

bot.polling()