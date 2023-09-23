from collections import deque
n, m, v = map(int, input().split())
li = [[] for _ in range(n+1)]
visitedD = [False]*(n+1)
visitedB = [False]*(n+1)

def dfs(s):
    print(s, end=" ")
    visitedD[s] = True

    for i in li[s]:
        if not visitedD[i]:
            dfs(i)

def bfs(s):
    q = deque()
    q.append(s)
    visitedB[s] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in li[now]:
            if not visitedB[i]:
                visitedB[i] = True
                q.append(i)


# 입력 받아주고, 연결 리스트 구현
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

for i in range(n+1):
    li[i].sort()

# dfs 출력
dfs(v)
print()
# bfs 출력
bfs(v)