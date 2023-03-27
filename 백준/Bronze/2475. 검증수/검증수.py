import sys
input = sys.stdin.readline

num = map(int, input().split())
_num = []
for i in num:
    _num.append(i*i)

print(sum(_num)%10)