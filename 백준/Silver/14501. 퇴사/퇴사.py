n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]  # t,p 순으로 배열 저장 됨

dp = [0 for _ in range(n + 1)]

for i in range(n):  # 7일 이므로 i는 날짜 기준
    for j in range(i + schedule[i][0], n + 1):  # 현재일에 상담을 했다면 +기간 한 날 부터 시작
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = max(dp[j], dp[i] + schedule[i][1])

print(max(dp))