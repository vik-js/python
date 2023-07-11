# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

hint_1_sum = int(input('Подсказка 1 - Сумма загаданных чисел равна: ')) 
hint_2_prod = int(input('Подсказка 2 - Произведение загаданных чисел равно: ')) 

d = hint_1_sum * hint_1_sum - 4 * hint_2_prod
if d < 0 or hint_1_sum == 0 or hint_2_prod == 0:
  exit("Введены НЕкорректные подсказки!")
elif d == 0:
  x, y = int(hint_1_sum / 2), int(hint_1_sum / 2)
elif d > 0:
  x, y = int((hint_1_sum + d ** 0.5) / 2), int((hint_1_sum - d ** 0.5) / 2)
if x + y == hint_1_sum and x * y == hint_2_prod:
  print(f"Задуманные числа: {x} и {y}")
else:
  print("Введены НЕкорректные подсказки!")