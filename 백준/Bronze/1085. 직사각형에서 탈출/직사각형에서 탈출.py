import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
answer = min(abs(0-x), abs(0-y), abs(x-w), abs(y-h))

print(answer)