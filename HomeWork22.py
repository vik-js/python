# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n_1 = int(input("Введите количество элементов 1-го множества: "))
data_list_1 = [int(i) for i in input(
    f'Введите {n_1} элементов 1-го множества через пробел: ').split()]
if len(data_list_1) != n_1:
    exit(f'Необходимо ввести {n_1} элемента(ов)!')
m_1 = int(input('Введите количество элементов 2-го множества: '))
data_list_2 = [int(j) for j in input(
    f'Введите {m_1} элементов 2-го множества через пробел: ').split()]
if len(data_list_2) != m_1:
    exit(f'Необходимо ввести {m_1} элемента(ов)!')

data_1 = set(data_list_1)
data_2 = set(data_list_2)

similar_elements = sorted(data_1.intersection(data_2))

print('Числа, которые встречаются в обоих множествах: ', end='')
print(*similar_elements)
