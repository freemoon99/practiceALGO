def solution(n, lost, reserve):
    # 잃어버렸는데 여분이 있는 학생들 제거
    dup = set(lost) & set(reserve)
    lost = list(set(lost) - dup)
    reserve = list(set(reserve) - dup)
    
    answer = n
    
    lost.sort()
    for j in lost:
        if j-1 in reserve:
            reserve.remove(j-1)
        elif j+1 in reserve:
            reserve.remove(j+1)
        else:
            answer -= 1

    
    return answer