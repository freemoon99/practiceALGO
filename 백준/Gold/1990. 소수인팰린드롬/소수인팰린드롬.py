a, b = map(int, input().split())


def is_prime_num(n):
    # 2부터 끝자리 수까지 나누어지지 않으면
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if b > 10000000: b = 10000000

for num in range(a, b + 1):
    if str(num) == str(num)[::-1]:
        if is_prime_num(num):
            print(num)

print(-1)
