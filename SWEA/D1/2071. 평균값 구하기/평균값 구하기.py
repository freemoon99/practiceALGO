T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))

    ans = round(sum(numbers)/len(numbers))

    print(f"#{test_case} {ans}")