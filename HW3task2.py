# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os   
os.system("clear")# библиотека для очистки терминала
num= int(input('введите длину списка: ')) 
my_list= list(range(1, num+1))
print(f'Ваш список: ', my_list)
res = []
for i in range(0, len(my_list)):
    res.append(my_list[i] * my_list[len(my_list)-i-1])
  
print("произведение пар списка : " + str(res))

    