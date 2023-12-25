n = int(input())
lst = list(map(int, input().split()))
set_lst = sorted(set(lst))
dic = {}
answer = []

for i in range(len(set_lst)):
    dic[set_lst[i]] = i

for num in lst:
    answer.append(dic[num])

print(" ".join(map(str, answer)))