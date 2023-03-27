import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()
    _S = list(S)
    ans = ""
    for i in _S:
        ans += int(R) * i
    print(ans)