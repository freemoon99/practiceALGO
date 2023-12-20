from collections import deque, defaultdict

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    dic = defaultdict(int)
    for i in words:
        dic[i] += 1
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, cnt = q.popleft()
        
        if word == target:
            answer = cnt
            break
        
        for i in range(len(words)):
            same_cnt = 0
            for j in range(len(word)):
                if word[j] != words[i][j]:
                    same_cnt += 1
            
            if same_cnt == 1 and dic[words[i]] != 0:
                q.append([words[i], cnt+1])
                dic[words[i]] = 0
            
    
    
    return answer