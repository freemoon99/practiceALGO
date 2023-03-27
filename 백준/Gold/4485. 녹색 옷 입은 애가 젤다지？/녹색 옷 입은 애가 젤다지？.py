import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 몇번째인지 카운트 하기 위함
cnt = 1
# 다익스트라 이용
def dijkstra():
  q=[]
  heapq.heappush(q, (graph[0][0], 0, 0))
  distance[0][0] = 0
  
  while q:
    cost, x, y = heapq.heappop(q)
    
    if x == N-1 and y == N-1:
      print("Problem ",cnt,": ",distance[x][y], sep="")
      break
    # 상하좌우 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        _cost = cost + graph[nx][ny]
        if _cost < distance[nx][ny]:
          distance[nx][ny] = _cost
          heapq.heappush(q, (_cost, nx, ny))

while True:
  N = int(input())
  # 0이 들어 오면 종료 해야함
  if N == 0:
    break
  # 테스트 케이스(그래프)
  graph = [list(map(int, input().split())) for _ in range(N)]
  distance = [[INF] * N for _ in range(N)]
  
  dijkstra()
  cnt += 1
