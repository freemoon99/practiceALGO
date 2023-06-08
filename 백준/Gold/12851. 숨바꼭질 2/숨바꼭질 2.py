import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

visited = [0] * 100001
visited[n] = 0

ans_cnt = 0
ans_way = 0

while q:
    x = q.popleft()
    count = visited[x]
    
    if x == k:
        ans_cnt = count
        ans_way += 1
        continue
    
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001:
            if visited[nx] == 0 or visited[nx] == visited[x]+1:
                q.append(nx)
                visited[nx] = count+1

print(ans_cnt)
print(ans_way)