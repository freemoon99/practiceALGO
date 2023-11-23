import copy
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
calc = list(map(int, input().split()))

# n과 m은 항상 짝수
# 1번 연산 (상하 반전)
def one():
    global a
    mid = n // 2

    for i in range(mid):
        a[mid - i - 1], a[mid + i] = a[mid + i], a[mid - i - 1]

# 2번 연산 (좌우 반전)
def two():
    global a
    mid = m//2

    for i in range(n):
        for j in range(mid):
            a[i][j], a[i][m - 1 - j] = a[i][m - 1 - j], a[i][j]


# 3번 연산 (오른쪽 90도) : 기존 n -> m, 기존 m -> n
def three():
    global a, n, m
    temp = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            temp[j][(n - i) - 1] = a[i][j]

    n, m = m, n
    a = temp

# 4번 연산 (왼쪽 90도 = 오른쪽 270도) : 기존 n -> m, 기존 m -> n
def four():
    global a, n, m
    temp = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            temp[m - j - 1][i] = a[i][j]

    n, m = m, n
    a = temp


# 5번 연산 (4구역 시계방향)
def five():
    global a
    n, m = len(a), len(a[0])
    temp = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # 1번 구역 -> 2번 구역
            if 0 <= j < (m//2) and 0 <= i < (n//2):
                temp[i][j+(m//2)] = a[i][j]
            # 2번 구역 -> 3번 구역
            if (m//2) <= j < m and 0 <= i < (n//2):
                temp[i+(n//2)][j] = a[i][j]
            # 3번 구역 -> 4번 구역
            if (m//2) <= j < m and (n//2) <= i < n:
                temp[i][j-(m//2)] = a[i][j]
            # 4번 구역 -> 1번 구역
            if 0 <= j < (m//2) and (n//2) <= i < n:
                temp[i-(n//2)][j] = a[i][j]
    a = temp

# 6번 연산 (4구역 반시계 방향)
def six():
    global a
    temp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # 1번 구역 -> 4번 구역
            if 0 <= j < (m // 2) and 0 <= i < (n // 2):
                temp[i+(n//2)][j] = a[i][j]
            # 2번 구역 -> 1번 구역
            if (m // 2) <= j < m and 0 <= i < (n // 2):
                temp[i][j-(m//2)] = a[i][j]
            # 3번 구역 -> 2번 구역
            if (m // 2) <= j < m and (n // 2) <= i < n:
                temp[i-(n//2)][j] = a[i][j]
            # 4번 구역 -> 3번 구역
            if 0 <= j < (m // 2) and (n // 2) <= i < n:
                temp[i][j+(m//2)] = a[i][j]
    a = temp


for i in calc:
    if i == 1:
        # 1번 연산 수행
        one()
    if i == 2:
        # 2번 연산 수행
        two()
    if i == 3:
        # 3번 연산 수행
        three()
    if i == 4:
        # 4번 연산 수행
        four()
    if i == 5:
        # 5번 연산 수행
        five()
    if i == 6:
        # 6번 연산 수행
        six()

# 결과 출력
for row in a:
    print(*row)
