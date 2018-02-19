from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
 	level=logging.INFO,
	filename='bot.log'
	)


current_question_num = 0

greeting_text = """Добрый день, {}! Я чатбот-коуч. 
Я умею только задавать вопросы. У меня нет мозгов, но ничего страшного, у других коучей-людей их тоже нет!

Давай договоримся. Я буду задавать вопросы, а ты на них отвечать. 

НАЧИНАЕМ!

Кратко опиши мне свою ПРОБЛЕМУ"""

questions = ["Почему это важно для тебя?", 
"Что ты хочешь получить в итоге?", 
"В чем причины проблемы?", 
"Что ты предлагаешь предпринять, чтобы исправить проблему?", 
"Как много энергии ты готов вложить в это?", 
"Какие шаги нужно предпринять в ближайшие 72 часа?", 
"Когда ты начнешь?", 
"Скажи, что было для тебя ценным в нашем разговоре?"]

answers = []

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))    
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    replay_back_text = greeting_text.format(update.message.chat.first_name)
    current_question_num = 0

    logging.info ("Bot started")

    update.message.reply_text(replay_back_text)

def talk_to_me(bot, update):
    global current_question_num
    global answers

    question_num = len(questions)
    user_text = update.message.text 
    answers.append(user_text)

    if current_question_num + 1 <= question_num:
        #reply with question
        reply = questions[current_question_num]
        current_question_num += 1
    else:
        # we are at the end of conversation
        reply = get_report()
        current_question_num = 0
        answers = []

    print (reply)

    update.message.reply_text(reply)


def get_report():
    global questions
    global answers

    report = "ОТЧЕТ О НАШЕЙ С ТОБОЙ КОУЧ-СЕССИИ по проблеме:\n\n" + answers[0]  + "\n\n"

    for i, q in enumerate(questions):
        report += "*" + q + "*" + "\n\n — " + answers[i+1]  + "\n\n"
    
    report += "РАД, ЧТО СУМЕЛ ПОМОЧЬ!\n\n"
    report += "Если хочешь обсудить новую проблему, поспользуйся /start"

    return report
main()