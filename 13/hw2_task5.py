# Объявление всех переменных
std_name = str(input('Введите имя >'))
num_lab = str(input('Введите номер работы >'))
num_gr = str(input('Введите номер группы >'))
lab = str('Лабораторная работа №')
gr = str('Выполнил студент гр. № ')
# Создание постоянных значений
line1 = lab + num_lab
line2 = gr + num_gr
line3 = std_name

width_frame = max(len(line1),len(line2),len(line3))

ls1 = (width_frame ) - (len(line1))
ls2 = (width_frame ) - (len(line2))
ls3 = (width_frame ) - (len(line3))

print('*' * (width_frame + 4))
print('*',line1,' ' * (ls1) ,'*')
print('*',line2,' ' * (ls2) ,'*')
print('*',line3,' ' * (ls3) ,'*')
print('*' * (width_frame + 4))

