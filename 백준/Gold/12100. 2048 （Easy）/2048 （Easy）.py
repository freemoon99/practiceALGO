import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def rotated(board):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = board[i][j]
    return temp

def get_max(board):
    max_value = 0
    for i in range(n):
        for j in range(n):
            if max_value < board[i][j]:
                max_value = board[i][j]
    return max_value

def move(board):
    for j in range(n):
        idx = 0
        for i in range(n):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if board[idx][j] == 0:
                    board[idx][j] = temp
                elif board[idx][j] == temp:
                    board[idx][j] *= 2
                    idx += 1
                else:
                    idx += 1
                    board[idx][j] = temp
    return board

def dfs(board, count):
    global ans
    if count == 5:
        ans = max(ans, get_max(board))
        return
    for _ in range(4):
        dfs(move(copy.deepcopy(board)), count+1)
        board = rotated(board)

dfs(grid, 0)
print(ans)
