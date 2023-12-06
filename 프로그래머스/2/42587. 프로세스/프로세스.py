from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])
    
    while q:
        now = q.popleft()
        
        if q and max(q)[0] > now[0]:
            q.append(now)
        else:
            answer += 1
            if location == now[1]:
                break
    
    return answer