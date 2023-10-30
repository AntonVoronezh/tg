from datetime import datetime

import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA')
# Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)
date = datetime(year=2023, month=10, day=18, hour=00, minute=9)
bot.send_message('-1001802264924', 'text', timeout=100)