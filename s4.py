# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

stroka = 'a a a b c a a d c d d'

def foo(stroka):
    list_1 = stroka.split()
    list_2 = []
    dct = {}
    for i in list_1:
        if i in dct:
            dct[i] += 1
            list_2.append(f'{i}_{str(dct[i])}')
        else:
            list_2.append(i)
            dct[i] = 0
    return ' '.join(list_2)

print(foo(stroka))