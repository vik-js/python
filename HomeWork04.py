# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print('Введите общее количество журавликов:')
amount = int(input())
if (amount > 0):
  num_p = int(amount / 3 / 2)
  num_s = int(num_p)
  num_k = int(amount / 3 * 2)
  print(f'{amount} -> {num_p} {num_k} {num_s}')
else:
  print('Ошибка ввода')