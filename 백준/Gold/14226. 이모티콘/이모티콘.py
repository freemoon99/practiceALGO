from collections import deque

s = int(input())
MAX_RANGE = 1001


def in_range(sc, cl):
    return 0 <= sc < MAX_RANGE and 0 <= cl < MAX_RANGE


# bfs
def bfs():
    time = 0  # 걸리는 시간
    screen = 1  # 최초에 1개 입력된 상태
    clipboard = 0  # 클립보드에 저장된 갯수
    visited = [[0] * MAX_RANGE for _ in range(MAX_RANGE)]
    q = deque()
    q.append((screen, clipboard, time))

    while q:
        ns, nc, t = q.popleft()
        # 종료 조건 : 화면에 출력된 갯수가 같을 원하는 결과값인 경우
        if ns == s:
            print(t)
            break

        for i in range(3):
            if visited[ns][nc] == 1: continue

            if i == 0:  # 복사
                new_screen, new_clip = ns, ns
                if in_range(new_screen, new_clip):
                    q.append((new_screen, new_clip, t + 1))

            if i == 1:  # 붙여넣기
                if nc == 0: continue
                new_screen, new_clip = ns + nc, nc
                if in_range(new_screen, new_clip):
                    q.append((new_screen, new_clip, t + 1))

            if i == 2:  # 삭제
                if ns == 0: continue
                new_screen, new_clip = ns - 1, nc
                if in_range(new_screen, new_clip):
                    q.append((new_screen, new_clip, t + 1))

        visited[ns][nc] = 1  # 연산 수행 후에 방문 처리


bfs()
