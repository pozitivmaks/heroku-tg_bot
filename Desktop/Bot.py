import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	stic = open('C:/Users/Adm1/Desktop/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, stic)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton("🎲 Случайное число")
	item2 = types.KeyboardButton("😃 Как дела?")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> , бот создан чтобы быть подопытним кроликом.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def  lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Случайное число':
			bot.send_message(message.chat.id, str(random.randint(0, 100)))
		elif message.text == '😃 Как дела?':
			bot.send_message(message.chat.id, 'Отлично')

			markup = types.InlineKeyboardMarkup(row_width=2)

			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Так себе", callback_data='norm')
			item3 = types.InlineKeyboardButton("Плохо", callback_data='bad')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Сам как?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю как на такое ответить')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Это радует! 😆')
			elif call.data == 'norm':
				bot.send_message(call.message.chat.id, 'Будет лучше! 🙄')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Обидно! 😥')

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😃 Как дела?",
				reply_markup=None)

	except Exception as e:
		print(repr(e))

bot.polling(none_stop = True)