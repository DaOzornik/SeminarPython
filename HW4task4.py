# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
def createDict():
     equation ={}
     degree = int(input('Задайте натуральную степень многочлена k: '))


     for i in range(degree, -1, -1):
        equation[i] = random.randint(-100,100)
     return equation

equation = createDict()

strEquation = ''

for k,v in equation.items():
    if v>0:
        strEquation += f' + {v}*x^{k}'
    elif v<0:
        strEquation += f' - {abs(v)}*x^{k}'


print(strEquation)    



