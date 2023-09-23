import sys
sys.setrecursionlimit(10 ** 4)

n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]
locMin = min(map(min, loc))     # 지역에서 최소 높이
locMax = max(map(max, loc))     # 지역에서 최대 높이
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ans = 1     # 아무것도 잠기 않았을 경우는 안전영역이 1이기 때문에

def dfs(row, col, h):
    for i in range(4):  # 4방향 순회
        nr = row + dr[i]
        nc = col + dc[i]
        if 0<=nr<n and 0<=nc<n and visited[nr][nc] == 0 and loc[nr][nc] > h:    # 다음 위치가 범위 안이고, 방문 가능하다면
            visited[nr][nc] = 1
            dfs(nr, nc, h)


for rain in range(locMin, locMax):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            # 현재 위치 (i, j)가 방문하지 않았고, 내리는 비의 양보다 크다면 체크
            if visited[i][j] == 0 and loc[i][j] > rain:
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, rain)

    ans = max(ans, cnt)

print(ans)