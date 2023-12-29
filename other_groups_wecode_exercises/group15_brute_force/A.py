n, m, k = [int(x) for x in input().split(" ")]
board = [[0 for i in range(m)] for j in range(n)]


def check(x, y):
    if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] * board[x - 1][y] * board[x][y - 1] * board[x][y] == 1: return True
    if x - 1 >= 0 and y + 1 < m and board[x - 1][y + 1] * board[x - 1][y] * board[x][y + 1] * board[x][y] == 1: return True
    if x + 1 < n and y - 1 >= 0 and board[x + 1][y - 1] * board[x + 1][y] * board[x][y - 1] * board[x][y] == 1: return True
    if x + 1 < n and y + 1 < m and board[x + 1][y + 1] * board[x + 1][y] * board[x][y + 1] * board[x][y] == 1: return True
    return False


def main():
    for d in range(k):
        i, j = [int(x) for x in input().split(" ")]
        board[i - 1][j - 1] = 1
        if check(i - 1, j - 1):
            print(d + 1)
            return
            
    print(0)
            
main()