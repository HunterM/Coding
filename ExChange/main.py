import telebot 
import config
import requests

bot = telebot.TeleBot(config.TOKEN)

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

USD = f"{data['Valute']['USD']['Value']}, {data['Valute']['USD']['Name']}"
EUR = f"{data['Valute']['EUR']['Value']}, {data['Valute']['EUR']['Name']}"
CNY = f"{data['Valute']['CNY']['Value']}, {data['Valute']['CNY']['Name']}"


@bot.message_handler(content_types=['text']) 
def start(message):
        if message.text == '/start':
                markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.row('€', '$', 'Y')
                msg = bot.send_message(message.chat.id, 'Выберите валюту', reply_markup=markup)
                bot.register_next_step_handler(msg, currency)

def currency(message):
        if message.text == '€':
                msg = bot.send_message(message.chat.id, 'Вы выбрали евро') 
                bot.send_message(message.chat.id, EUR)
                bot.send_message(message.chat.id, 'Введите /start для повтора операции')
        elif message.text == '$':
                msg = bot.send_message(message.chat.id, 'Вы выбрали доллары')
                bot.send_message(message.chat.id, USD)
                bot.send_message(message.chat.id, 'Введите /start для повтора операции')
        elif message.text == 'Y':
                msg = bot.send_message(message.chat.id, 'Вы выбрали юани')
                bot.send_message(message.chat.id, CNY)
                bot.send_message(message.chat.id, 'Введите /start для повтора операции')
        
        else:
                msg = bot.send_message(message.chat.id, 'Введите корректные данные')
                bot.register_next_step_handler(msg, currency)

bot.polling()
       

