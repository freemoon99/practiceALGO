import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

li = [0 for i in range(10)]

x = A*B*C

for i in list(str(x)):
  li[int(i)] += 1

for j in li:
  print(j)