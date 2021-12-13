import pprint
pp = pprint.PrettyPrinter(depth=6)

# Parse input
f = open("04/input.txt", "r")
lines = [line.rstrip('\n') for line in f]
draws = lines[0].split(',')
boards = []
boardLine = 0
for line in lines[2:]:
    if (line == ''):
        continue
    if boardLine == 0 or boardLine == 5:
        boards.append([])
        boardLine = 0
    if boardLine < 5:
        boards[len(boards)-1].append(line.split())
        boardLine += 1

# Part 1
def isWin(board):
    for row in board:
        if all(cell=='x' for cell in row):
            return True
    for col in range(0,5):
        if all(board[row][col]=='x' for row in range(0,5)):
            return True
        if all(board[col][row]=='x' for row in range(0,5)):
            return True
    return False

def findBestBoard():
    for draw in draws:
        for board in boards:
            for row in range(0,5):
                for col in range(0,5):
                    if board[row][col] == draw:
                        board[row][col] = 'x'
            if isWin(board):
                return [draw, board]

def getUnmarkedSum(board):
    score = 0
    for row in board:
        for cell in row:
            if (cell != 'x'):
                score += int(cell)
    return score

[draw, board] = findBestBoard()
pp.pprint(board)
print(getUnmarkedSum(board) * int(draw))

# Part 2
def findWorstBoard():
    remainingBoards = range(0, len(boards))
    for draw in draws:
        for board in list(boards):
            for row in range(0,5):
                for col in range(0,5):
                    if board[row][col] == draw:
                        board[row][col] = 'x'
            if isWin(board):
                if (len(boards) == 1):
                    return [draw, board]
                boards.remove(board)

[draw, board] = findWorstBoard()
pp.pprint(board)
print(getUnmarkedSum(board) * int(draw))