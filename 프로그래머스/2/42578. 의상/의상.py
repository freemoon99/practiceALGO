from collections import defaultdict

def solution(clothes) -> int:
    answer = 1
    dic = defaultdict(list)
    
    for i in clothes:
        name, category = i
        dic[category].append(name)
    
    if len(dic.keys()) == 1:
        return len(clothes)
    
    for k in dic.keys():
        answer *= len(dic[k]) + 1
    
    return answer - 1