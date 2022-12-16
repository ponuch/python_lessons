import telebot

bot = telebot.TeleBot("5930237493:AAGP1vVDmK99cMmbnLAr_omvwtPcx6jlA6o", parse_mode=None)

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['answer'])    
def answer(message):
    with open(f'F:\Projects\Geek_brains\Python_Prog\python_lessons\{message.from_user.id}.txt', 'r+', encoding='utf-8') as data:
        questions = data.readlines()
        for q in questions:
            reply = f'Dear {message.from_user.first_name}, your question was {q}, sorry, but we dont know what to say' 
            bot.reply_to(message, reply)
            
            

@bot.message_handler(func=lambda m: True)    
def echo_all(message):
    with open(f'F:\Projects\Geek_brains\Python_Prog\python_lessons\{message.from_user.id}.txt', 'a+', encoding='utf-8') as data:
        data.writelines(message.text + "\n")
 
 
bot.infinity_polling()