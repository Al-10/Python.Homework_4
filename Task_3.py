# Задача 3. 
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

string = input('Введите числа через запятую (без пробела): ')
new_str = string.split(',')

new_list = []
count = 0
for i in new_str:
    # print ('i:',i)
    for j in new_str:
        # print ('j:',j)
        if j == i:
            count += 1

    if count == 1:
        new_list.append(i)
        # print (count)
    count = 0
print(f'Неповторяющиеся элементы: {new_list}')