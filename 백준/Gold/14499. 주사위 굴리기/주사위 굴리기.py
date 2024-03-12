import sys

input = sys.stdin.readline

n, m, r, c, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
fr, ba, le, ri, to, bo = 0, 0, 0, 0, 0, 0

for d in order:
    nr, nc = r, c  # 새로운 위치를 미리 계산
    if d == 4:  # 남
        nr += 1
    elif d == 3:  # 북
        nr -= 1
    elif d == 2:  # 서
        nc -= 1
    elif d == 1:  # 동
        nc += 1

    # 이동이 격자 범위 내인지 확인
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        continue  # 범위를 벗어나면 이동하지 않음

    # 이동이 유효하면 위치 업데이트
    r, c = nr, nc

    if d == 4:  # 남
        temp = [to, fr, bo, ba]   # 앞, 바닥, 뒤, 위 순
        if grid[r][c] == 0:
            grid[r][c] = temp[1]
        else:
            temp[1] = grid[r][c]
            grid[r][c] = 0

        fr, bo, ba, to = temp

    if d == 3:  # 북
        temp = [bo, ba, to, fr]  # 앞, 바닥, 뒤, 위 순
        if grid[r][c] == 0:
            grid[r][c] = temp[1]
        else:
            temp[1] = grid[r][c]
            grid[r][c] = 0

        fr, bo, ba, to = temp

    if d == 2:  # 서
        temp = [to, le, bo, ri]  # 좌, 바닥, 우, 위 순
        if grid[r][c] == 0:
            grid[r][c] = temp[1]
        else:
            temp[1] = grid[r][c]
            grid[r][c] = 0

        le, bo, ri, to = temp

    if d == 1:  # 동
        temp = [bo, ri, to, le]  # 좌, 바닥, 우, 위 순
        if grid[r][c] == 0:
            grid[r][c] = temp[1]
        else:
            temp[1] = grid[r][c]
            grid[r][c] = 0

        le, bo, ri, to = temp

    print(to)