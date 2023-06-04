from telebot import TeleBot

BOT_TOKEN = '6247691240:AAEYrbQue6I7H1zYTx8_z_bFOyslAC-2wlk'
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o boot do Vítor Braga!")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()