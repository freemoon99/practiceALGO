import sys
input = sys.stdin.readline

n = int(input())
strings = [input().rstrip() for _ in range(n)]
numbers = []

for s in strings:
  temp = ""
  for i in s:
    if i.isnumeric():
      temp += i
    elif temp:
      numbers.append(int(temp))
      temp = ""
  if temp:
    numbers.append(int(temp))

numbers.sort()
for j in numbers:
  print(j)