T = 1
for test_case in range(1, T + 1):
    n = int(input())
    ans = ""
    for i in range(1, n + 1):
        num = str(i)
        change = num.count('3')+num.count('6')+num.count('9')

        if change > 0:
            ans += "-"*change + " "
        else:
            ans += num+" "

    print(ans)
