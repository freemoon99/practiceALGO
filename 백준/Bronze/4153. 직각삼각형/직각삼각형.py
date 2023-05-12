import sys
input = sys.stdin.readline

while True:
    n = list(map(int, input().split()))
    n.sort()
    
    if n == [0, 0, 0]:
        break
    if (n[2]**2) == (n[0]**2+n[1]**2):
        print('right')
    else:
        print('wrong')