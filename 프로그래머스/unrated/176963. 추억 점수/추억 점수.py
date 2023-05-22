def solution(name, yearning, photo):
    answer = []
    dic = {name[i]: yearning[i] for i in range(len(name))}
    
    for ele in photo:
        cnt = 0
        for i in ele:
            if i not in dic:
                cnt += 0
            else:
                cnt += dic[i]
        answer.append(cnt)
        
    return answer