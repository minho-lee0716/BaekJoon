# [ 약수 ]
# https://www.acmicpc.net/problem/1037

size, nums = int(input()), list(map(int, input().split(' ')))
print(max(nums) * min(nums))
