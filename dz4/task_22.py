# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

cnt_elems = input(
    'Введите через пробел кол-во элементов первого и второго множеств: '
)
lst_cnt_elems = cnt_elems.split()
set_1 = set()
set_2 = set()
for i in range(len(lst_cnt_elems)):
    for j in range(1, int(lst_cnt_elems[i]) + 2):
        if i == 0:
            if j <= int(lst_cnt_elems[i]):
                set_1.add(int(input('Введите число: ')))
            if j > int(lst_cnt_elems[i]):
                print(
                    f'Ввод чисел первого множества окончен\n'
                    f'Состав первого множества: {set_1}'
                )
        else:
            if j <= int(lst_cnt_elems[i]):
                set_2.add(int(input('Введите число: ')))
            if j > int(lst_cnt_elems[i]):
                print(
                    f'Ввод чисел второго множества окончен\n'
                    f'Состав второго множества: { set_2}'
                )
lst = list(set_1.intersection(set_2))
lst.sort()
print(f'Общие элементы двух множеств: ', end=" ")
for i in lst:
    print(i, end=" ")






