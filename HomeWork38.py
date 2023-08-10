# Задача 38: Дополнить телефонный справочник возможностью изменения
# и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

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


def edit_tel(s, object):
    with open(filename, "a", encoding="UTF-8") as f:
        edit_str = input("Введите новую информацию: ")
        for i, line in enumerate(s, 1):
            if object == i:
                line.clear()
                line.append(edit_str)
            open(filename, 'w').close()
            f.writelines(f'{" ".join(line)} \n')
    return s


def del_tel(s, object):
    with open(filename, "a", encoding="UTF-8") as f:
        for i, line in enumerate(s, 1):
            if object != i:
                open(filename, 'w').close()
                f.writelines(f'{" ".join(line)} \n')
    s.pop(object-1)
    return s


def search_tel(s, object):
    for i, line in enumerate(s, 1):
        if object in line or object.capitalize() in line or object == str(i):
            return " ".join(line)
    return "Запись не найдена!"


def show_tel(s):
    for i, line in enumerate(s, 1):
        print(i, " ".join(line))


if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input(
            "\n1 - добавить данные\n2 - изменить данные\n3 - удалить данные\n4 - поиск\n5 - показать справочник\n6 - выход\n> ")
        print()
        if action == "1":
            s = input_tel(s)
            print(f"Запись успешно добавлена!")
        elif action == "2":
            show_tel(s)
            edit_line = int(input("Какую запись изменить? >>> "))
            edit_tel(s, edit_line)
            print(f"Запись №{edit_line} успешно изменена!")
        elif action == "3":
            show_tel(s)
            del_line = int(input("Какую запись удалить? >>> "))
            del_tel(s, del_line)
            print(f"Запись №{del_line} успешно удалена!")
        elif action == "4":
            search_name = input("Найти >>> ")
            print(search_tel(s, search_name))
        elif action == "5":
            show_tel(s)
        elif action == "6":
            break
        else:
            print("Некорректный ввод!")
