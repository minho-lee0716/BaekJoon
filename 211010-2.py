result = 99
num = int(input())
if num <= 99:
    print(num)
else:
    for i in range(100, num+1):
        if (lambda l : True if l[2]-l[1] == l[1]-l[0] else False)([int(l) for l in str(i)]):
            result += 1
    print(result)
