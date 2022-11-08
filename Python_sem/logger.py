from datetime import datetime 


def word(action):
    if action == "1":
        return "сложение"
    elif action == "2":
        return "вычитание"
    elif action == "3":
        return "умножение"
    elif action == "4":
        return "обычное деление"
    elif action == "5":
        return "деление с остатком"
    elif action == "6":
        return "деление нацело"
    elif action == "7":
        return "возведение в степень"
    elif action == "8":
        return "извлечение квадратного корня"


def log(a, b, result, action):
    time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    if action == '8':
        with open('log.txt', 'a') as file:
            file.write(f'{time}: {a} {word(action)} {result}\n')
    else:
        with open('log.txt', 'a') as file:
            file.write(f'{time}: {a} {b} {word(action)} {result}\n')