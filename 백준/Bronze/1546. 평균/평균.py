import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
_num= []
M = max(num)
for i in num:
  _num.append(i/M*100)

avg = sum(_num)/N
print(avg)