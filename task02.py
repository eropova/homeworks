def string_to_number():
    """Программа принимает на вход две строки с названиями цифр (ноль, один и т.д.)
     и выводит название их суммы"""

    x = input('put x number here: ')
    y = input('put y number here: ')

    dict_units = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5,
                  'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
                  'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14,
                  'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18,
                  'девятнадцать': 19}

    in_numbers = [dict_units.get(x), dict_units.get(y)]
    try:
        out_sum = sum(in_numbers)
        return list(dict_units.keys())[out_sum]
    except TypeError:
        print('нет такого числа, проверьте ввод')


print(string_to_number())