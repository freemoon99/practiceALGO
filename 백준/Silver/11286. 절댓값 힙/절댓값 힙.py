import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []

for _ in range(n):
  info = int(input())
  if info == 0:
    if len(arr) == 0:
      print(0)
    else:
      print(heapq.heappop(arr)[1])
  else:
    heapq.heappush(arr, (abs(info), info))
