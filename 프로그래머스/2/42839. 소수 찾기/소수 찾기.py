from itertools import permutations

def solution(numbers):
    answer = 0
    nums = list(numbers)
    candidates = set()
    
    for i in range(1, len(nums)+1):
        for j in permutations(nums, i):
            candidates.add(int("".join(j)))
    
    max_value = max(candidates)
    
    # 소수 판별 : 에라토스테네스...?
    prime = [False]+[False]+[True]*(max_value+1)
    for i in range(2, max_value+1):
        if prime[i]:
            for j in range(2*i, max_value+1, i):
                prime[j] = False
    
    for cand in candidates:
        if prime[cand]:
            answer += 1
            
    return answer