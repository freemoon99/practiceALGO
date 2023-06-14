import sys
input = sys.stdin.readline

money = int(input())
price = list(map(int, input().split()))

# 준현
def bnp(m):
  leave_money = m
  cnt = 0

  for i in price:
    if leave_money//i > 0:
      cnt += (leave_money//i)
      leave_money -= i*(leave_money//i)
    else:
      continue
  final_money = cnt*price[-1] + leave_money
  
  return final_money

#성민
def timing(m):
  leave_money = m
  cnt = 0
  
  for i in range(len(price)):
    # 모든 거래는 전량 매도, 전량 매수
    # 조건에서 3일 연속이므로 적어도 이전에 값이 3개 이상 있어야 함
    if i > 2:
      # 3일 연속 상승 -> 전량 매도
      if price[i]>price[i-1] and price[i-1]>price[i-2] and price[i-2]>price[i-3]:
        leave_money += cnt*price[i]
        cnt = 0
      # 3일 연속 하락 -> 전량 매수
      if price[i]<price[i-1] and price[i-1]<price[i-2] and price[i-2]<price[i-3]:
        if leave_money//price[i] > 0:
          cnt += (leave_money//price[i])
          leave_money -= price[i]*(leave_money//price[i])
    else:
      continue
  final_money = cnt*price[-1] + leave_money
  
  return final_money

if bnp(money) > timing(money):
  print("BNP")
elif bnp(money) < timing(money):
  print("TIMING")
elif bnp(money) == timing(money):
  print("SAMESAME")