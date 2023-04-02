import sys
input = sys.stdin.readline

from string import ascii_lowercase

alphabet_dict = {}

for i in ascii_lowercase:
	alphabet_dict[i] = -1

S = input().strip()

for i in S:
  alphabet_dict[i] = S.index(i)

ans = []

for j in alphabet_dict.values():
  ans.append(j)
  
print(*ans)