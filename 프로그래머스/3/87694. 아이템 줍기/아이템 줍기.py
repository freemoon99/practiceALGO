from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX_VALUE = 102
    grid = [['*']*MAX_VALUE for _ in range(MAX_VALUE)]
    
    # 테두리 찾기 -> 외곽은 1로 바꾸고, 범위 안이면 0으로 바꾸기 (겹치는 부분도 0으로 바뀜)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    grid[i][j] = 0
                elif grid[i][j] != 0:
                    grid[i][j] = 1
    
    visited = [[0]*MAX_VALUE for _ in range(MAX_VALUE)]
    q = deque()
    q.append((characterX*2, characterY*2))
    
    while q:
        cx, cy = q.popleft()
        
        if (cx, cy) == (itemX*2, itemY*2):
            answer = visited[cx][cy]//2
            break
        
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx+dx, cy+dy
            
            if grid[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1

    return answer