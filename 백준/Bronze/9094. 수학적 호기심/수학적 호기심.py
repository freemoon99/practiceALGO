t = int(input())
dp = [[0]*101 for _ in range(101)]

for i in range(1, 100):
    for j in range(i + 1, 101):
        dp[i][j] = (i**2)+(j**2)

for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())

    for a in range(1, n-1):
        for b in range(a + 1, n):
            if (dp[a][b] + m) % (a * b) == 0:
                cnt += 1

    print(cnt)

