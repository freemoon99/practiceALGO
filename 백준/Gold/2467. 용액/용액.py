N = int(input())
li = list(map(int, input().split()))
i, j = 0, 0
left = 0
right = N-1

ans = int(2e9)

while left < right:
  plus = li[left] + li[right]
  
  if abs(plus) <= ans:
    i = li[left]
    j = li[right]
    ans = abs(plus)
    
  if plus <= 0:
    left += 1  
  else:
    right -= 1
    
print(i, j)