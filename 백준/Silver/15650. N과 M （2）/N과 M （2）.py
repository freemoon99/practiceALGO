# 자연수 n,m이 주어졌을 때,
# 1. 1~n까지 중복 x m개를 고른 수열(자연수)
# 2. 오름차순


n, m = map(int, input().split())

selected = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]

# 함수 정의 : 중복 가능한 수열 찾기
def func(cnt):
    if cnt == m:    # m개 를 골랐으면 출력
        print(" ".join(map(str, selected)))
    else: # 수 뽑기
        # 시작할때, 처음 뽑는 수가 아니라면 이전에 뽑은 수보다 커야함
        if cnt == 0:
            start = 1
        else:
            start = selected[cnt-1]

        for candidate in range(start, n+1):
            if used[candidate]:
                continue
            selected[cnt] = candidate
            used[candidate] = 1
            func(cnt+1)
            selected[cnt] = 0
            used[candidate] = 0

func(0)