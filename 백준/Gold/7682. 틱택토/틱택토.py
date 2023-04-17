import sys
input = sys.stdin.readline

def checkWin(game, win):
  if game[0]==game[1]==game[2]==win:
    return True
  if game[3]==game[4]==game[5]==win:
    return True
  if game[6]==game[7]==game[8]==win:
    return True
  if game[0]==game[3]==game[6]==win:
    return True
  if game[1]==game[4]==game[7]==win:
    return True
  if game[2]==game[5]==game[8]==win:
    return True
  if game[0]==game[4]==game[8]==win:
    return True
  if game[2]==game[4]==game[6]==win:
    return True
  return False

while True:
  game = input().rstrip()
  if game == 'end':
    break
  x_cnt = game.count('X')
  o_cnt = game.count('O')
  
  if checkWin(game, 'X') and not checkWin(game, 'O') and x_cnt == o_cnt + 1:
    print('valid')
  elif checkWin(game, 'O') and not checkWin(game, 'X') and x_cnt == o_cnt:
    print('valid')
  elif not checkWin(game, 'O') and not checkWin(game, 'X') and x_cnt == 5 and o_cnt == 4:
    print('valid')
  else:
    print('invalid')

