def solution(sequence, k):
    INF = int(1e9)
    answer = [[0,INF]]
    right = 0
    cnt = 0
    for left in range(len(sequence)):
        while cnt < k and right < len(sequence):
            cnt += sequence[right]
            right += 1
        if cnt == k:
            if (right-1-left) < (answer[0][1]-answer[0][0]):
                answer[0] = (left, right-1)
        cnt -= sequence[left]
    return answer[0]