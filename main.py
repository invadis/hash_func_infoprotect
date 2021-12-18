import random
import math


def input_str():
    inp_str = str(input("Введите сообщение для шифрации: "))
    return inp_str

#функция перевода символов в код Unicode
def translate_unicode(inp_str):
    inp_str = list(inp_str)
    list_of_codes = []

    for i in inp_str:
        s = ord(i)
        list_of_codes.append(s)
    
    return list_of_codes

#функция перевода юникода в двоичный код
def codes_to_binary(list_of_codes):
    #перемножение чисел в массиве и добавление результата обратно к массиву 
    number = 1
    for x in list_of_codes:
        number *= x
    #number = int(''.join(map(str, list_of_codes)))
    list_of_codes.append(number)
    list_of_binaries = []

    for i in list_of_codes:
        bin_code = f'{i:b}'
        list_of_binaries.append(bin_code)

    for i, j in enumerate(list_of_binaries):
        list_of_binaries[i] = int(list_of_binaries[i])

    return list_of_binaries


def encryption(list_of_binaries):
    s = ''

    for i in list_of_binaries:
        s += str(i)

    s = list(s)
    len_list = len(s)
    #проверка на пустоту
    if len_list % 2 != 0:
        s.append('0')
    #делим список на 2 части
    print("s =", s)
    s1 = s[:int(len_list/2)]
    s2 = s[int(len_list/2):]
    print("s1=", s1, "s2=", s2)
    final_s = ''

    for i, j in zip(s1, s2):
        new_s = i + j
        final_s += str(int(new_s, 2))

    print("final:", final_s)

st = input_str()
list_of_codes = translate_unicode(st)
print(list_of_codes)
list_of_binaries = codes_to_binary(list_of_codes)
print(list_of_binaries)
encryption(list_of_binaries)
