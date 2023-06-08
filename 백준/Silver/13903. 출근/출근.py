import sys
input = sys.stdin.readline
from collections import deque

# 입력 받기
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
n = int(input())
rule = [list(map(int, input().split())) for _ in range(n)]

# 초기화
q = deque()

# 1. 세로 블록만 밟는다. 첫 번째 row의 세로 블록 중 아무 곳에서 출발
for i in range(c):
    if board[0][i] == 1:
        q.append((0, i, 0))  # (x, y, count) 형태로 큐에 추가, count 초기값은 0

# BFS 시작
while q:
    curr = q.popleft()
    x, y, count = curr

    # 2. 주어진 규칙에 따라 이동 (rule 리스트 사용)
    for dx, dy in rule:
        nx = x + dx
        ny = y + dy

        # 이동한 위치가 보드 범위를 벗어나지 않고, 방문하지 않은 위치라면
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 1:
            q.append((nx, ny, count + 1))  # count 증가하여 큐에 추가
            board[nx][ny] = 0  # 방문한 위치는 0으로 표시

            # 3. 마지막 row에 도착한 경우, 출근 성공
            if nx == r - 1:
                print(count + 1)  # 이동 횟수 출력
                sys.exit()  # 프로그램 종료

# 출근에 실패한 경우
print(-1)