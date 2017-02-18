num = int(input('Введите число > '))
def chek (num):

   for x in range(0,num*2):
       x += 2
       if x % 2 == 0:
           print(x)

chek(num)
