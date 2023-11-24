n = int(input())
for _ in range(n):
    a, b = map(str, input().split(" "))
    a = int(a, 2)
    b = int(b, 2)

    c = bin(a+b)
    print(c[2:])