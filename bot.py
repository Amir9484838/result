
import pytz
from datetime import datetime
import telebot
from telebot import types
import random
import logging
import requests
from time import sleep


#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
bot = telebot.TeleBot('741179276:AAGkvKvXJecDMIYEnfU5k7n5tCGntSQDJAA')



@bot.message_handler(commands=['send_message'])
def process_start(message):
    text = 'Отправить сообщение (репеем)'
    bot.send_message(message.chat.id, text)
    bot.send_message(468437664, "Был зарегестрирован первый шаг!")
    bot.register_next_step_handler(message, process_mind)

def process_mind(message):
    text = 'Сообщение было отправлено пользователю ' + str(message.reply_to_message.forward_from.first_name)
    #bot.send_message(message.reply_to_message.from_user.id, 'k')
    bot.forward_message(message.reply_to_message.forward_from.id, 468437664, message.message_id)
    bot.send_message(468437664, text)
    bot.send_message(468437664, message.reply_to_message.forward_from.id)




@bot.message_handler(commands=['id'])
def process_start(message):
	bot.send_message(message.chat.id, "Твой ID:" + str(message.user.id) ,parse_mode = 'HTML')
	bot.send_message(468437664, srt(message.from_user.first_name) + ' узнал свой ID')





@bot.message_handler(commands=["ping"])
def start(message):
	bot.send_message(message.chat.id, "<b>PONG!</b>", parse_mode="HTML")
	bot.send_message(468437664,'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /ping')
	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id,  'Привет,' + str(message.from_user.first_name) +'!\n' 'Напиши /help для просмотра возможностей бота.')
	bot.send_message(468437664,'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /start')

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'Этот бот создан для обратной связи с @amir_foreverornever. Для этого просто напишите сообщение, я его получу и отвечу. Дополнительные команды:\n\n/ping — проверяет работоспособность бота\n/id — показывает твой ID' )
	bot.send_message(468437664,'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /help')
	

@bot.message_handler(content_types=["text"])
def messages(message):
	if int(message.chat.id) == 468437664:
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		
		bot.forward_message(468437664, message.chat.id, message.message_id)
		bot.send_message(message.chat.id, str(message.from_user.first_name) + ',' +' я получил сообщение и очень скоро на него отвечу :)')






bot.send_message(468437664, 'Скрипт полностью запущен, бот функционирует!')
#bot.send_message(config.owner, 'Найдено администраторов бота: <b>2</b>', parse_mode='html')
#bot.send_message(config.owner, 'Администратор №1 - @amir_foreverornever', parse_mode='html')
#bot.send_message(config.owner, 'Worker <b>#1</b> был запущен!', parse_mode='html')
#bot.send_message(config.owner, 'Worker <b>#2</b> был запущен!', parse_mode='html')
#bot.send_message(config.owner, 'Worker <b>#3</b> был запущен!', parse_mode='html')
#bot.send_message(config.owner, 'Worker <b>#4</b> был запущен!', parse_mode='html')
#bot.send_message(config.owner, 'Worker <b>#5</b> был запущен!', parse_mode='html')
#bot.send_message(config.owner, 'Есть сообщения в очереди!', parse_mode='html')
#bot.send_message(config.owner, 'Сообщений в очереди:', parse_mode='html')
#bot.send_message(config.owner, random.randint(1,200))
#bot.send_message(config.owner, 'Вся служебная информация была доставлена администратору @amir_foreverornever!', parse_mode='html')


if __name__ == '__main__':
        bot.polling(none_stop = True)

    
       
