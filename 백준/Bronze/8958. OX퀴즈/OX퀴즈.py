import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 0;
    li = list(input().strip())
    cnt = 0
    ans = 0
    for i in li:
        if i == "O":
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)