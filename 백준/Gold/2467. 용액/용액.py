value = 2000000000
N = int(input())
x, y = 0, 0
l = 0
r = N - 1

dragon_liquid = [int(x) for x in input().split()]
# 문제에서 이미 오름차순으로 정렬

while l < r:
    cur_value = dragon_liquid[l] + dragon_liquid[r]

    if abs(cur_value) <= value:
        x = dragon_liquid[l]
        y = dragon_liquid[r]
        value = abs(cur_value)

    if cur_value <= 0:
        l += 1

    else: # cur_value > 0
        r -= 1

print(x, y)