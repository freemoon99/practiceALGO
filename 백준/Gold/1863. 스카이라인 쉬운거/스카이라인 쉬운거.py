import sys
input = sys.stdin.readline

N = int(input())
godo = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    while godo and godo[-1] > y:
        ans += 1
        godo.pop()
    if godo and godo[-1] == y:
        continue
    godo.append(y)

while godo:
    if godo[-1] > 0:
        ans += 1
    godo.pop()

print(ans)
