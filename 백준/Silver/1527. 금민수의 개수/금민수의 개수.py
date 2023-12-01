from itertools import product

a, b = map(int, input().split())
max_len = max(len(str(a)), len(str(b)))
ans = 0

candidate = []

for i in range(max_len + 1):
    for j in product('47', repeat=i):
        if j:
            candidate.append(int("".join(map(str, j))))

for num in candidate:
    if a<= num <= b:
        ans += 1

print(ans)
