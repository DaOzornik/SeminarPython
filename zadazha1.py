# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python
    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

first_num= int(input('введите первое число: '))
second_num= int(input('введите второе число: '))
max_num= max(first_num,second_num) #функция нахождения максимального числа из введенных чисел
for i in range(max_num, (first_num*second_num + max_num)):  # перебираем цикл с шагом на кратное число
    if i % first_num == 0 and i % second_num ==0:
        print(i)
        break




# Задача 2
# D = b2 − 4ac формула дискриминанта
# Если D < 0, корней нет;
# Если D = 0, есть ровно один корень;
# Если D > 0, корней будет два.

exit()
list_num = input('Введите значения коэффициентов a, b и z через пробел: ').split()
print(list_num)

a, b, z = list(map(int, list_num))  # переводим список строк в список чисел

d = b ** 2 - 4 * a * z

if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print(f'x_ = {x}', end=' ')
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    print(f'x1_ = {x1}', end=' ')
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x2_ = {x2}')


# Sympy библиотека для второго решения задачи
    
# Задача 1

exit()
numbers = input('введите числа через пробел: ').split()
print(numbers)
numbers = list(map(int, numbers))
print(max(numbers), min(numbers))
    











exit()
# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# Zadacha1
# import random # взяли из гугля
# n = int(input('Print your N: '))
# for i in range(n):
#     print(random.randint(0,10), end=' ')

#Zadacha2
# n = int(input('Print your N: '))
# my_dict ={}
# for i in range(1,n+1):
#     my_dict[i] = 3*i+1
# print(my_dict)


#Zadacha 3

# first_string = str(input('Ведите строку, в которой будем искать: '))
# second_string = str(input('Введите строку, корую ищем: '))
# first_string = 'овкукареку ку кук'
# second_string = 'ку'
# count = 0
# for i in range(len(first_string) - len(second_string)):
#     if first_string[i] == second_string[0]:
#         flag = True
#         for j in range(1, len(second_string)):
#             if second_string[j] != first_string[i+j]:
#                 flag = False
#         if flag:
#             count += 1
# print(count)

# Zadacha4

# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.



"""import time

current_time= time.time()
print(current_time)
random_num = int(99999*current_time)
print(random_num)
print(random_num%100)
print(str(random_num[-5:]))""" 


# Zadacha5
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


"""import os   # библиотека для очистки консоли
os.system("clear")


list = ['2', '3', '4', '5', '6']
num= input('введите число: ')
for i in list:
    if num == i:
        print(f' число {i} есть в списке')
        break
else:
        print('заданного числа нет в списке')"""



# Zadacha6

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(my_list)

string_find = "йцу"
count = 0
for i in range(len(my_list)):
    if string_find == my_list[i]:
        count+=1
        if count == 2:
            print(i)
            break
else:
    print(-1)

