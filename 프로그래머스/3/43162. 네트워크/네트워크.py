from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n

    def bfs(r):
        nonlocal visited, answer

        q = deque()
        q.append(i)

        while q:
            now = q.popleft()
            visited[now] = 1
            
            for j in range(n):
                if computers[now][j] == 1 and visited[j] == 0:
                    q.append(j)
        answer += 1

    for i in range(n):
        if visited[i] == 0:
            bfs(i)

    return answer