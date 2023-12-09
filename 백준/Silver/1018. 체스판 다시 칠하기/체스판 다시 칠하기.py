n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
max_value = 0
cnt = []

# 시작점 기준으로 순회
for i in range(n-7):
    for j in range(m-7):
        start_black = 0
        start_white = 0

        # 시작점을 기준으로 8칸 순회
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:  # x+y가 짝수라면
                    if grid[x][y] != 'B':   # 시작점이 검은색 이라면
                        start_black += 1
                    if grid[x][y] != 'W':   # 시작점이 흰색 이라면
                        start_white += 1
                else:
                    if grid[x][y] != 'W':
                        start_black += 1
                    if grid[x][y] != 'B':
                        start_white += 1

        cnt.append(min(start_black, start_white))

print(min(cnt))