from collections import deque

def solution(maps):
    answer = 0
    n = len(maps) # row
    m = len(maps[0]) # col
    visited = [[0]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    
    def bfs(r,c):
        nonlocal visited, dist
        
        q = deque()
        q.append((r,c))
        visited[r][c] = 1
        
        while q:
            x, y = q.popleft()
            
            if (x,y) == (0,0):
                return dist[x][y]
            
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x+dx, y+dy
                
                if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                    if maps[nx][ny] == 1:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                        dist[nx][ny] = dist[x][y]+1
    
    ans = bfs(n-1, m-1)
    
    if ans:
        answer = ans+1
    else:
        answer = -1
    
    return answer