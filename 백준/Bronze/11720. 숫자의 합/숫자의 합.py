import sys
input = sys.stdin.readline

n = int(input())
li = [int(i) for i in list(input().strip())]
print(sum(li))