# 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방 선호
# 각 층에 w개 방, h층 건물
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    grid = [[0] * w for _ in range(h)]

    floor = n % h
    room_num = (n // h) + 1

    if floor == 0:
        room_num = n//h
        floor = h

    print(floor * 100 + room_num)