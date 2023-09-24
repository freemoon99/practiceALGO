com = int(input())
n = int(input())
virus = [[] for _ in range(com+1)]
visited = [0 for _ in range(com+1)]
cnt = 0

for _ in range(n):
    a, b = map(int, input().split())

    virus[a].append(b)
    virus[b].append(a)

def dfs(s):
    global cnt
    visited[s] = 1

    for i in virus[s]:
        if visited[i] == 0:
            visited[i] = 1
            cnt+=1
            dfs(i)

dfs(1)
print(cnt)