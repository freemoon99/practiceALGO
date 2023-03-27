import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str = list(input().strip())
    print(str[0], str[-1], sep="")
