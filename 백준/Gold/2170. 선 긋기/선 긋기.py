import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort()

leng = [li[0]]
ans = 0
for i in range(1, n):
    if leng[0][0] <= li[i][0] <= leng[0][1]:
        leng[0][1] = max(leng[0][1], li[i][1])
    else:
        ans += (leng[0][1]-leng[0][0])
        leng[0] = li[i]
        
ans += (leng[0][1]-leng[0][0])
print(ans)