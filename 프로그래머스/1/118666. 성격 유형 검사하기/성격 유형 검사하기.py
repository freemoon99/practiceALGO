def solution(survey, choices):
    answer = ''
    n = len(survey)
    
    persnal = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0,
    }
    choose = {
        1 : 3,
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2,
        7 : 3
    }
    
    for i in range(n):
        if choices[i] < 4:
            persnal[survey[i][0]] += choose[choices[i]]
        elif choices[i] > 4:
            persnal[survey[i][1]] += choose[choices[i]]
    
    persnal_keys = list(persnal.keys())
    persnal_left = persnal_keys[::2]
    persnal_right = persnal_keys[1::2]
        
    for i in range(4):
        left = persnal[persnal_left[i]]
        right = persnal[persnal_right[i]]
        
        if right > left:
            answer += persnal_right[i]
        else:
            answer += persnal_left[i]
            
    return answer