n = int(input())
candidate = []
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 0우, 1상, 2좌, 3하

for _ in range(n):
    temp = []
    x, y, d, g = map(int, input().split())
    temp.append((x, y))
    # [1] 방향들만 모두 저장
    dirs = [d]
    # 세대가 증가할 때, 지나는 방향들 추가
    for _ in range(g):
        revers_dirs = dirs[::-1]
        for i in range(len(revers_dirs)):
            dirs.append((revers_dirs[i] + 1) % 4)

    # [2] 방향들을 기준으로 좌표들 저장
    for idx in dirs:
        nx, ny = temp[-1][0] + direction[idx][0], temp[-1][1] + direction[idx][1]
        temp.append((nx, ny))

    candidate.extend(temp)

candidate = set(candidate)  # 중복 제거

# [3] 시작점을 좌상단 좌표로 설정하여 사각형에 속하는지 판단
cnt = 0

for i in candidate:
    ix, iy = i
    if ((ix + 1, iy) in candidate) and ((ix, iy + 1) in candidate) and ((ix + 1, iy + 1) in candidate):
        cnt += 1

print(cnt)
