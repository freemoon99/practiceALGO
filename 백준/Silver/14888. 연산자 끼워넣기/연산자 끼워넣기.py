import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxRes = -1e9
minRes = 1e9

def dfs(depth, total, add, sub, mul, div):
  global maxRes, minRes
  # 종료 조건 : n개의 숫자가 모두 연산되었다면 
  if depth == n:
    minRes = min(total, minRes)
    maxRes = max(total, maxRes)
    return
  
  if add:
    dfs(depth+1, total + num[depth], add -1, sub, mul, div)
  if sub:
    dfs(depth+1, total - num[depth], add, sub-1, mul, div)
  if mul:
    dfs(depth+1, total * num[depth], add, sub, mul-1, div)
  if div:
    dfs(depth+1, int(total / num[depth]), add, sub, mul, div-1)
    

dfs(1, num[0], add, sub, mul, div)
print(maxRes)
print(minRes)