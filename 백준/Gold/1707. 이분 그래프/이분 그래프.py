import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())


def dfs(s, group):
    # 현재 노드를 그룹에 저장
    visited[s] = group
    # 인접 노드 탐색
    for i in graph[s]:
        # 방문하지 않았다면 다른 그룹
        if not visited[i]:
            res = dfs(i, -group)
            if not res:
                return False
        # 인접한 정점과 같은 그룹이라면 거짓
        elif visited[i] == group:
            return False
    # 그 외에는 참
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        # 무방향 그래프 구현
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        # 방문하지 않았다면
        if not visited[i]:
            res = dfs(i, 1)
            # 결과가 거짓이라면 종료
            if not res:
                break

    print("YES" if res else "NO")