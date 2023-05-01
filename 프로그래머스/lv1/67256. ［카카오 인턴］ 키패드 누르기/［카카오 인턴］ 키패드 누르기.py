def solution(numbers, hand):
    answer = ''

    key = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    left = key['*']
    right = key['#']
    
    for i in numbers:
        temp = key[i]
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = temp
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = temp
        else:
            l = abs(left[0]- temp[0]) + abs(left[1]- temp[1])
            r = abs(right[0]- temp[0]) + abs(right[1]- temp[1])
            
            if l < r:
                answer += 'L'
                left = temp
            elif l > r:
                answer += 'R'
                right = temp
            elif l == r:
                if hand == 'right':
                    answer += 'R'
                    right = temp
                else:
                    answer += 'L'
                    left = temp
                    
    return answer