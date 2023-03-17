N, K = map(int, input().split())
dol = list(map(int, input().split()))

start, end, cnt = 0, 0, 0
res = int(1e9)

# 만약 첫 인덱스가 1일 경우 라이언 카운트
if dol[end] == 1:
  cnt += 1

# end 인덱스가 N보다 작을때까지 반복
while end < N:
  # 만약 라이언의 수가 K와 같다면
  if cnt == K:
    # 최솟값 저장
      res = min(res, end - start + 1)
      # 배열의 첫 시작이 1일 경우 라이언 하나 제거-> 시작점이 이동하기 때문에 카운트 감소
      if dol[start] == 1:
        cnt -= 1
      # 시작점 증가
      start += 1
  else:
    # 끝 점 증가
    end += 1
    # 끝점이 인덱스의 마지막이 아니고, 끝점의 위치에 라이언이 있으면 카운트
    if end < N and dol[end] == 1:
      cnt += 1

if res == 1e9:
  print(-1)
else: 
  print(res)