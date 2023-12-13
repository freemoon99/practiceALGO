def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    row = 0 # 노란색의 줄의 갯수
    while True:
        row += 1
        col = yellow // row
        
        if col == 0:
            break
        
        if brown == row*2 + col*2 + 4:
            if row >= col:
                if area == (row+2)*(col+2):
                    answer.append([row+2, col+2])
        
    return answer[0]