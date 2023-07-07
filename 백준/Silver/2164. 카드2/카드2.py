import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
card = deque(i for i in range(1, n+1))

while len(card)>1:
  card.popleft()
  num = card.popleft()
  card.append(num)
  
print(card[0])