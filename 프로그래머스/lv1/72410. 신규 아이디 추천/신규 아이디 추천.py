import re
def solution(new_id):
    answer = ''
#     1단계
    first = new_id.lower()
#     2단계(정규식으로 제외)
    second = re.sub(r"[^a-z0-9-_.]","",first)
#     3단계
    third = re.sub('(([.])\\2{1,})',".",second)
#     4단계
    fourth = third
    if third.startswith('.'):
        if third.endswith('.'):
            fourth = third[1:-1]
        else:
            fourth = third[1:]
    elif third.endswith('.'):
        fourth = third[:-1]
#     5단계 
    if len(fourth) == 0:
        fifth = 'a'
    else:
        fifth = fourth
#     6단계
    sixth = fifth
    if len(fifth) >= 16:
        sixth = fifth[:15]
        if sixth.endswith('.'):
            sixth = sixth[:-1]    
#     7단계
    last = sixth[-1]
    if len(sixth) < 3:
        seventh = sixth + (last)*3
        seventh = seventh[:3]
    else:
        seventh = sixth
        
    return seventh