import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=float, nargs='+', action='store')
parser.add_argument('-x', type=float, nargs='?', action='store')
parser.add_argument('-v', '--verbose', action='store_true')

poly = parser.parse_args()

answer = 0
n = len(poly.a)
out_st = []

for i in range(n):
    answer += (poly.a[i] * poly.x**(n-1))
    out_st.append([poly.a[i], poly.x**(n-1)])
    n -= 1

if poly.verbose:
    print("+".join(f"{out_st[a][0]}*{out_st[a][1]}" for a in range(len(poly.a))) + f"={answer}")

else:
    print(answer)
