import sys
input = sys.stdin.readline

str = list(input())
_str = []
for i in str:
    if i.isupper():
        _str.append(i.lower())
    else:
        _str.append(i.upper())

print(''.join(_str))