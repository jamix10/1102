a = float(input('Enter num 1 >'))
b = float(input('Enter num 2 >'))
operator = str(input('Enter operation  >'))

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def input_operator(operator, a, b):
    if operator == '+':
        print('{} + {} = {}'.format(a, b, plus(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, minus(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mult(a, b)))
    elif operator == '/':
        print('{} : {} = {}'.format(a, b, div(a, b)))
    else:
        print("НЕПРАВИЛЬНЫЙ ВВОД!")

input_operator(operator, a, b)
