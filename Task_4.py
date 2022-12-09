# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

from random import randint

k = int(input('Введите натуральную степень k = '))
array = []

for i in range(k + 1):
    array.append(randint(0, 100))
result = []

for i in range(k,-1,-1):
    if array[i] != 0:
        if i == 0:
            result.append(f'{array[i]}')
        elif i == 1:
            result.append(f'{array[i]}*x')
        else:
            result.append(f'{array[i]}*x^{i}')

with open ('file.txt', 'w') as data:
    data.write(" + ".join(result) + " = 0")  