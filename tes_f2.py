def get_summ(one, two, delimeter=' ', case = "upper"):
    summ = (str(one) + str(delimeter) + str(two)).upper()
    return summ

print (get_summ("Vasya", "Petya", case = "low", delimeter = "+"))
