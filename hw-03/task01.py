class PreconditionError(Exception):
    def __init__(self):
        pass


class ComplexRootError(Exception):
    def __init__(self):
        pass


def solve(a, b, c):
    try:
        if not isinstance((a, b, c), (int, float)):
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
                    raise ComplexRootError
            else:
                raise PreconditionError

        else:
            raise TypeError

    except ComplexRootError:
        return f'Исключение: комплексные корни с аргументами: {a} {b} {c}'

    except PreconditionError:
        return f'Исключение: нарушение предусловия a!=0'

    except TypeError:
        wrong_args = []
        for _i in (a, b, c):
            if not isinstance(_i, (int, float)):
                wrong_args.append((a, b, c).index(_i) + 1)
        if len(wrong_args) == 1:
            return f'Исключение: неправильные типы: {wrong_args[0]} аргумент'
        else:
            return 'Исключение: неправильные типы: ' + ', '.join([str(_i) for _i in wrong_args]) + ' аргументы'

ins = [(1, 2, 1), (0.25, -2.5, 6), (1, 0, 1), (0, 1, -2), (1j, 2, 3), (1, "2", "3")]
for i in ins:
    print(solve(*i))
