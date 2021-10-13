a, b, res = input(), input(), 0
for idx, num in enumerate(b[::-1]):
    x = int(a)*int(num)
    print(x)
    res += x*(10**idx)
print(res)

#a = '123'
#print(a[::-1])
