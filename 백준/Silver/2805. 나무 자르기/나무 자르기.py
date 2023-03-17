N, M = map(int, input().split())
H = list(map(int, input().split()))

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        res = 0
        # 나무가 기준 값보다 클 때
        for tree in H:
          if tree > mid:
            res += tree - mid
        # 시작점, 끝점 조작
        if res < M:
          end = mid - 1
        else:
          start = mid + 1
    return end

# 이진 탐색 수행 결과 출력
result = binary_search(1, max(H))

print(result)