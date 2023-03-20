str = input()
bomb = input()
stack = []

for now in str:
  stack.append(now)
  if now == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
    for _ in range(len(bomb)):
      stack.pop()

ans = ''.join(stack)

if ans:
  print(ans)
else:
  print('FRULA')