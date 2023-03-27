import sys
input = sys.stdin.readline

li = []

for _ in range(9):
    li.append(int(input().strip()))

print(max(li))
print(li.index(max(li))+1)