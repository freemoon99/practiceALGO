n, m = map(int, input().split())
A = [0]+[[0]+list(map(int, input().split())) for _ in range(n)]   # 0을 추가하여 인덱스를 맞춤, (1,1)->(n,n)까지 맞추기 위함
di = [[0,0], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1, 1], [1,0], [1,-1]]  # 8방향 인덱스 맞추기

# 대각선 거리 1인 칸에 물이 있는 바구니 수 확인
def diagonal_cnt(row, col):
  count = 0
  for dr, dc in di[2::2]:
    nr = row + dr
    nc = col + dc
    if 1<=nr<=n and 1<=nc<=n: # 범위 안에 있을때 -> 경계를 넘어가면 거리가 1이 아니기 때문
      if A[nr][nc] != 0:
        count += 1
  return count

# [0] 구름 초기화
cloud = [[n,1], [n,2], [n-1,1], [n-1,2]]

for _ in range(m):
  d, s = map(int, input().split())
  
  # [1] 모든 구름이 di방향으로 si만큼 이동
  for i in range(len(cloud)):
    cloud[i][0] = (cloud[i][0] + di[d][0]*s-1) % n + 1
    cloud[i][1] = (cloud[i][1] + di[d][1]*s-1) % n + 1
  # [2] 각 구름에서 비가 내려 물 증가
  for row, col in cloud:
    A[row][col]+=1
  # [3] 구름 사라짐
  cloud_copy = set(tuple(item) for item in cloud)
  cloud = []
  # [4] 물 복사 버그 마법
  for row, col in cloud_copy:
    A[row][col] += diagonal_cnt(row, col)
  # [5] 새로운 구름 생성
  for i in range(1, n+1):
    for j in range(1, n+1):
      if (i, j) not in cloud_copy:  # 이전에 구름이 생성된 지역이 아닐 때
        if A[i][j] >= 2:  # 바구니의 물의 양이 2 이상이면 구름 생성
          cloud.append([i,j])
          A[i][j] -= 2

# 바구니에 들어있는 물의 총합 구하기
total = sum(sum(row) for row in A[1:])
print(total)