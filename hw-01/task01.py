x = int(input('Ввод:\n'))
y = int(input())

def math_programm():
    """Программа принимает два числа
     и возвращает сумму, произведение и степень этих двух чисел"""

    return f'Вывод:\n{x + y} {x * y} {x ** y}'


print(math_programm(x, y))
