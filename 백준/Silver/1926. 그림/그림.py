import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(graph, a, b):
  q = deque()
  q.append((a, b))
  graph[a][b] = 0
  cnt = 1
  
  while q:
    x ,y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx, ny))
        cnt += 1
      elif graph[nx][ny] == 0:
        continue
  return cnt

ans = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      ans.append(bfs(graph, i, j))

if not ans:
  print(len(ans))
  print(0)
else:
  print(len(ans))
  print(max(ans))