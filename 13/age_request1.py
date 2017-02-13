cr = 2017
name = str(input('Введите имя > '))
year = int(input('Введите год рождения >'))
age = cr - year
msg = "{0} {1}".format(str(name), str(age))

print(msg)
