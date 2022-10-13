actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

s = "12 + ( 15 + 20 ) * 2 / 5 - 5 / 2"


def scob(line):
    my_list = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            m = line.index(')', i)
            my_list.append(line[i+1:m])
            i = m
        else:
            my_list.append(line[i])
        i += 1
    return my_list


print(scob(s.split()))


def in_scob(my_list):
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            a, b, c = scob(my_list[i])
            my_list[i] = actions[b](a, c)
    return my_list


print(in_scob(scob(s.split())))


def aref(my_list):
    ip = [i for i, j in enumerate(my_list) if j in "*/"]
    while ip:
        t = ip[0]
        a, b, c = my_list[t - 1: t + 2]
        my_list.insert(t-1, actions[b](a, c))
        del my_list[t: t + 3]
        ip = [i for i, j in enumerate(my_list) if j in "*/"]

    while len(my_list) > 1:
        a, b, c = my_list[:3]
        del my_list[: 3]
        my_list.insert(0, actions[b](a, c))

    return my_list


print(aref(in_scob(scob(s.split()))))
