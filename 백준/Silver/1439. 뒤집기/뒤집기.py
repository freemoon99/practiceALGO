nums = list(input())
cnt = 0
temp = []
temp.append(nums[0])

for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        temp.append(nums[i])

ans = []
ans.append(temp.count('0'))
ans.append(temp.count('1'))

print(min(ans))