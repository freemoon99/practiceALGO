N = int(input())
li = list(map(int, input().split()))
ans = int(2e9)
left = 0
right = N-1

while left < right:
  plus = li[left] + li[right]
  
  if abs(plus) <= ans:
    i = li[left]
    j = li[right]
    ans = abs(plus)
    
  if plus > 0:
    right -= 1
  else:
    left += 1
    
print(i, j)