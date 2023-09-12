import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

num = [i for i in range(n)]
def comb(arr, r):
  for i in range(len(arr)):
    if r == 1:
      yield [arr[i]]
    else:
      for next in comb(arr[i+1:], r-1):
        yield [arr[i]]+next

starts = []
# 팀 추출
for arr in comb(num, n/2):
  starts.append(arr)
# 능력치 계산
ans = int(1e9)
# 능력치는 스타트팀(Sij + Sji) - 링크팀(Si'j' + Sj'i')
# 자기 자신은 0 이니깐 계산에 영향 x
for start in starts:
  teamStart = 0
  teamLink = 0
  for i in start:
    for j in start:
      teamStart += grid[i][j]
  link = list(set(num)-set(start))
  for i in link:
    for j in link:
      teamLink += grid[i][j]
  ans = min(ans, abs(teamStart-teamLink))

print(ans)