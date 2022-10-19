def txt_in_csv(adres):
    with open(f"{adres.replace('.txt', '')}.csv", "w") as w_file, \
            open(f"{adres}", "r") as r_file:
        for i in r_file:
            w_file.write(";".join(i.split(" ")))


def csv_in_txt(address):
    with open(f"{address.replace('.csv', '')}.txt", "w") as w_file, \
            open(f"{address}", "r") as r_file:
        for i in r_file:
            w_file.write(" ".join(i.split("\n")))