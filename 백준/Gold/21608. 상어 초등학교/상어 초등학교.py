n = int(input())
seats = [[0]*(n+1) for _ in range(n+1)]
like_list = [0]*(n*n+1)
order = []

# 상좌우하순
dr = [-1, 0, 0, 1]
dc = [0, 1, -1, 0]

# 좋아하는 사람 리스트와 순서 저장
for _ in range(n*n):
  num = list(map(int, input().split()))
  like_list[num[0]] = num[1:]
  order.append(num[0])

# 학생 자리 배치
for now in order:
  temp = [] # 현재 학생을 앉힐 수 있는 자리 후보군
  for i in range(1, n+1):
    for j in range(1, n+1):
      if seats[i][j] == 0:   # 빈칸일 경우
        like_cnt = 0  # 좋아하는 학생 수
        empty_cnt = 0  # 인접한 빈칸 수

        for k in range(4):  # 4방향 탐색
          nr = i + dr[k]
          nc = j + dc[k]
          
          if 1<=nr<n+1 and 1<=nc<n+1:   # 좌석 범위일 때
            if seats[nr][nc] in like_list[now]:   # 인접한 칸에 좋아하는 사람이 있다면
              like_cnt += 1
            if seats[nr][nc] == 0: # 인접한 칸이 비었다면
              empty_cnt += 1
        
        # 후보군에 추가 [인접한 좋아하는 학생수, 인접한 빈칸 수, 현재 행, 현재 열]
        temp.append([like_cnt, empty_cnt, i, j])

  # 리스트를 정렬 (like_cnt와 empty_cnt는 내림차순, 행과 열은 오름차순)
  temp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
  
  # 최적의 조건에 학생 배치 (행과 열)
  seats[temp[0][2]][temp[0][3]] = now

# 점수 계산
res = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    now = seats[i][j] 
    cnt = 0
    
    for k in range(4):
      nr = i + dr[k]
      nc = j + dc[k]
      # 범위 안이고, 인접한 학생이 좋아하는 학생이라면
      if 1<=nr<n+1 and 1<=nc<n+1 and seats[nr][nc] in like_list[now]:  
          cnt += 1
      
    if cnt != 0:
      res += 10**(cnt-1)

print(res)