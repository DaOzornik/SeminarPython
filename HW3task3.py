#  Задайте список из вещественных чисел. 
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19




import os   
os.system("clear")

numbers = input('введите числа через пробел: ').split()
print(numbers)
numbers = list(map(float, numbers))
new_lst= [round (i % 1, 2) for i in numbers if i % 1 != 0]
print(max(new_lst) - min(new_lst))
