def solution(s):
    answer = 0
    dic = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i in dic:
        s = s.replace(i, str(dic.index(i)))

    return int(s)