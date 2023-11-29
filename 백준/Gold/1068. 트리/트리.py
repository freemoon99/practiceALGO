n = int(input())
nodes = list(map(int, input().split()))
remove_node = int(input())
graph = [[] for _ in range(n)]

# 노드 연결하기
for i, p in enumerate(nodes):
    if p == -1:
        continue
    graph[p].append(i)

# 연결된 자식 노드들 찾기
candidate = []
candidate_parents = []
visited = set()

# 지워야 하는 노드들 찾기
def dfs(node):
    visited.add(node)
    candidate.append(node)

    for i in graph[node]:
        if i not in visited:
            dfs(i)

# 지워야 하는 노드들의 부모 찾기
def find_parents(node):
    candidate_parents.append((node, nodes[node]))


# 노드와 연결된 노드 지우기(간선지우기..?)
dfs(remove_node)
candidate.sort()

for i in candidate:
    find_parents(i)

for target, parents in candidate_parents:
    if parents == -1:   # 루트 노드 이므로
        continue
    graph[parents].remove(target)

# 노드 지우기
for i, cand in enumerate(candidate):
    graph.pop(cand - i)  # pop 하는 순간 i만큼 없어지니까(순서대로 정렬되므로 앞에서 부터 사라짐)

cnt = 0
for l in graph:
    if not l:
        cnt += 1

print(cnt)
