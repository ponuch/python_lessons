import telebot

bot = telebot.TeleBot("5930237493:AAGP1vVDmK99cMmbnLAr_omvwtPcx6jlA6o", parse_mode=None)

@bot.message_handler(commands=['start', 'help', "hello"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)    
def echo_all(message):
    with open('F:\Projects\Geek_brains\Python_Prog\python_lessons\messages.txt', 'a+', encoding='utf-8') as data:
        data.writelines(message.text + "\n")
 
 
bot.infinity_polling()