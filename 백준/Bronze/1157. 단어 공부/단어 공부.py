import sys
input = sys.stdin.readline

str = input().strip().upper()
_str = list(set(str))

cnt = []
for i in _str:
  cnt.append(str.count(i))
  
if cnt.count(max(cnt)) > 1:
  print("?")
  
else:
  print(_str[cnt.index(max(cnt))])