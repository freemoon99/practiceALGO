n, m, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
fireballs = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])  # 인덱스 0부터 시작

# 방향
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# k번 명령
for _ in range(k):
    # 이동
    while fireballs:
        _r, _c, _m, _s, _d = fireballs.pop()
        dr, dc = dirs[_d]
        nr = (_r + (dr * _s)) % n
        nc = (_c + (dc * _s)) % n
        grid[nr][nc].append([_m, _s, _d])

    for i in range(n):
        for j in range(n):
            # 2개 이상 파이어볼이 있는 경우
            if len(grid[i][j]) > 1:
                sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(grid[i][j])

                while grid[i][j]:
                    now_m, now_s, now_d = grid[i][j].pop()
                    sum_m += now_m
                    sum_s += now_s
                    if now_d%2 == 0:
                        even += 1
                    else:
                        odd += 1

                if odd == cnt or even == cnt:  # 방향이 모두 짝수 이거나, 모두 홀수 이면
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                # 질량이 존재할 때, 4방향 분해됨
                if sum_m // 5:
                    for direction in nd:
                        dx, dy = dirs[direction]
                        fireballs.append([i, j, (sum_m // 5), (sum_s // cnt), direction])

            # 아닌 경우(1개인 경우)
            if len(grid[i][j]) == 1:
                om, os, od = grid[i][j].pop()
                fireballs.append([i, j, om, os, od])

# 모든 파이어볼의 질량의 합
answer = 0
for i in fireballs:  # 파이어볼 = [행, 열, 질량, 속력, 방향] 순
    answer += i[2]

print(answer)
