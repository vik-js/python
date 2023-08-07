# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os

filename = "tell.txt"


def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s


def input_tel(s):
    first_name = input("Введите имя: ").capitalize()
    patronymic = input("Введите отчество: ").capitalize()
    last_name = input("Введите фамилию: ").capitalize()
    tel = input("Введите номер телефона: ")
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"{first_name} {patronymic} {last_name} {tel} \n")
    s.append([first_name, patronymic, last_name, tel])
    return s


def search_tel(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            return " ".join(line)
    return "Запись не найдена!"


def show_tel(s):
    for line in s:
        print(" ".join(line))


if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input(
            "\n1 - добавить данные\n2 - поиск\n3 - показать справочник\n4 - выход\n> ")
        if action == "1":
            s = input_tel(s)
        elif action == "2":
            search_name = input("Найти >>> ")
            print(search_tel(s, search_name))
        elif action == "3":
            show_tel(s)
        elif action == "4":
            break
        else:
            print("Некорректный ввод!")
