import sys
input = sys.stdin.readline

k = int(input())
weights = list(map(int, input().split()))
s = sum(weights)

candidates = [weights[0]]

for i in range(1, k):
  curr = weights[i]
  temp = [curr]
  for e in candidates:
    temp += [curr+e, abs(curr-e)]
    
  candidates += temp
  
candidates = list(set(candidates))

if 0 in candidates:
  candidates.remove(0)

ans = s-len(candidates)

print(ans)