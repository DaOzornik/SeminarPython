#Реализуйте алгоритм перемешивания списка.

import random
num = int(input("Введите размер списка: "))
my_list = list(range(1, num+1))
print ("Ваш список : " + str(my_list))

random.shuffle(my_list)# встроенная функция по перетасовке списка
print ("Перемешанный список : " +  str(my_list))

exit()
# алгоритм перетасовки списка Фишера-Йейтса. Этот алгоритм просто принимает 
# более высокое значение индекса и заменяет его текущим значением, 
# этот процесс повторяется в цикле до конца списка.
for i in range(len(my_list)):
     
        j = random.randint(0, i + 1)  # выбор случайного индекса от 0 до i
        
my_list[i], my_list[j] = my_list[j], my_list[i]
     

print ("Перемешанный список : " +  str(my_list))
