from collections import deque
n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]

for _ in range(k):
  r, c = map(int, input().split())
  # 사과(1)표시
  graph[r-1][c-1] = 1

L = int(input())
snake = deque([[0,0]])
direction = deque([[0,1],[1,0],[0,-1],[-1,0]])
time = dict() # 시간 저장

for _ in range(L):
  t,d = input().split()
  time[int(t)] = d

# 방향 전환
# 우 -> 하 -> 좌 -> 상 순으로 초기화
# rotate가 양수 -> 젤 뒷 숫자 가 맨 앞으로
# rotate가 음수 -> 젤 앞 숫자가 맨 뒤로
def turn(d):
  if d == 'D':  # 오른쪽, 시계방향
      direction.rotate(-1)  
  else: # 왼쪽, 반시계 방향
    direction.rotate(1) 

sec = 0

# 주어진 초 동안 진행
while True:
  sec += 1
  nr = snake[-1][0] + direction[0][0]
  nc = snake[-1][1] + direction[0][1]
  # 종료 조건(범위를 벗어났을 때, 자기 자신을 만났을 때)
  if not(0 <=nr < n and 0 <= nc < n) or ([nr, nc] in snake):
    break
  
  if graph[nr][nc] == 1:  # 다음칸에 사과가 있다면
    snake.append([nr,nc])
    graph[nr][nc] = 0
  else:
    snake.append([nr,nc])
    snake.popleft()

  # 시간이 지난 후에 방향 전환
  if sec in time:
    turn(time[sec])

print(sec)