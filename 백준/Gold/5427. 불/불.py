import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != 'FIRE':
            flag = visited[x][y]
        else:
            flag = "FIRE"
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (graph[nx][ny] == '.' or graph[nx][ny] == '@'):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx,ny))
            else:
                if flag != 'FIRE':
                    return flag + 1
    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    q = deque()
    graph = []
    visited = [[-1] * w for _ in range(h)]
    
    for i in range(h):
        graph.append(list(input().rstrip()))
        for j in range(w):
            if graph[i][j] == '@':
                visited[i][j] = 0
                s = (i, j)
            elif graph[i][j] == '*':
                visited[i][j] = 'FIRE'
                q.append((i, j))
    q.append(s)
    print(bfs())