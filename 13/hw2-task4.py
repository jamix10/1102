#вывод символа звездочки по возрастанию до 10
x = 10
while x >= 0:
    print('*' * x)
    x -= 1
print('-' *10, '\n')
#вывод символа звездочки по убыванию от 10
y = 1
while y <= 10:
    print('*' * y)
    y += 1
print ('-' * 10, '\n')
#вывод символа звездочки в форме квадрата
z = 10
count = 1
while count <= 5:
    msg = '*' * z
    print(msg)
    count += 1
