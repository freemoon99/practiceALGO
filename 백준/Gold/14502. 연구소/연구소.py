from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus_list = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 2]
empty_list = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 0]
ans = 0

# 벽 세우기
def wall(start, cnt):
    global ans

    # 종료 조건 : 벽 3개를 세웠을 때
    if cnt == 3:
        temp_graph = [row[:] for row in graph]
        for v in virus_list:
            bfs(v[0], v[1], temp_graph)
        safe_zones = sum(i.count(0) for i in temp_graph)
        ans = max(ans, safe_zones)
        return

    for i in range(start, len(empty_list)):
        x, y = empty_list[i]
        graph[x][y] = 1
        wall(i + 1, cnt + 1)
        graph[x][y] = 0

# 바이러스 퍼트리기
def bfs(x, y, temp_graph):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                bfs(nx, ny, temp_graph)

# 메인 함수 실행
wall(0, 0)
print(ans)
