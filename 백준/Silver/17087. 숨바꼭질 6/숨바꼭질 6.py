import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N, S = map(int, input().split())
li = list(map(int, input().split()))
distance = []

for i in li:
    x = abs(S - i)
    distance.append(x)

ans = distance[0]
for i in range(1, N):
    ans = gcd(distance[i], ans)
print(ans)
