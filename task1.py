# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

num = int(input('Введите число от 1 до 7: '))
if num >=1 and num <=5:
    print('working day')    
elif num==6 or num==7:
    print('day off')    
else:
    print('enter correct number')    

