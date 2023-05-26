import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

dp = [0]*(n+1)
long = 0

for i in range(n):
    idx = line[i]
    dp[idx] = dp[idx-1]+1
    long = max(long, dp[idx])
    
print(n-long)