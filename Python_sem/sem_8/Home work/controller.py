

import print_data
import push_data
import read_data
import search_data


def start():
    print("Здравствуйте!")
    while True:
        print("Что хотим сделать:\n\
        1 - получить всю информацию о учениках;\n\
        2 - добавить ученика;\n\
        3 - поиск ученика;\n\
        4 - выход.")
        ch = input("Введите цифру: ")
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")
            start()
        
        elif ch == '4':
            print("Сеанс окончен, до свидания!")
            break
        else:
            print("Введите корректную цифру!")
            start()
        
