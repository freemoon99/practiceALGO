n = int(input())
dp = [0]*(n+1)

# 0 또는 1 이 1이 되는 방법은 없으니 0
# 따라서 2부터 시작

for i in range(2, n+1): # i가 1일 될때 연산 횟수
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[n])