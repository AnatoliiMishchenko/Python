def check_num(line):
    return True if line.isdigit() or line.replace(".", "", 1).isdigit() else False


def check_exit(line):
    return True if line == 'q' else False


def check_back(line):
    return True if line == 'r' else False


def check_comp(line):
    return True if line in ['1', '2', '3', '4'] else False