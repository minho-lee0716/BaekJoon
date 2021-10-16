m = int(input().split(' ')[1])
c = list(map(int, input().split(' ')))
for _ in range(m):
    c.sort()
    c[0]=c[1]=c[0]+c[1]
print(sum(c))
