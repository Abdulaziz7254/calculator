import telebot
def if_true(message):
    i = 0
    nums = []
    while i<len(message.text.split()):
        try:
            nums.append(float(message.text.split()[i]))
        except:
            bot.send_message(message.chat.id, f"{message.text.split()[i]} не является цифрой ")
        i+=1
    return nums
bot = telebot.TeleBot('6339601851:AAHaDWRBYnbJK4GI5paOfGhp6IdoqdT-JrA')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте дорогой пользователь {message.chat.username}!')

@bot.message_handler(commands=['sum'])
def sum(message):
    bot.send_message(message.chat.id, 'Введите цифры через пробел которые вы хотите сложить')
    @bot.message_handler()
    def sum1(message):
        suma = 0
        num = if_true(message)
        for i in num:
            suma+=i
        bot.send_message(message.chat.id,suma)
@bot.message_handler(commands=['subtract'])
def subtract(message):
    bot.send_message(message.chat.id, 'Введите от чего хотите вычесть (a) и что хотите вычесть (b) ')
    @bot.message_handler()
    def subtract1(message):
        a , b  = if_true(message)
        bot.send_message(message.chat.id,a-b)
@bot.message_handler(commands=['degree'])
def degree(message):
    bot.send_message(message.chat.id, 'Введите какую цифру (a) хотите возвети в степень (b) ')
    @bot.message_handler()
    def degree1(message):
        a , b  = if_true(message)
        bot.send_message(message.chat.id,a**b)








bot.infinity_polling()