N = int(input())
M = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N))
plan = list(map(int, input().split()))

# 경로 압축
def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parents[y] = x
  else:
    parents[x] = y

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      union(i, j)
      
ans = "YES"
for i in range(1, M):
  if parents[plan[i]-1] != parents[plan[0]-1]:
    ans = "NO"
    break
  
print(ans)