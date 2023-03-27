import sys

input = sys.stdin.readline
N, X = map(int, input().split())
li = list(map(int, input().split()))
ans = []
for i in range(N):
    if li[i] < X:
        ans.append(str(li[i]))

print(' '.join(ans))