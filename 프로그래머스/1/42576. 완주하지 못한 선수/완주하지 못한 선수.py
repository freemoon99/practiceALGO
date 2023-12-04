from collections import defaultdict
def solution(participant, completion):
    answer = ''
    dic = defaultdict(int)
    
    for i in participant:
        dic[i] += 1
    
    for j in completion:
        dic[j] -= 1
        
    for k, v in dic.items():
        if v == 1:
            answer = k
        
    return answer