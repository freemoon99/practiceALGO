import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))  # 내구도
robot = deque([0]*n) # n까지만 로봇들이 올라갈 수 있으므로 n개만 생성
cnt = 0

# 내구도가 0인 칸의 개수가 k개 이상이면 종료
def isFinishsed():
  return a.count(0) >= k

while True:
  # 종료 조건
  if isFinishsed():
    break
  
  # 1. 벨트, 로봇 회전하고 내리기
  a.rotate(1)
  robot.rotate(1)
  robot[-1] = 0
  
  # 2. 이동
  if 1 in robot:  # 로봇이 존재 한다면
    for i in range(n-2, -1, -1):  # n과 가까운 것이 먼저 올라간 것
      if robot[i] == 1 and robot[i+1] == 0: # 현재 로봇이 존재하고, 다음 칸에 로봇이 없다면
        if a[i+1] >= 1:  # 만약 내구도가 1 이상 이라면 
          robot[i+1] = 1  # 다음칸으로 이동
          robot[i] = 0  # 현재 칸은 비움
          a[i+1] -= 1
    # 로봇 내리는 곳에 있다면 내리기
    robot[-1] = 0
  
  # 3. 로봇 올리기
  if robot[0] == 0 and a[0] > 0:
    robot[0] = 1  # 로봇 올리기
    a[0] -= 1 # 내구도 -1
  cnt += 1

print(cnt)