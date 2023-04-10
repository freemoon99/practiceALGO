import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
maxNum = 0;

for i in range(n):
  for j in max(li):
    if j > maxNum:
      maxNum = j

def dfs(x, y, h):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < n and li[nx][ny] > h:
      if v[nx][ny] == False:
        v[nx][ny] = True
        dfs(nx, ny, h)

ans = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(maxNum):
  v = [[False]*n for _ in range(n)]
  cnt = 0
  
  for j in range(n):
    for k in range(n):
      if li[j][k] > i and v[j][k] == False:
        cnt += 1
        v[j][k] = True
        dfs(j, k, i)

  ans = max(ans, cnt)

print(ans)