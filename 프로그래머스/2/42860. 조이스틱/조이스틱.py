def solution(name):
    answer = 0
    change_alpha = 0
    change_cursor = len(name)-1 # 무작정 오른쪽으로만 이동하는 값
    
    for i, alpha in enumerate(name):
        # 알파벳 변경에 걸리는 횟수 저장 (왼쪽 이동, 오른쪽 이동 비교)
        change_alpha += min(ord(alpha)-ord('A'), ord('Z')-ord(alpha)+1)

        # 전체 커서 이동
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        
        change_cursor = min(change_cursor, i*2+(len(name)-idx), i+2*(len(name)-idx))
        
    answer = change_alpha+change_cursor
    return answer