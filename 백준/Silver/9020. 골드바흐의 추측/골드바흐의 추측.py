import sys
input = sys.stdin.readline

T = int(input())
n = [int(input()) for _ in range(T)]

a = [False, False] + [True]*10000

for i in range(2, 10001):
    if a[i] == True:
        for j in range(2*i, 10001, i):
            a[j] = False
for x in n:
    A, B = x//2, x//2
    while A > 0:
        if a[A] and a[B]:
            print(A, B)
            break
        A -= 1
        B += 1
