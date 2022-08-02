import config
import telebot
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
chatId = 


@bot.message_handler(commands=["help"])
def start(message):
  bot.send_message(message.chat.id, 'Ты черт и гнида 😈')

#@bot.message_handler()    # Удаление перменной 1
#def filter_messages(message: types.Message):
#    if "1" in message.text:
#      message.delete()

#@bot.message_handler(content_types=['text'])
##def all_messages(message):
#    if '08' in message.text.lower():
#        bot.forward_message(chatId, message.chat.id, message.message_id)

#@bot.message_handler(content_types=['photo', 'document', 'audio', 'video']) #пересылка документов под переменной 100
#def all_media_messages(message):
#    if message.caption is not None and '100' in message.caption.lower():
#        bot.forward_message(chatId, message.chat.id, message.message_id)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привэт':
        bot.send_message(message.chat.id, 'Привет слейв')
   
    elif message.text.lower() == 'ку':
        bot.send_message(message.chat.id, 'kek')
    elif message.text.lower() == 'я не права':
        bot.send_message(message.chat.id, 'зато я прав!')
    elif message.text.lower() == 'ок':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFZX9i4nuSzFSxPcBMQzeFuWhX4ax7zQACGgMAAhM5jxFyf3SEG5i0tikE')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFZY1i4nyEDbJ19vIRwki3m-XHHV_HPwACgQ8AAk9tKgABwYJjM144lx4pBA')
    elif message.text.lower() == 'прости':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFZYFi4nugHHkrCcylUiyc19kHKwP6SgACEAMAAhM5jxHbLUYOzi7MBSkE')
    elif message.text.lower() == 'климсаныч':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFZYNi4nv-pqnjsGpvPPo-o_4v1XFPxwACSwQAAo-dWgW3ycMu1iIwbikE')
    elif message.text.lower() == 'гачи':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFZYVi4nwbZUOxBYaZAT9WcV-1KSRucQACmBEAAof42EvYtqA3NW0HqykE')
    elif message.text.lower() == 'вопрос':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFaNdi44a21-JjTLHTTYXeyi5wv44OSwACVAwAAk9tKgABUFn0LfDelYkpBA')
    if "Прием обращений к(запросы)\nЗаполнена на 0.1" in message.text:
       bot.forward_message(chatId, message.chat.id, message.message_id)



if __name__ == '__main__':
  bot.polling(none_stop = True)


