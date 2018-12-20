
import telebot



#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
bot = telebot.TeleBot('741179276:AAGkvKvXJecDMIYEnfU5k7n5tCGntSQDJAA')

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

    
       
