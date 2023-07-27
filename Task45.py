# Задача 45: Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

def find_sum_dividers(m):
    res = 0
    for i in range(1, int(m / 2) + 1):
        if m % i == 0:
            res += i
    res1 = 0
    for i in range(1, (res // 2) + 1):
        if res % i == 0:
            res1 += i
    if res1 == m and m != res:
        return m, res
    # for i in range(1, n // 2 ):
    #     if n % i == 0:
    #         res -= i
    # if res == 0:


#
# print(find_sum_dividers(220))
k = int(input("input number: "))
r = []
for i in range(1, k):
    a = find_sum_dividers(i)
    if a:
        if a[::-1] not in r:
            r.append(a)
for i in r:
    print(*i)


# def get_divisors(n):
#     divisors = [1]
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     return divisors


# def find_friendly_numbers(k):
#     friendly_numbers = []
#     for n in range(2, k + 1):
#         m = sum(get_divisors(n))
#         if m <= k and sum(get_divisors(m)) == n and m != n:
#             pair = (n, m) if n < m else (m, n)
#             if pair not in friendly_numbers:
#                 friendly_numbers.append(pair)
#     return friendly_numbers
