from collections import deque
n = int(input())
problem = list(map(str, input()))
numbers = [int(input()) for _ in range(n)]
result = []
# 알파벳이면 결과에 추가
# 연산자이면 결과에서 뒤에 2개 뽑아서 계산하여 다시 추가
# A부터 순서대로 이므로 -64 하면 A=0, B=1, ... 로 인덱스가 구해짐
t = len(problem)

for i in problem:
    if i.isalpha():
        result.append(numbers[ord(i)-65])
    else:
        # 종료 조건 : result의 갯수가 1개 일 때
        num2 = float(result.pop())
        num1 = float(result.pop())
        if i == '+':
            temp = num1 + num2
            result.append(temp)
        if i == '-':
            temp = num1 - num2
            result.append(temp)
        if i == '*':
            temp = num1 * num2
            result.append(temp)
        if i == '/':
            temp = num1 / num2
            result.append(temp)

print('{:.2f}'.format(result[-1]))
