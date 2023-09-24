n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

ans1 = 0
ans2 = []

def dfs(row, col):
    visited[row][col] = 1
    cnt = 1 # 현재 단지의 집 수를 세기 위함

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0<=nr<n and 0<=nc<n and visited[nr][nc] == 0:
            if graph[nr][nc] == 1:
                cnt += dfs(nr, nc)

    return cnt # 현재 단지의 집 수 반환

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            ans1 += 1 # 단지 수를 체크하기 위함
            ans2.append(dfs(i, j))
print(ans1)
ans2.sort()
for i in ans2:
    print(i)