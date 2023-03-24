T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  importance = list(map(int, input().split()))
  order = [0 for i in range(N)]
  order[M] = 1
  cnt = 0
  
  while True:
    if importance[0] == max(importance):
      cnt += 1
      if order[0] == 1:
        print(cnt)
        break
      importance.pop(0)
      order.pop(0)
    else:
      importance.append(importance.pop(0))
      order.append(order.pop(0))