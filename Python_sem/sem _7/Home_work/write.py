


def writer_fail(data, adres):
    with open( f"{adres}","a") as fail:
        fail.write((" ".join(data)))
       