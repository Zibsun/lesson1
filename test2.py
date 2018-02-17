print ("Задача 1")
names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
	print (i)
print ("---")

print ("Задача 2")
for i in names:
	print (i, len(i))
print ("---")


print ("Задача 3")
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

print ("---")
for i in names:
	gender = is_male[i] and "Мужской" or "Женский"
	print (i, gender)


print ("Задача 4")

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print ("Всего групп %d" % len(groups))

for i in groups:
	print ("В группе %d ученика" % len(i))
print ("---")

print ("Задача 5")


for i, g in enumerate(groups):
	print ("Группа %d:  %s" % (i, ", ".join(g)))

print ("---")
