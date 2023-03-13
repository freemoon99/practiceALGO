N = int(input())
tower = list(map(int, input().split()))
stack = []
ans = [0]*N

for i in range(N):
  while stack:
    # 현재 탑의 높이가 stack의 탑보다 크다면 제거
    if tower[stack[-1][0]] < tower[i]:
      stack.pop()
    else:
      # 탑의 위치 저장(인덱스 이므로 타워의 위치는 +1 해줘야함)
      ans[i] = stack[-1][0] + 1
      break
  # 현재 타워와 idx 저장
  stack.append((i, tower[i]))
print(*ans)