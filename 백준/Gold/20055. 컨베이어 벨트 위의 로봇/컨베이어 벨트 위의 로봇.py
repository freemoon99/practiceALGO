from collections import deque
n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([0]*n)
cnt = 0


while True:
  # 종료 조건: 내구도가 0 인것이 k 이상일때
  if a.count(0) >= k:
    break
  # 벨트, 로봇 순으로 회전
  a.rotate(1)
  robot.rotate(1)
  robot[-1] = 0   # 내리는 구간이므로 초기화
  if 1 in robot: # 로봇이 존재하면
    for i in range(n-2, -1, -1):  # 먼저 올라간 로봇 부터(N의 위치에 가까운)
      # 현재 위치(i)에 로봇이 존재하고, 한칸 앞에 로봇이 없고, 내구도가 0초과이면,
      if robot[i] == 1 and robot[i+1] == 0 and a[i+1]>0:
        robot[i+1] = 1
        robot[i] = 0
        a[i+1] -= 1
    robot[-1] = 0 # 로봇 내리는 부분에 있다면 내리기
  # 로봇 올리기: 올리는 위치(1위치 idx로는 0)에 로봇이 없고, 내구도가 0초과이면,
  if robot[0] == 0 and a[0] > 0:
    robot[0] = 1
    a[0] -= 1
  cnt += 1


print(cnt)