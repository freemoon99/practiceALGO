def solution(sizes):
    answer = 0
    max_size = 0
    min_size = 1e9
    
    for x, y in sizes:
        if max_size < max(x, y):
            max_size = max(x, y)
        if min_size > min(x, y):
            min_size = min(x,y)
    
    for i, j in sizes:
        if (i < max_size and j < min_size) or (j < max_size and i < min_size):
            continue
        else:
            if min_size < min(i, j):
                min_size = min(i, j)
    
    
    answer = min_size * max_size
    return answer