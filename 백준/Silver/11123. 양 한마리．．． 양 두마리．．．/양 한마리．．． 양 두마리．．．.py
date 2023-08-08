import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

t = int(input())

def dfs(y, x):
  # 방문
  grid[y][x] = '.'
  # 상하좌우에 # 이 있는지 확인
  dx = [0, -1, 0, 1]
  dy = [-1, 0, 1, 0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0<=nx<w and 0<=ny<h:
      if grid[ny][nx] == '#':
        dfs(ny, nx)

for _ in range(t):
  h, w = map(int, input().split())
  grid = [list(input().rstrip()) for _ in range(h)]
  cnt = 0
  
  for i in range(h):
    for j in range(w):
      if grid[i][j] == '#':
        dfs(i, j)
        cnt += 1

  print(cnt)