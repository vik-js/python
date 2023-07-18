# Задача 25: Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

s = input('Напишите текст: ').split()
d = {}
res = []

for i in s:
    if i in d:
        res.append(f'{i}_{d[i]}')
    # print(f'{i}_{d[i]}', end=' ')
    else:
        res.append(i)
    d[i] = d.get(i, 0) + 1
print(''.join(res))
