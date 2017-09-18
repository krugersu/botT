# -*- coding: utf-8 -*-
import config
import telebot
import random
import data



bot = telebot.TeleBot(config.token)


# Обработчик команд '/start'  и '/help'.
@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    bot.reply_to(message, "3...2...1... Пуск!!!!!")


#  Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


# Handles all sent documents  and audio files
@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    tstr = random.choice(data.tpict)

    bot.reply_to(message, tstr)


# Handles all sent documents and audio files
@bot.message_handler(content_types=['sticker'])
def handle_docs_audio(message):
    tstr = random.choice(data.stic)
    bot.reply_to(message, tstr)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    # print(type(message.text))
    Strs = str(message.text)

    if finditemlistfrommessage(Strs, data.sisk) == 1:
        tstr = random.choice(data.sis)

    elif finditemlistfrommessage(Strs, data.work) == 1:
        tstr = random.choice(data.workmess)

    elif finditemlistfrommessage(Strs, data.want) == 1:
        tstr = random.choice(data.jel)

    elif finditemlistfrommessage(Strs, data.onec) == 1:
        tstr = random.choice(data.cstr)

    elif finditemlistfrommessage(Strs, data.privet) == 1:
        tstr = random.choice(data.privets)

    elif (Strs.find('стикер') != -1):
        tstr = random.choice(data.stic)

    elif (Strs.find('Кости') != -1) or (Strs.find('кости') != -1) or (Strs.find('Костя') != -1) or (
                Strs.find('костя') != -1):
        tstr = "Костя отдыхает!"
    else:
        tstr = random.choice(data.rzr)
        

    bot.send_message(message.chat.id,  tstr)
    #bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

def finditemlistfrommessage(tstr, tlist):
    for item in tlist:
        if tstr.find(item) != -1:
            return 1

    return 0


if __name__ == '__main__':
    bot.polling(none_stop=True)
