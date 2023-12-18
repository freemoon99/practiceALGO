from collections import deque

n = int(input())
lst = [list(input()) for _ in range(n)]
res = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def bfs(r, c):
    global visited
    q = deque()
    q.append((r, c))
    cnt = 0

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] == "*":
                    cnt += 1

    res[r][c] = cnt

flag = 0
for i in range(n):
    for j in range(n):
        if res[i][j] == 'x':
            if lst[i][j] == '*':
                flag = 1
            bfs(i, j)

if flag:
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '*':
                res[i][j] = '*'

for s in res:
    print("".join(map(str, s)))
