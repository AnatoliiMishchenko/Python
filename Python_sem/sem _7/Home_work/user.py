from os import path

import convert
import write


def adres_name():
    return input("Введите имя файла с расширением txt, csv ")


def user_info():
    count = int(input(" Введите количество человек справочинка "))
    data = []
    while count > 0:
        f = input("Введите фамилию ")
        N = input("Введите Имя ")
        o = input("Введите Отчество ")
        t = input("Введите телефон ")
        op = input("Введите описание ")
        data.append(f"{f} {N} {o} {t} {op}\n")
        count -= 1
    return data


def tur():
    txt = """Введите для конвертации из txt в csv - 1 
    для конвертации из csv в txt - 2"""
    print(txt)
    choice = input("Ввод: ")
    if choice == "1":
        name = adres_name()
        if path.exists(name):
            convert.txt_in_csv(name)
        else:
            print("Файла с таким именем нет")
    elif choice == "2":
        name = adres_name()
        if path.exists(name):
            convert.csv_in_txt(name)
        else:
            print("Файла с таким именем нет")
    else:
        print("Некорректный ввод")


def write_or():
    txt = """Введите для записи в файл - 1
    для конвертации файла - 2"""
    print(txt)
    choice = input("Ввод: ")
    if choice == "1":
        write.writer_fail(user_info(), adres_name())
    elif choice == "2":
        tur()
    else:
        print("Некорректный ввод")
