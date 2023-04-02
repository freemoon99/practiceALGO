import sys
input = sys.stdin.readline

remain = set()

for _ in range(10):
  N = int(input())
  
  remain.add(N%42)

print(len(remain))