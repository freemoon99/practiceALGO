import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0

for i in a:
  remain = i-b
  if remain <=0:
    ans += 1
  else:
    ans += 1
    if remain % c == 0:
      ans += remain//c
    else:
      ans = ans + remain//c +1

print(ans)