# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Длина шоколадки (в дольках):')
number_n = int(input())
print('Ширина шоколадки (в дольках):')
number_m = int(input())
print('Желаемое количество долек:')
slice_number_k = int(input())

if (slice_number_k % number_n == 0 or slice_number_k % number_m == 0):
  print(f'{number_n} {number_m} {slice_number_k} -> yes')
else:
  print(f'{number_n} {number_m} {slice_number_k} -> no')
