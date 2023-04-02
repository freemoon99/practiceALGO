import sys
input = sys.stdin.readline

A, B = map(str, input().split())

_A = "".join(reversed(A))
_B = "".join(reversed(B))

if int(_A) < int(_B):
  print(_B)
else:
  print(_A)
