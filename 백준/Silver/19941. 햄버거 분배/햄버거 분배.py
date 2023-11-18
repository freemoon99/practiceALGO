n, k = map(int, input().split())
line = list(input())
ans = 0

for i in range(n):
    if line[i] == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if line[j] == 'H':
                line[j] = 0
                ans += 1
                break

print(ans)
