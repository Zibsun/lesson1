from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)

greeting_text = "Что нового?"

dialog = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def main():
    updater = Updater("526728660:AAEctMCPi-coN2NZpXO0UfatdgWkcBcOzak")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
	update.message.reply_text(greeting_text)

def talk_to_me(bot, update):
    user_text = update.message.text.lower()
    reply = "Чо?"
    if user_text in dialog:
    	reply = dialog[user_text]

    update.message.reply_text(reply)

main()