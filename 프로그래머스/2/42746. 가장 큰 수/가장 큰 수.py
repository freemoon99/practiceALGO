def solution(numbers):
    ans = []
    for i in numbers:
        ans.append(str(i))
    
    ans.sort(key = lambda x: x*11, reverse = True)
    
    answer = int("".join(ans))
    return str(answer)