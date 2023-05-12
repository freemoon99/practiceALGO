import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in nums:
    if isPrime(i):
        cnt += 1
        
print(cnt)