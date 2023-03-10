# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Мое решение:
lst_num = [2, 3, 5]

res = list()
res.append(lst_num[0])

for i in range(lst_num[2] - 1):
    num = res[-1] + lst_num[1]
    res.append(num)

print(res)

# Эталонное решение:

a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a1 + i * d)