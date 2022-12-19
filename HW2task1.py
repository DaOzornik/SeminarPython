# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num= float(input('Введите число: '))
while num != int(num):
    num *= 10
count=0
while num>0:
    count+= num %10
    num//= 10
    sum= count+num
print(sum)



