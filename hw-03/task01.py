class PreconditionError(Exception):
    def __init__(self):
        self.message = f'Исключение: нарушение предусловия a!=0'


class ComplexRootError(Exception):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.message = f'Исключение: комплексные корни с аргументами: {self.a} {self.b} {self.c}'


def solve(a, b, c):
    try:
        sum_arg = 0
        for arg in (a, b, c):
            if isinstance(arg, (int, float)):
                sum_arg += 1
        if sum_arg == 3:
            if a != 0:
                discriminant = b ** 2 - 4 * a * c
                if discriminant == 0:
                    x = -b / (2 * a)
                    return x
                elif discriminant > 0:
                    x1 = (-b + discriminant ** 0.5) / (2 * a)
                    x2 = (-b - discriminant ** 0.5) / (2 * a)
                    return ' '.join([str(x) for x in sorted((x1, x2))])
                else:
                    raise ComplexRootError(a, b, c)
            else:
                raise PreconditionError
        else:
            raise TypeError

    except ComplexRootError as cre:
        return cre.message
    except PreconditionError as pe:
        return pe.message
    except TypeError:
        wrong_args = []
        for arg in (a, b, c):
            if not isinstance(arg, (int, float)):
                wrong_args.append((a, b, c).index(arg) + 1)
        if len(wrong_args) == 1:
            return f'Исключение: неправильные типы: {wrong_args[0]} аргумент'
        else:
            return 'Исключение: неправильные типы: ' + ', '.join([str(_) for _ in wrong_args]) + ' аргументы'


ins = [(1, 2, 1), (0.25, -2.5, 6), (1, 0, 1), (0, 1, -2), (1j, 2, 3), (1, "2", "3")]
for i in ins:
    print(solve(*i))
