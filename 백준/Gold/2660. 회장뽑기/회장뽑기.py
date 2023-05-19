import sys
input = sys.stdin.readline

m = int(input())
li = [[] for _ in range(m+1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    li[a].append(b)
    li[b].append(a)

# 점수 계산(bfs)
def calcScore(mem):
    visited = set()
    q = [(mem, 0)]
    
    while q:
        temp, score = q.pop(0)
        visited.add(temp)
        for friend in li[temp]:
            if friend not in visited:
                q.append((friend, score + 1))
                visited.add(friend)
    return score

scores = [calcScore(mem) for mem in range(1, m+1)]
pos_mem = [i+1 for i in range(m) if scores[i] == min(scores)]

print(f'{min(scores)} {len(pos_mem)}')
print(*pos_mem)