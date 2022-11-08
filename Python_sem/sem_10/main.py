import exceptions
import rational
import complex as c
import logger as l

from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

MAIN_MENU, RAT_MENU, FOR_SQRT, FIRST, SECOND = range(5)
COMPLEX_MENU, VALID_1, IMAGINARY_1, VALID_2, IMAGINARY_2 = range(5, 10)
choice = None
num_1 = None
valid_1 = None
imaginary_1 = None
valid_2 = None


def menu_m(update, _):
    txt = '''Введите
            для работы с рациональными числами: 1
            для работы с комплексными числами: 2
            для выхода: q'''
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")


def menu_r(update, _):
    txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для деления с остатком: 5
        для деления нацело: 6
        для возведения в степень: 7
        для извлечения из квадратного корня: 8
        для выхода: q
        для возврата в предыдущее меню: r"""
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")


def menu_c(update, _):
    txt = """Введите
        для сложения: 1
        для вычитания: 2
        для умножения: 3
        для обычного деления: 4
        для выхода: q
        для возврата в предыдущее меню: r"""
    update.message.reply_text(txt)
    update.message.reply_text("Ввод: ")


def start(update, _):
    update.message.reply_text("Привет. Это калькулятор.")
    menu_m(update, _)
    return MAIN_MENU


def main_menu(update, _):
    main_choice = update.message.text
    if main_choice == '1':
        menu_r(update, _)
        return RAT_MENU
    elif main_choice == '2':
        menu_c(update, _)
        return COMPLEX_MENU
    elif exceptions.check_exit(main_choice):
        update.message.reply_text("Вышел")
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\nПопробуйте еще раз")
        menu_m(update, _)
        return MAIN_MENU


def rat_menu(update, _):
    global choice
    choice = update.message.text
    if choice == "8":
        update.message.reply_text('Введите число: ')
        return FOR_SQRT
    elif choice in ['1', '2', '3', '4', '5', '6', '7']:
        update.message.reply_text('Введите первое число: ')
        return FIRST
    elif exceptions.check_back(choice):
        menu_m(update, _)
        return MAIN_MENU
    elif exceptions.check_exit(choice):
        update.message.reply_text("Вышел")
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\nПопробуйте еще раз")
        menu_r(update, _)
        return RAT_MENU


def for_sqrt(update, _):
    num = update.message.text
    if exceptions.check_num(num):
        rational.init(eval(num), 0)
        res = rational.do_it(choice)
        update.message.reply_text(f"Результат: {res}")
        l.log(num, 0, res, choice)
        update.message.reply_text("Конец")
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\n")
        return FOR_SQRT


def first(update, _):
    global num_1
    num_1 = update.message.text
    update.message.reply_text('Введите второе число: ')
    return SECOND


def second(update, _):
    global num_1
    num_2 = update.message.text
    if exceptions.check_num(num_1) and exceptions.check_num(num_2):
        if choice in ['4', '5', '6'] and num_2 == '0':
            update.message.reply_text("На 0 делить нельзя\nПопробуйте еще раз")
            update.message.reply_text('Введите первое число: ')
            return FIRST
        else:
            num_1, num_2 = eval(num_1), eval(num_2)
            rational.init(num_1, num_2)
            res = rational.do_it(choice)
            update.message.reply_text(f"Результат: {res}\n")
            l.log(num_1, num_2, res, choice)
            update.message.reply_text("Конец")
            return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\n")
        update.message.reply_text('Введите первое число: ')
        return FIRST


def complex_menu(update, _):
    global choice
    choice = update.message.text
    if exceptions.check_comp(choice):
        update.message.reply_text('Введите действительную часть первого числа: ')
        return VALID_1
    elif exceptions.check_back(choice):
        menu_m(update, _)
        return MAIN_MENU
    elif exceptions.check_exit(choice):
        update.message.reply_text("Вышел")
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\nПопробуйте еще раз")
        menu_c(update, _)
        return COMPLEX_MENU


def valid_first(update, _):
    global valid_1
    valid_1 = update.message.text
    update.message.reply_text('Введите мнимую часть первого числа: ')
    return IMAGINARY_1


def imaginary_first(update, _):
    global imaginary_1
    imaginary_1 = update.message.text
    update.message.reply_text('Введите действительную часть второго числа: ')
    return VALID_2


def valid_second(update, _):
    global valid_2
    valid_2 = update.message.text
    update.message.reply_text('Введите мнимую часть второго числа: ')
    return IMAGINARY_2


def imaginary_second(update, _):
    global imaginary_1, valid_1, valid_2
    imaginary_2 = update.message.text
    if exceptions.check_num(valid_1) and exceptions.check_num(imaginary_1) and \
            exceptions.check_num(valid_2) and exceptions.check_num(imaginary_2):
        c.init_x(eval(valid_1), eval(imaginary_1))
        c.init_y(eval(valid_2), eval(imaginary_2))
        res = c.do_it(choice)
        update.message.reply_text(f"Результат: {res}\n")
        l.log(c.x, c.y, res, choice)
        update.message.reply_text("Конец")
        return ConversationHandler.END
    else:
        update.message.reply_text("Некорректный ввод\n")
        update.message.reply_text('Введите действительную часть первого числа: ')
        return VALID_1


def cancel(update, _):
    update.message.reply_text('Пока', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MAIN_MENU: [MessageHandler(Filters.text & ~Filters.command, main_menu)],
            RAT_MENU: [MessageHandler(Filters.text & ~Filters.command, rat_menu)],
            FOR_SQRT: [MessageHandler(Filters.text & ~Filters.command, for_sqrt)],
            FIRST: [MessageHandler(Filters.text & ~Filters.command, first)],
            SECOND: [MessageHandler(Filters.text & ~Filters.command, second)],
            COMPLEX_MENU: [MessageHandler(Filters.text & ~Filters.command, complex_menu)],
            VALID_1: [MessageHandler(Filters.text & ~Filters.command, valid_first)],
            IMAGINARY_1: [MessageHandler(Filters.text & ~Filters.command, imaginary_first)],
            VALID_2: [MessageHandler(Filters.text & ~Filters.command, valid_second)],
            IMAGINARY_2: [MessageHandler(Filters.text & ~Filters.command, imaginary_second)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()