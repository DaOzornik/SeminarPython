"""Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6"""

x = int(input('Введите число: '))
n1 = 0 # 0 1 1 2 3 5 8 13
n2 = 1
s = 1
while n2 < x:
    n1, n2 = n2, n2+n1
# tmp=n2+n1 #1---2---3
# n1=n2 #1---1---2
# n2=tmp #1---2---3
    s += 1 # 1---2---3
# print(n1)
# print(n2)
#print(n2)
if n2 == x:
   print(s)
else:
   print(-1)

