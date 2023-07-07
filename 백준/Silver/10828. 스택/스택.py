import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
  cmd = input().split()
  if cmd[0] == 'push':
    stack.append(int(cmd[1]))
  if cmd[0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  if cmd[0] == 'size':
    print(len(stack))
  if cmd[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  if cmd[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])