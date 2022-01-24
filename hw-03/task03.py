import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', type=float, nargs='+', action='store')
parser.add_argument('-x', type=float, nargs='?', action='store')
parser.add_argument('-v', '--verbose', action='store_true')

poly = parser.parse_args()


def polynom():
    coef = poly.a
    x = poly.x
    v = poly.verbose
    answer = 0
    n = len(coef)
    out_st = []

    for _ in range(n):
        answer += (coef[_] * x**(n-1))
        out_st.append([coef[_], x**(n-1)])
        n -= 1
    #print(out_st)
    #print(out_st[0][0], out_st[0][1])

    if v:
        return "+".join(f"{out_st[a][0]}*{out_st[a][1]}" for a in range(len(coef))) + f"={answer}"

    else:
        return answer


print(polynom())
