num_1 = int(input('Ввести число 1> '))
num_2 = int(input('Ввести число 2> '))
num_3 = int(input('Ввести число 3> '))

if num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        msg = num_1 + 5 + num_2 + 5 + num_3 + 5
        print(msg)
else:
    print('Нет равных чисел')
