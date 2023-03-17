N = list(input())
N.sort(reverse=True)
sum = 0
# 입력 값에 0이 없으면 -1() -> 30의 배수가 아니기 때문에
if '0' not in N:
  print(-1)
# 각 자리의 숫자들을 더했을 때 3의 배수여야 함 -> 3의 배수가 되려면
else:
  for i in N:
    sum += int(i)
  if sum % 3 != 0:
    print(-1)
  else:
    print("".join(N))