import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a][b] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if li[j][i] and li[i][k]:
                li[j][k] = 1

ans = 0

for i in range(1, n+1):
    lower = 0
    upper = 0
    for j in range(1, n+1):
        if i == j:
            continue
        elif li[i][j] == 1: # 현재 구슬보다 가벼운 갯수 세기
            lower += 1
        elif li[j][i] == 1:# 현재 구슬 보다 무거운 갯수 세기
            upper += 1
    if upper > n//2 or lower > n//2: # 가볍거나 무거운 개수가 중간값 보다 많으면 될 수가 없다
        ans += 1
        
print(ans)