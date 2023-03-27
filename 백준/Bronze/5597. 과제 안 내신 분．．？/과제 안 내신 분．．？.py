import sys
input = sys.stdin.readline

li = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    li.remove(n)

print(li[0])
print(li[1])
