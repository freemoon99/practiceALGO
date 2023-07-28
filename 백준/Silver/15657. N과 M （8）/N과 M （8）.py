import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = []

def dfs(s):
  if len(ans) == m:
    print(*ans)
    return
  for i in range(s, n):
    ans.append(numbers[i])
    dfs(i)
    ans.pop()

dfs(0)