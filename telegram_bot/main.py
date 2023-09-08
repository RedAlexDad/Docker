import telebot

TG_BOT_TOKEN = '6487987515:AAEsFb-SdJVRq7e1mHOfqxrlakOEN9jLCJU'

# Создание бота
bot = telebot.TeleBot(TG_BOT_TOKEN)

HELP = '''
/help - Меню переключателя
/start - chatGPT
'''

# Справочник
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, f'''Hi! Telegram bot is working in docker! \n {HELP}''')

bot.polling(none_stop=True)