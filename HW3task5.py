# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


import os   
os.system("clear")# библиотека для очистки терминала
num= int(input('введите число: ')) 

fib1 = fib2 = 1
 
print(fib1, fib2, end=' ')
 
for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')


