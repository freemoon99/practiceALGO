from typing import List

def solution(nums:List[int]) -> int:
    a = len(nums)//2
    b = len(set(nums))
    
    return min(a, b)