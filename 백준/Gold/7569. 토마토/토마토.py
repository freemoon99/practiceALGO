from collections import deque

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()

# 익어 있는 토마토 리스트
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))


def in_range(x, y, z):
    return (0 <= x < N) and (0 <= y < M) and (0 <= z < H)


def bfs():  # 0인 것만 방문 하면 됨
    dirs = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]  # 위, 아래, 왼, 오, 앞, 뒤
    while q:
        h, n, m = q.popleft()

        for dr, dc, dz in dirs:
            nh, nn, nm = h + dz, n + dr, m + dc

            if in_range(nn, nm, nh):  # 범위 안에 속해있을 때
                if boxes[nh][nn][nm] == 0:
                    boxes[nh][nn][nm] = boxes[h][n][m] + 1  # 방문 처리
                    q.append((nh, nn, nm))


# 토마토 퍼트리기
bfs()

# 토마토가 모두 익지 못하는 상태, 모두 익을 수 있는 상태
ans = 0
for i in boxes:
    for j in i:
        for k in j:
            if k == 0:  # 안 익은 토마토가 존재함
                print(-1)
                exit(0)
        ans = max(ans, max(j))
# 처음이 0일 기준으로 해야 함으로 -1
print(ans-1)
