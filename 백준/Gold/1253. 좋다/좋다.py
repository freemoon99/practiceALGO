import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
li.sort()
good = 0

for i in range(N):
  temp = li[:i] + li[i+1:]
  start, end = 0, len(temp) -1
  
  while start < end:
    t = temp[start] + temp[end]
    if t == li[i]:
      good += 1
      break
    elif t < li[i]:
      start += 1
    else:
      end -= 1
      
print(good)