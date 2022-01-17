def number_to_string():
    """Программа принимает число и печатает его прописью"""
    dict_units = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
                  6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    dict_first_ten = {0: 'десять', 1: 'одиннадцать', 2: 'двенадцать', 3: 'тринадцать',
                      4: 'четырнадцать', 5: 'пятнадцать', 6: 'шестнадцать', 7: 'семнадцать',
                      8: 'восемнадцать', 9:'девятнадцать'}
    dict_tens = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
                 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}

    x = int(input('put number here: '))

    if x < 10:
        return dict_units.get(x)
    elif 9 < x < 20:
        return dict_first_ten.get(int(x%10))
    else:
        if x % 10 == 0:
            return f'{dict_tens.get(int(x/10))}'
        else:
            return f'{dict_tens.get(int(x/10))} {dict_units.get(x % 10)}'

#print(number_to_string())
# for x in range(20, 40):
#     print(x, number_to_string(x))
