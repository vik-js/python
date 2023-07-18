# Задача 33: Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_balls(balls):
    min_number = min(balls)
    max_number = max(balls)
    for i in range(len(balls)):
        if balls[i] == max_number:
            balls[i] = min_number
    print(*balls)


grades = [int(i) for i in input("введите оценки: ").split()]
change_balls(grades)
