# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
list_1 = [i for i in range(1, n+1)]
print(*list_1)
k = int(input("Введите число, которое будем искать в массиве: "))

mod = abs(k - list_1[0])
num = list_1[0]
for i in range(1, len(list_1)):
    if mod > abs(list_1[i] - k):
        mod = abs(list_1[i] - k)
        num = list_1[i]
print(num)
