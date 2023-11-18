T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # (0, 0) -> (n-m,n-m) 까지 탐색
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(m):
                for l in range(m):
                    temp += grid[i+k][j+l]
            ans = max(ans, temp)
    print(f"#{test_case} {ans}")