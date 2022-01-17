def math_programm():
    """Программа принимает два числа
     и возвращает сумму, произведение и степень этих двух чисел"""
    x = int(input('put x number here: '))
    y = int(input('put y number here: '))
    sum_xy = x + y
    prod_xy = x * y
    pow_xy = x ** y
    return f'{sum_xy} {prod_xy} {pow_xy}'


print(math_programm())


def math_programm2(x, y):
    """Программа принимает два числа
     и возвращает сумму, произведение и степень этих двух чисел"""
    out_list = []
    sum_xy = x + y
    out_list.append(sum_xy)
    prod_xy = x * y
    out_list.append(prod_xy)
    pow_xy = x ** y
    out_list.append(pow_xy)
    return ' '.join([str(a) for a in out_list])


print(math_programm2(10, 7))
