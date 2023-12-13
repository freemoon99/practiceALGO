from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    
    candidates = list(permutations(dungeons, n))
    
    for cand in candidates:
        now = k
        cnt = 0
        for m, u in cand:
            if now >= m:
                now -= u
                cnt += 1
                
        answer = max(answer, cnt)
            
    return answer