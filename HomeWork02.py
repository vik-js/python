# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Введте 3-х значное число:")
num = int(input())
digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10
sum = digit_1 + digit_2 + digit_3
print(num, '->', sum, '(',digit_1, '+', digit_2, '+', digit_3,')')