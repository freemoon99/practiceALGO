import math
def solution(progresses, speeds):
    answer = []
    days = []
    # 몇일 뒤에 완성되는지 확인
    for i in range(len(speeds)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    # 해당 기능 이전에 완성된 것(앞에 숫자가 더 큰지)이 있는지 확인
    print(days)
    
    front = 0
    for back in range(len(speeds)):
        if days[front] < days[back]:
            answer.append(back-front)
            front = back

    answer.append(len(speeds) - front)
        
    return answer