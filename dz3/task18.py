# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

n = int(input('Введите кол-во элементов в массиве: '))
x = 6
lst = list()
for i in range(n):
    num = int(input())
    lst.append(num)

min1 = abs(x - lst[0])
close_num = lst[0]
for i in lst[1:]:
    if min1 > abs(x - i):
        min1 = abs(x - i)
        close_num = i
print(close_num)

