n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]  # 2차원 배열, [물건][무게]
lst = [[0, 0]]  # 기준이되는 0,0추가

for i in range(n):
    w, v = map(int, input().split())
    lst.append([w, v])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = lst[i]

        if j < w:  # 최대 무게가 현재 무게보다 작을 경우 이전 기준 가져오기
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
