# [ 설탕 배달 - 브론즈1 ]
# https://www.acmicpc.net/problem/2839

sugar, n, fail = int(input()), 0, False
while sugar%5 != 0:
    sugar -= 3
    fail = True if sugar < 0 else False
    n += 1
print(-1 if fail else n + sugar//5)
