
# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

d = int(input("Укажите какое количество знаков после запятой будет иметь число Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')