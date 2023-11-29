h, y = map(int, input().split())
MAX_YEAR = 11
dp = [0 for _ in range(MAX_YEAR)]  # 해당 년도가 지난 시점의 최댓값 저장
dp[0] = h

for i in range(1, MAX_YEAR):
    if i >= 5:  # a,b,c 투자 모두 가능
        dp[i] = int(max(dp[i-1] * (1 + 0.05), dp[i-3] * (1 + 0.2), dp[i-5] * (1 + 0.35)))
    elif i >= 3:  # a,b가능
        dp[i] = int(max(dp[i-1] * (1 + 0.05), dp[i-3] * (1 + 0.2)))
    else:
        dp[i] = int(dp[i-1] * (1 + 0.05))


ans = int(dp[y])  # 소수점 버리기
print(ans)
