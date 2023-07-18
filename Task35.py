# Задача 35: Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

import time


# def check(n, div = None):
#     if div is None:
#         div = n - 1
#     while div >= 2:
#         if n % div == 0:
#             print("Число не является простым")
#             return False
#         else:
#             return check(n, div-1)
#     else:
#         print("Число является простым")
#         return True


def check(n):
    if n < 4:
        print("yes")
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("No")
            return
    print("yes")


n = int(input("Введите число: "))
time1 = time.time()
check(n)
print(time.time()-time1)
