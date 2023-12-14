def solution(number, k):
    answer = ''
    temp = []
    
    for num in number:
        while temp:
            if temp[-1] < num and k > 0:
                temp.pop()
                k -= 1
            else:
                break
            
        temp.append(num)
    
    while len(temp) > len(number)-k:
        temp.pop()
    
    for i in temp:
        answer += i
    
    return answer