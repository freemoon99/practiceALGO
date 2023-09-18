n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while True:
    isClean = False     # 청소 유무 판별
    # 주변 4방향 탐색
    for _ in range(4):
        d = (d+3) % 4
        nr = dr[d] + r
        nc = dc[d] + c

        # 그래프 범위 안, 탐색할 수 있다면
        if 0 <=nr<n and 0<=nc<m and graph[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt+=1
                r, c = nr, nc
                isClean = True
                break
    
    # 방문한 적이 있을때, 4방향 청소가 안되어있다면
    if not isClean:
        # 후진할 곳이 벽이라면
        if graph[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r-dr[d], c-dc[d]
