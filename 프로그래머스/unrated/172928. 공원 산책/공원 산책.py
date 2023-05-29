def solution(park, routes):
    answer = []
    w = len(park[0])
    h = len(park)
    sx, sy = 0, 0
#     시작 지점 초기화
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                sx, sy = j, i
                break
#     움직임 선언
    move = {"E":(0, 1), "W":(0, -1), "N":(-1, 0), "S":(1, 0)}
#     움직임
    for i in routes:
        y, x = move[i[0]]
#         현재 위치
        nx, ny = sx, sy
#         이동하는 칸 수 만큼 이동할 때 => 1단위 이기 때문에 이동 수 만큼 반영됨
        for _ in range(int(i[2])):
#         이동할 수 있을 때, 이동한 칸이 X가 아니고, 0<x<w 범위 in 이고, 0<y<h 범위 in 일때,
            if 0 <= nx+x < w and 0 <= ny+y < h and park[ny+y][nx+x] != "X":
                nx, ny = nx+x, ny+y
            else:
                nx, ny = sx, sy
                break
        sx, sy = nx, ny

    return [sy, sx]