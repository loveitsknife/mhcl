 import telebot
API='6027105637:AAF8HrojiClgk6jcV5Ueb1pqyW3GIOgrm1g'
bot=telebot.TeleBot(API, parse_mode=None)
@bot.message_handler(commands=["start"])
def start(msg):

    bot.send_message(msg.from_user.id, 'Привет\nКак тебя зовут? ' )
    name = msg.text
    vivod1 = name + ", как дела ? "
    bot.send_message(msg.from_user.id, ' Сколько тебе лет ? ')
    age = msg.text
    vivod2 = age + ", это круто "
   # age=input( "Теперь укажи свой возраст " )
   # vivod1= name + ", как дела ? "
    #vivod2= age + ", это круто "
    bot.reply_to(msg, "" + vivod1 + vivod2 )
bot.polling()
