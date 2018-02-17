def get_answer(question, answers):
	if question in answers:
		return answers[question].lower()
	else:
		return "Ты кто?"

a = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

while True:
	question = input ("> ").lower()
	if question == "спи":
		break
	else:
		print (get_answer(question, a))
