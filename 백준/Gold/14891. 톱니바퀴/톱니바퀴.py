import sys
from collections import deque

input = sys.stdin.readline
gear = [deque(list(map(int, input().rstrip()))) for _ in range(4)] 

k = int(input())
for _ in range(k):
    r = []  
    for i in range(4):
        r.append([gear[i][6], gear[i][2]])
    n, d = map(int, input().split())
    n = n - 1

    for i in range(n, 0, -1):
        if r[i][0] != r[i - 1][1]:
            if (n - (i - 1)) % 2 == 0:
                gear[i - 1].rotate(d)
            elif (n - (i - 1)) % 2 != 0:
                gear[i - 1].rotate(-1 * d)
        elif r[i][0] == r[i - 1][1]:
            break
    for i in range(n, 3):
        if r[i][1] != r[i + 1][0]:
            if (n - (i + 1)) % 2 == 0:
                gear[i + 1].rotate(d)
            elif (n - (i + 1)) % 2 != 0:
                gear[i + 1].rotate(-1 * d)
        elif r[i][1] == r[i + 1][0]:
            break
    gear[n].rotate(d)

res = sum(gear[i][0] * (2 ** i) for i in range(4))
print(res)