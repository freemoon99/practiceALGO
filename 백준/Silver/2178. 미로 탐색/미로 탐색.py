from collections import deque

n,m = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited[row][col] == 1

    while q:
        now = q.popleft()
        # 4방향 탐색 (우하좌상순)
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            # 범위 안이고, 이동할 수 있다면
            if 0<=nc<m and 0<=nr<n and miro[nr][nc] == 1:
                if visited[nr][nc] == 0: # 방문 x
                    visited[nr][nc] = 1
                    miro[nr][nc] = miro[now[0]][now[1]]+1   # 방문 가능한 자리가 1이므로 더해가면 됨
                    q.append((nr, nc))

bfs(0,0)
print(miro[n-1][m-1])