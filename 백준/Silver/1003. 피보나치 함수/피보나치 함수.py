t = int(input())
dp = [[0, 0] for _ in range(41)]   # 최대 40까지 이므로
dp[0] = [1,0]
dp[1] = [0,1]

for _ in range(t):
    n = int(input())
    if n>1: # n이 2부터 fibo 적용
        for i in range(2, n+1):
            dp[i] = [dp[i-1][1], dp[i-1][0]+dp[i-1][1]]
    # 출력 : 0이 출력되는 횟수, 1이 출력되는 횟수
    print(f'{dp[n][0]} {dp[n][1]}')