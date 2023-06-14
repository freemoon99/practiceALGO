import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 케이스를 분리해야함..
# 만약 현재 위치의 모양이 '-'이면 행으로 가로 
# => 2차원 배열에서 [x][y]이면 y값이 움직이면 좌우 이동 -> m이랑 연관
# 현재 위치의 모양이 '|'이면 열로 세로 
# => 2차원 배열에서 [x][y]이면 x값이 움직이면 상하 이동 -> n이랑 연관

def dfs(x, y):
  if graph[x][y] == '-':
    graph[x][y] = True
    for dy in [1, -1]:
      ny = y + dy
      if ny>0 and ny<m and graph[x][ny] == '-':
        dfs(x, ny)
        
  if graph[x][y] == '|':
    graph[x][y] = True
    for dx in [1, -1]:
      nx = x + dx
      if nx>0 and nx<n and graph[nx][y] == '|':
        dfs(nx, y)

ans = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == '-' or graph[i][j] == '|':
      dfs(i,j)
      ans += 1

print(ans)