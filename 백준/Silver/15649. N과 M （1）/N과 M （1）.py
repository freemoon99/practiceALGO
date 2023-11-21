# 자연수 n,m이 주어졌을 때,
# 1. 1~n까지 중복 없이 m개를 고른 수열(자연수)

n, m = map(int, input().split())

selected = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]

# 함수 정의 : 중복 가능한 수열 찾기
def func(cnt):
    if cnt == m:    # m개 를 골랐으면 출력
        print(" ".join(map(str, selected)))
    else:
        for candidate in range(1, n+1):
            if used[candidate]:
                continue
            selected[cnt] = candidate
            used[candidate] = 1
            func(cnt+1)
            selected[cnt] = 0
            used[candidate] = 0

func(0)