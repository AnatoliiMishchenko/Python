# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

import array
import random
Number = int(input("Введите количество кодируемых символов "))
path = 'C:/Users/Anatolii/Desktop/git_GB/Python/Python_sem/sem_5/text_words.txt'
path1 = 'C:/Users/Anatolii/Desktop/git_GB/Python/Python_sem/sem_5/text_code_words.txt'
path2 = 'C:/Users/Anatolii/Desktop/git_GB/Python/Python_sem/sem_5/text_decoder_words.txt'

def str_initial(n):
   with open(path, 'a', encoding="UTF-8") as t:
        size = 'avsDdFgPOiATWQP'
        for i in range(n):
            t.write(random.choice(size))


def srt_read():
    with open(path, 'r', encoding="UTF-8") as t:
        str = t.read()
        return str


str_initial(Number)
cod = srt_read()
print(f"Исходная строка: {cod}")


def srt_cod(cod):
    count = 1   
    for i in range(len(cod)-1):

        if cod[i] == cod[i+1]:
            count += 1

        else:
            with open(path1, 'a+', encoding="UTF-8") as r:
                r.write(f"{count}{cod[i]}")
                count = 1
    if (cod[len(cod)-2] != cod[-1]):
            with open(path1, 'a+', encoding="UTF-8") as r:
                r.write(f"{count}{cod[-1]}")


def read_str_cod():   
    with open(path1, 'r', encoding="UTF-8") as r:
        str = r.read()
    return str


srt_cod(cod)
new_str = read_str_cod()
print(f"Закодированная строка: {new_str}")


def str_decoder():  
    with open(path1, 'r', encoding="UTF-8") as w:
        str = w.read()
        count = 1
        for i in range(len(str)):
            if not str[i].isalpha():
                count = str[i]
            else:
                with open(path2, 'a+', encoding="UTF-8") as r:
                    for j in range(int(count)):
                        r.write(str[i])

def read_str_decoder():   
    with open(path2, 'r', encoding="UTF-8") as r:
        str = r.read()
    return str

str_decoder()
str_decoder_new =read_str_decoder()
print(f"Разкодированная строка: {str_decoder_new}")





