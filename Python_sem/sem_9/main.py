from telegram import ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
fld = list(range(1, 10))
x = chr(10060)
o = chr(11093)
count = 9
player = x
CHOICE = 0


def show_field(field):
    txt = ''
    for i in range(len(field)):
        if not i % 3:
            txt += f'\n{"-" * 25}\n'
        txt += f'{field[i]:^8}'
    txt += f"\n{'-' * 25}"
    return txt


def check_win(field, symb):
    if (field[0] == symb and field[1] == symb and field[2] == symb) or \
            (field[3] == symb and field[4] == symb and field[5] == symb) or \
            (field[6] == symb and field[7] == symb and field[8] == symb) or \
            (field[0] == symb and field[3] == symb and field[6] == symb) or \
            (field[1] == symb and field[4] == symb and field[7] == symb) or \
            (field[2] == symb and field[5] == symb and field[8] == symb) or \
            (field[0] == symb and field[4] == symb and field[8] == symb) or \
            (field[2] == symb and field[4] == symb and field[6] == symb):
        return True
    return False


# функция обратного вызова точки входа в разговор
def start(update, _):
    global fld, player, count
    fld = list(range(1, 10))
    count = 9
    player = x
    update.message.reply_text("Привет, давай сыграем в крестики-нолики")
    update.message.reply_text(show_field(fld))
    update.message.reply_text(f'Первыми ходят {chr(10060)}')
    return CHOICE


def choice(update, _):
    global player, count
    move = update.message.text
    move = int(move)
    if move not in fld:
        update.message.reply_text(f"Некорректный ввод{chr(9940)}\nПопробуйте еще раз")
    else:
        fld.insert(fld.index(move), player)
        fld.remove(move)
        update.message.reply_text(show_field(fld))
        if check_win(fld, player):
            update.message.reply_text(f"{player} - ПОБЕДИТЕЛЬ{chr(127942)}{chr(127881)}")
            return ConversationHandler.END
        player = o if player == x else x
        count -= 1

    if count == 0:
        update.message.reply_text(f"Ничья {chr(129309)}")
        return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text('Пока', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater("YOUR TOKEN")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()