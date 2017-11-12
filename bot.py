import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp="/КатяКолосова")
def handle_message(message):
    chat_id=message.chat.id
    mess=bot.send_message(chat_id,"Привет,Кать.Хочешь я тебе кое-что скажу?")
    bot.register_next_step_handler(mess, HelloKatya)

def HelloKatya(message):
    if message.text == "Да":
        bot.send_message(message.chat.id,'Я тебя немножечко люблю:)')
    else:
        bot.send_message(
            message.chat.id,
            'Ну..Ладно, пока')

if __name__ == '__main__':
    bot.polling(none_stop=True)
