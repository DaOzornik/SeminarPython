# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


def new_lst():# Это функция, которая создаст список
    num= input('Введите элементы в массива: ').split()
    #print(num) #строковый массив
    for k in range(len(num)):
        num[k] = int(num[k])
    #print(num) # преобразование строкового массива в числовой   
    return(num)

lst_a = [3, 1, 3, 4, 2, 12]
lst_b = [4, 15, 43, 1, 15, 1]
def div_lst(lst_a, lst_b)
    lst_c = []
    for i in lst_a:
        if i not in lst_b:
            lst_c.append(i)
    return lst_c  
print(div_lst)
        



