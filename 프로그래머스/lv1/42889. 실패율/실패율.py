def solution(N, stages):
    answer = []
    cnt = [0 for _ in range(N+2)]
    fail = [0 for _ in range(N+1)]
    for s in stages:
        cnt[s] += 1
        
    player = len(stages)
    for i in range(N+1):
        fail_rate = cnt[i]/player if player > 0 else 0
        fail[i] = (fail_rate, i)
        player -= cnt[i]
    
    fail.sort(reverse=True, key = lambda x: (x[0], -x[1]))
    
    for i in fail:
        answer.append(i[1])
    answer.remove(0)

    return answer