x=0
y=0

def init(a,b):
    global x
    global y
    x=a
    y=b

def sum():
    return x+y

def div():
    return x/y

def iDiv():
    return x//y

def dif():
    return x-y

def mul():
    return x*y

def pow():
    return x**y

def sqrt():
    return x**0.5

def rDiv():
    return x%y

def do_it(operator):
    match operator:
        case "1": return sum()
        case "2": return dif()
        case "3": return mul()
        case "4": return div()
        case "5": return rDiv()
        case "6": return iDiv()
        case "7": return pow()
        case "8": return sqrt()