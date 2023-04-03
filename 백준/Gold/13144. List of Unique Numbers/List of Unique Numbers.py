N = int(input())
num = list(map(int, input().split()))

res = 0
start, end = 0, 0
check = [False]*100001

while start != N and end != N:
    if not check[num[end]]:
        check[num[end]] = True
        end += 1
        res += end - start
    else:
        while check[num[end]]:
            check[num[start]] = False
            start += 1

print(res)
