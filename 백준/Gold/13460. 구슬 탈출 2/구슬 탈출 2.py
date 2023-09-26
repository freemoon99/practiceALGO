from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
# 4차원 배열(메모리 많이 잡아먹고, O(1)) 또는 set(동적 할당 가능하지만, 최악의 경우 O(N))으로 방문처리
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] 
# visited = set()

# 0, B, R의 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == "B":
            B = [i, j]
        elif graph[i][j] == "R":
            R = [i, j]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((B[0], B[1], R[0], R[1], 0))   # 파란 구슬, 빨간 구슬 좌표 , 움직인 수
  visited[B[0]][B[1]][R[0]][R[1]] = 1   # 방문 처리
  
  # 탐색
  while q:
    br, bc, rr, rc, cnt = q.popleft()
    
    if graph[rr][rc] == "O":  # 종료 조건[1] : 빨간 구슬이 탈출
      return print(cnt)

    if cnt >= 10:   # 종료 조건[2] : 움직임이 10 이상이라면 -1출력
      continue
    
    # 4방향 순회
    for i in range(4):
      r_move = 0
      b_move = 0

      # [1] 빨간색 순회
      nrr = rr + dr[i]
      nrc = rc + dc[i]
      # 벽 또는 구멍을 만나기 전까지 직진
      while True:
        if graph[nrr][nrc] == "#":  # 탈출 조건[1] : 벽일때 한칸 후진
            nrr -= dr[i]
            nrc -= dc[i]
            break
        if graph[nrr][nrc] == "O":   # 탈출 조건[2] : 구멍
            break
        nrr += dr[i]
        nrc += dc[i]
        r_move += 1

      # [2] 파란색 순회
      nbr = br + dr[i]
      nbc = bc + dc[i]
      # 벽 또는 구멍을 만나기 전까지 직진
      while True:
        if graph[nbr][nbc] == "#":  # 탈출 조건[1] : 벽일때 한칸 후진
            nbr -= dr[i]
            nbc -= dc[i]
            break
        if graph[nbr][nbc] == "O":   # 탈출 조건[2] : 구멍
            break
        nbr += dr[i]
        nbc += dc[i]
        b_move += 1

      # 만약 파란 공이 빠졌다면 다른 방향 시도
      if graph[nbr][nbc] == "O":
        continue
      
      # 두 구슬의 위치가 같을 경우, O의 위치가 아닐때
      if nrr == nbr and nrc == nbc:
        if r_move>b_move:
            nrr -= dr[i]
            nrc -= dc[i]
        else:
            nbr -= dr[i]
            nbc -= dc[i]
      
      # bfs 순회
      if visited[nbr][nbc][nrr][nrc] == 0:
        visited[nbr][nbc][nrr][nrc] = 1 # 방문 처리
        q.append((nbr, nbc, nrr, nrc, cnt+1))
    
  print(-1)
bfs()
