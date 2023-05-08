import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

multitap = []
cnt = 0

for i in range(k):
    # 만약 현재 수가 이미 멀티탭에 존재한다면 패스
    if li[i] in multitap:
        continue
    # 현재수가 멀티탭에 존재하지 않고, 구멍이 비어있다면
    if len(multitap) < n:
        multitap.append(li[i])
        continue
    # 멀티탭에 존재하지 않지만, 빈 구멍이 없다면
    far = 0
    temp = 0
    for j in multitap:
        # 앞으로 사용 해야 할 리스트에 없으면
        if j not in li[i:]:
            temp = j
            break
        # 
        elif li[i:].index(j) > far:
            far = li[i:].index(j)
            temp = j
    
    multitap[multitap.index(temp)] = li[i]
    cnt += 1
        
print(cnt)