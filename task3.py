# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

first_num= int(input('введите координату Х: '))
second_num = int(input('введите координату У: '))

if first_num <0 and second_num >0:
    print('1 четверть')
elif first_num >0 and second_num >0:
        print('2 четверть')
elif first_num >0 and second_num <0:
            print('3 четверть')
elif first_num <0 and second_num <0:
                print('4 четверть')
else:
                print('ваша комбинация содержит 0, введите число не равное 0')




