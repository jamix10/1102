num = int (input('Ведите число > '))
def is_prime(num):
    i = 2
    j = 0
    while i ** 2 <= num and j != 1:
        if num % i == 0:
            j = 1
        i += 1
    if j == 1:
        print("Это составное число")
    else:
        print("Это простое число")
is_prime(num)
