import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    kind_list = []
    for i in range(n):
        name, kind = map(str, input().split())
        kind_list.append(kind)
    k = Counter(kind_list) # 데이터 갯수를 딕셔너리로 만들어 주는 걸로 알고 있음

    cnt = 1
    for i in k:
        cnt *= k[i]+1
    print(cnt-1)