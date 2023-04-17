import sys
input = sys.stdin.readline

li = [list(map(int, input().split())) for _ in range(3)]

def ccw(p1, p2, p3):
  temp = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
  temp = temp - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0]
  
  if temp > 0:
    return 1
  elif temp < 0:
    return -1
  else:
    return 0

print(ccw(li[0], li[1], li[2]))