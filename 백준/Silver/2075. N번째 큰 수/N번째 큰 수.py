import heapq

N = int(input())
q = []
ans = 0
for _ in range(N):
  li = list(map(int, input().split()))
  
  for i in li:
    if len(q) < N:
      heapq.heappush(q, i)
    else:
      if q[0] < i:
        heapq.heappop(q)
        heapq.heappush(q, i)
print(q[0])