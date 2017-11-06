# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(func=lambda message: True,content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'B:/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Saved that.")
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':

     bot.polling(none_stop=True)

