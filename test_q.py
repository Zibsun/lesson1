from telegram.ext import Updater

people = {
	"Коля" : {"city": "Москва", "temperature":-10, "wind":"Северный"},
	"Петя" : {"city": "Питер", "temperature":-13, "wind":"Восточный"},
	"Вася" : {"city": "Екат", "temperature":-5, "wind":"Западный"},
	"Оля" : {"city": "Париж", "temperature":7, "wind":"Южный"},
}

name = input ("Выбор имени ")

if name in people:
	print ("В городе %s температура %d, ветер %s" % (
		people[name]["city"], 
		people[name]["temperature"], 
		people[name]["wind"]))
else:
	print ("Такого у нас нет")
