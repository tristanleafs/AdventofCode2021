import copy

#checks boards and returns unchecked items sum
def checkBoard(board, currentDraws):
    newBoard = copy.deepcopy(board)
    
    for i in range(len(currentDraws)):
        for row in range(5):
            for col in range(5):
                if(board[row][col] == currentDraws[i]):
                    newBoard[row][col] = 0

    #check rows
    done = False
    for row in range(5):
        if(newBoard[row][0] == 0 and newBoard[row][1] == 0 and newBoard[row][2] == 0 and newBoard[row][3] == 0 and newBoard[row][4] == 0):
            done = True
        elif(newBoard[0][row] == 0 and newBoard[1][row] == 0 and newBoard[2][row] == 0 and newBoard[3][row] == 0 and newBoard[4][row] == 0):
            done = True
    
    sum = 0
    for row in range(5):
        for col in range(5):
            sum += newBoard[row][col]
    
    return done, sum



draws = []
boards = []
with(open("data4.txt") as f):
    draws = [int(s) for s in f.readline().split(sep= ",")]

    
    while(f.readline()):
        board = []
        for i in range(5):
            
            board.append([int(s) for s in f.readline().split()])
        boards.append(board)

shitBoard = []
for row in range(5):
    shitBoard.append([])
    for col in range(5):
        shitBoard[row].append(-1)

currentDraws = []
finalDone = False
finalSum = 0
finalDraw = 0
for draw in draws:
    currentDraws.append(draw)
    for count, board in enumerate(boards):
        [done,sum] = checkBoard(board, currentDraws)
        if(done): 
            boards[count] = copy.deepcopy(shitBoard)
            finalSum = sum
            finalDraw = draw
    

print("sum",finalSum)
print("draw", finalDraw)
print("ans", finalSum*finalDraw)


    





