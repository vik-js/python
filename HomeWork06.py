# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

print('Введите 6-ти значный номер билета:')
ticket_number = input()
if (len(ticket_number) == 6):
  digit_1 = int(ticket_number[0])
  digit_2 = int(ticket_number[1])
  digit_3 = int(ticket_number[2])
  digit_4 = int(ticket_number[3])
  digit_5 = int(ticket_number[4])
  digit_6 = int(ticket_number[5])
  if (digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6):
    print(f'{ticket_number} -> yes')
  else:
    print(f'{ticket_number} -> no')
else:
  print('Ошибка ввода')

# print('Введите 6-ти значный номер билета:')
# ticket_number = int(input())
# if (100000 <= ticket_number < 1000000):
#   digit_1 = int(ticket_number // 100000)
#   digit_2 = int(ticket_number // 10000 % 10)
#   digit_3 = int(ticket_number // 1000 % 10)
#   digit_4 = int(ticket_number // 100 % 10)
#   digit_5 = int(ticket_number // 10 % 10)
#   digit_6 = int(ticket_number % 10)
#   if (digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6):
#     print(f'{ticket_number} -> yes')
#   else:
#     print(f'{ticket_number} -> no')
# else:
#   print('Ошибка ввода')
