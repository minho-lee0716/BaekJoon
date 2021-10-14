x = input().split(' ')
print('==' if x[0] == x[1] else ('>' if int(x[0]) > int(x[1]) else '<'))
