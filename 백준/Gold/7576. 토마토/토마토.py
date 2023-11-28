from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()


def bfs():
    while q:
        row, col = q.popleft()

        for dr, dc in dirs:
            nr, nc = row + dr, col + dc

            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == 0:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))


for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            q.append((i, j))
bfs()

ans = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, grid[i][j])
        
print(ans - 1)  # 첫날이 1부터 시작하므로 0으로 맞춰줌
