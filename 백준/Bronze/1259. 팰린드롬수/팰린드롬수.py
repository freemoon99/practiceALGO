import sys
input = sys.stdin.readline

while True:
    n = list(input().rstrip())
    if n == ['0']:
        break
    else:
        print('yes' if n == n[::-1] else 'no')