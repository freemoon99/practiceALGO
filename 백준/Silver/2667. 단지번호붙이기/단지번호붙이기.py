n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
complex = 0
counts = []

def dfs(r, c):
    cnt = 1
    visited[r][c] = 1
    grid[r][c] = complex

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if visited[nr][nc] == 0:
                if grid[nr][nc] == 1:
                    cnt += dfs(nr, nc)

    return cnt


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            complex += 1
            counts.append(dfs(i, j))

print(complex)
counts.sort()
for num in counts:
    print(num)
