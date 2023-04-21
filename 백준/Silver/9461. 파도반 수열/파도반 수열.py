import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(102)]
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(4, 101):
  dp[i] = dp[i-3]+dp[i-2]

for _ in range(t):
  n = int(input())
  print(dp[n])