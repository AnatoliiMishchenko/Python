x = 0
y = 0


def init_x(a, b):
    global x
    x = complex(a, b)


def init_y(a, b):
    global y
    y = complex(a, b)


def sum():
    return x+y


def dif():
    return x-y


def mul():
    return x*y


def div():
    return x/y


def do_it(operator):
    match operator:
        case "1": return sum()
        case "2": return dif()
        case "3": return mul()
        case "4": return div()