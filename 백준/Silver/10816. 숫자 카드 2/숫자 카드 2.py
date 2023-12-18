from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
dic = defaultdict(int)

for i in nums:
    dic[i] += 1

m = int(input())
get = list(map(int, input().split()))
answer = []

for j in get:
    answer.append(dic[j])

print(' '.join(map(str, answer)))
