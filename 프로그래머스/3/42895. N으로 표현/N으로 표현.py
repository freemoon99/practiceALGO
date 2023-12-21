def solution(N, number):
    answer = -1
    MAX_VALUE = 9
    dp = []
    
    if N == number:
        return 1

#     두 수 사이에 연산자 넣기..? -> 연산자 한개
    for i in range(1, MAX_VALUE):
        temp_set = set()
        temp_set.add(int(str(N)*i))
        
        for j in range(i-1):
            for num1 in dp[j]:
                for num2 in dp[-j-1]:
                    temp_set.add(num1+num2)
                    temp_set.add(num1-num2)
                    temp_set.add(num1*num2)
                    if num2 != 0:
                        temp_set.add(num1//num2)
        
            
        if number in temp_set:
            answer = i
            break
        
        dp.append(temp_set)
                
    return answer