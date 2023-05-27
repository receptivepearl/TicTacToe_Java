# main.py
# main.py

import random
# creating grid
grid=[]
for i in range(3):
  rows=[]
  for j in range(3):
    rows.append(" ")
  grid.append(rows)
# printing board
def printing(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if j == 2:
        print(" "+grid[i][j],end='')
      else:
       print(" "+grid[i][j],end=' |')
    print()
    if i!=2:
      print("---+---+---")  
# checks win
def checkWin(board,player):
  # check different combinations
  # check vertical wins
  for i in range(3):
    if board[0][i]==player and board[1][i]==player and board[2][i]==player:
      return True
  # check horizontal wins
  for i in range(3):
    if board[i][0]==player and board[i][1]==player and board[i][2]==player:
      return True 
  # check diagonal
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

 #check tie 
def checkTie(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j]==" ":
        return False
  return True

def testWin(board, player,r,c):
  if board[r][c]!=" ":
    return False
  duplicate=[]
  for i in range(3):
    rows=[]
    for j in range(3):
      rows.append(board[i][j])
    duplicate.append(rows) 
  duplicate[r][c]=player
  return checkWin(duplicate,player)
  
def testFork(board,player,r,c):
  if board[r][c]!=" ":
    return False
  duplicate=[]
  for i in range(3):
    rows=[]
    for j in range(3):
      rows.append(board[i][j])
    duplicate.append(rows) 
  duplicate[r][c]=player
  
  winningMoves=0
  for i in range(len(duplicate)):
    for j in range(len(duplicate[i])):
      if duplicate[i][j]==" ":
        duplicate[i][j]=player
        if checkWin(duplicate,player):
          winningMoves+=1
        duplicate[i][j]=" "
  return winningMoves>1
      
# def randomSpot(board):
#   while True:
#     spots=[[0,1],[1,0],[1,2],[2,1]]
#     random=random.randint(0,3)
#     if spots[random]==" ":
#       return spots[random][0],spots[random][1]
#computer turn 
def computerPlay(board):
  '''
    1)play win
    2)block opponent
    3)fork
    4)block fork
    5)play center
    6)play corner
    7)random
  ''' 
  # play win
  for i in range(len(board)):
    for j in range(len(board[i])):
      if testWin(grid,"O",i,j) != False:
        print("win")
        return i,j
        
  # block opponent
  for i in range(len(board)):
    for j in range(len(board[i])):
      if testWin(grid,"X",i,j) != False:
        print("block")
        return i,j
  # play fork
  for i in range(len(board)):
    for j in range(len(board[i])):
      if testFork(grid,"O",i,j) != False:
        print("fork")
        return i,j
  # block fork
  fork=0
  blockI=-1
  blockJ=-1
  for i in range(len(board)):
    for j in range(len(board[i])):
      if testFork(grid,"X",i,j) != False:
        print("block fork")
        fork+=1
        blockI=i
        blockJ=j
  if fork==2:
    if board[0][1] == ' ':
      return 0,1
    if board[1][0] == ' ':
      return 1, 0
    if board[1][2] == ' ':
      return 1, 2
    if board[2][1] == ' ':
      return 2, 1
  elif fork==1:
    return blockI,blockJ
  # play center
  if board[1][1] == " ":
    print("center")
    return 1,1
  # play corner
  corners=[[0,0],[2,0],[0,2],[2,2]]
  emptyCorners=[]
  for c in corners:
    if board[c[0]][c[1]] == " ":
      emptyCorners.append(c)
  if len(emptyCorners)>0:
    randCorner=random.randint(0,len(emptyCorners)-1)
    print("corner")
    return emptyCorners[randCorner][0],emptyCorners[randCorner][1]
  # play random
  while True:
    computerRow=random.randint(0,2)
    computerCol=random.randint(0,2)
    if board[computerRow][computerCol] == " ":
      print("random")
      return computerRow, computerCol

  
# choosing turn
playerTurn=random.randint(0,1)
turn = "X" if playerTurn==0 else "O"
print("It's player "+turn + "'s turn.  ")
# players choosing spots/check win
while True:
  printing(grid)
  # user's turn
  if turn=="X":
    true=True
    while true:
      userRow=int(input("Choose a row to mark:  "))
      userCol=int(input("Choose a column to mark:  "))
      if(userRow >=0 and userRow<=2) and (userCol >=0 and userCol<=2) and  (grid[userRow][userCol] == " "):
        grid[userRow][userCol]="X"
        true=False
      else:
        print("Not a valid spot")
  else:
    # computer's turn
    computerRow, computerCol = computerPlay(grid)
    grid[computerRow][computerCol]="O"
   
  if checkWin(grid,turn):
    printing(grid)
    print("Player "+turn+" Wins!")
    break
  elif checkTie(grid):
    printing(grid)
    print("It's a tie. There are no more spaces.")
    break
  else:
    turn="O" if turn=="X" else "X"

