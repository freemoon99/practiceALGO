import heapq
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, t = map(int, input().split())
  graph[a].append((b, t))

def dijkstra(start):
  q=[]
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    # 가장 최단 거리가 짧은 노드 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 처리 된 적이 있는 노드라면 pass
    if distance[now]<dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인(i[0]=인덱스, i[1]=비용)
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q, (cost, i[0]))
  return distance

result = [[]]
time_list = []

for i in range(1, N+1):
  distance = [INF]*(N+1)
  result.append(dijkstra(i))
  
for i in range(1, N+1):
  time_list.append(result[i][X] + result[X][i])
  
print(max(time_list))