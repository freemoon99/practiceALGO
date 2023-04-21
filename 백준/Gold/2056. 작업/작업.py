import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
  info = list(map(int, input().split()))
  t[i] = info[0]
  if info[1] == 0:
    continue
  else:
    for j in info[2:]:
      graph[i].append(j)

for i in range(1, n+1):
  temp = 0
  for j in graph[i]:
    temp = max(temp, t[j])
  t[i] += temp
  
print(max(t))
