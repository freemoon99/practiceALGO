def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr.pop(0))
    for i in range(len(arr)):
        if arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])
    
    return answer