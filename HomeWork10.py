# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

coints_n = int(input('Введите число монеток, лежащих на столе: ')) 
n = [int(i) for i in input(f'Введите 1 и 0 через пробел {coints_n} раз(а): ').split()]
if len(n) > coints_n:
  exit(f"Необходимо вводить 1 и 0 только {coints_n} раз(а)!")
count = 0
for i in n:
  if i > 1:
    exit("Необходимо вводить только 1 или 0!")
  if i == 0:
    count += 1
print(f'Необходимо перевернуть {count} монеток(ки)')