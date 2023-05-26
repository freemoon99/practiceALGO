import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global res
    visited[x] = True
    cycle.append(x)
    node = nums[x]
    
    if visited[node]:
        if node in cycle:
            res += cycle[cycle.index(node):]
            return
    else:
        dfs(node)
        
t = int(input())

for _ in range(t):
    n = int(input())
    nums = [0]+ list(map(int, input().split()))
    res = []
    visited = [True]+[False]*(n)
    
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(res))