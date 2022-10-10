# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect
import random
count = int(input('Number of words: '))
kit = "абв"




def text(count, kit):
    my_list = []
    for i in range(count):
        word = random.sample(kit, k=3)
        my_list.append("".join(word))
    str =" ".join(my_list)
    return str


t = text(count,kit)
print(t)

def new_text( str):    
    n_s = str.replace("абв","")
    return n_s

print(new_text(t))
    



# find_txt = "абв"
# # lst = [i for i in txt.split() if find_txt not in i]
# # print(f'Результат: {" ".join(lst)}')
# print(txt.replace(find_txt, ""))
