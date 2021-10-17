#k = int(input().split(' ')[1])
#nums = [int(num) for num in input()]
#nums.sort()
#print(''.join(list(map(str, (nums[k:][::-1])))))

# a[temp:k] = ['-']*(k-temp)

delete, idx = int(input().split(' ')[1]), 0
nums = list(map(str, input()))
while cnt != 0:
    nums.index(max(nums[idx:delete+1]))

print(''.join(nums).replace('-',''))
