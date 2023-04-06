import sys
input = sys.stdin.readline

N = int(input())
ai = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if ai[i] > ai[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
_dp = max(dp)

res = []
for i in range(N-1, -1, -1):
    if dp[i] == _dp:
        res.append(ai[i])
        _dp -= 1
res.reverse()
for j in res:
    print(j, end=' ')
