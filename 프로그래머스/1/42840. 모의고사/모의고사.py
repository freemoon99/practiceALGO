def solution(answers):
    candidates = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    cnt = [0,0,0]
    
    for idx, ans in enumerate(answers):
        if ans == candidates[0][idx%5]:
            cnt[0] += 1
        if ans == candidates[1][idx%8]:
            cnt[1] += 1
        if ans == candidates[2][idx%10]:
            cnt[2] += 1
                
    max_value = max(cnt)
    result = []
    for i in range(3):
        if cnt[i] == max_value:
            result.append(i+1)
            
    return result