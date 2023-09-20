n, m = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(n)]
house = []
chick = []
res = int(1e9)
# 집과 치킨집 좌표들 찾기 (모든 좌표는 1부터 시작함)
for i in range(n):
    for j in range(n):
        if grids[i][j] == 1:
            house.append([i, j])
        elif grids[i][j] == 2:
            chick.append([i, j])

# 조합 구현
def comb(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in comb(arr[i+1:], r-1):
                yield [arr[i]]+next

# 치킨 집에서 m개 뽑아서 치킨 거리 구하기
for c in comb(chick, m):
    cd = 0  # 현재 치킨 거리(chicken distance)
    for h in house:
        temp = int(1e9)
        for dot in c:   # 치킨 거리 저장(치킨 집과의 가장 짧은 거리)
            temp = min(temp, abs(h[0]-dot[0]) + abs(h[1]-dot[1]))
        cd += temp
    res = min(res, cd)

print(res)