import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))
V = int(input())
cnt = 0
for i in range(N):
    if li[i] == V:
        cnt += 1

print(cnt)