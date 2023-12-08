from collections import deque

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


# 열 수 있는 국경 탐색
# 열린 국경 리턴
def bfs(row, col):
    union = []
    q = deque()
    q.append((row, col))
    union.append((row, col))

    while q:
        now_r, now_c = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = now_r + dx, now_c + dy

            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    sub = abs(a[now_r][now_c] - a[nr][nc])
                    if l <= sub <= r:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        union.append((nr, nc))
    return union


days = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                union = bfs(i, j)

                if len(union) > 1:
                    flag = 1
                    member_sum = sum(a[x][y] for x, y in union)

                    for x, y in union:
                        a[x][y] = member_sum // len(union)

    if flag == 0:
        print(days)
        break

    days += 1
