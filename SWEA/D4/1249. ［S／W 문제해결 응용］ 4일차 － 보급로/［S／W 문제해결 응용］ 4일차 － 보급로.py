from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    dist = [[1e9] * n for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = deque()
    q.append((0, 0))
    dist[0][0] = 0

    while q:
        r, c = q.popleft()

        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if dist[nr][nc] > dist[r][c] + grid[nr][nc]:
                    dist[nr][nc] = dist[r][c] + grid[nr][nc]
                    q.append((nr,nc))
                    
    print(f"#{test_case} {dist[n-1][n-1]}")
