import random
import sys

'''
    Changes from part 1:
    I put appropriate names for certain variables.
    (ex: puzzle -> board)
    Cleaner code
'''
# 1: function tileLabels: arguments(n) returns(list of strings 1 to (n^2-1)'  ')
def tileLabels(n):

    labels = []
    for i in range(1, n * n):
        if i < 10:
            labels.append(str(i) + ' ')
        else:
            labels.append(str(i))
    labels.append('  ')
    return labels

#2: function getNewPuzzle argument(n), returns(n*n puzzles ready) LIST OF SUBLISTS
def getNewPuzzle(n):
    
    labels = tileLabels(n)
    random.shuffle(labels)
    board = []
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(labels[i * n + j])
        board.append(row)
    
    return board

# 3: function findEmptyTile argument(puzzle) returns(row_number, column_number)
def findEmptyTile(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '  ':
                return (i, j)
            
# 4: board as argument, determines and returns the next move selon le input
def nextMove(board):
    
    n = len(board)
    empty_row, empty_col = findEmptyTile(board)
    valid_moves = {}
    
    if empty_row > 0:
        valid_moves['W'] = "(W)"
    if empty_row < n - 1:
        valid_moves['S'] = "(S)"
    if empty_col > 0:
        valid_moves['A'] = "(A)"
    if empty_col < n - 1:
        valid_moves['D'] = "(D)"
    
    while True:
        print("Enter WASD (or QUIT):", " ".join(valid_moves.values()))
        move = input("> ").upper()
        if move == "QUIT":
            sys.exit("Game exited.")
        if move in valid_moves:
            return move
        print("Invalid move. Try again.")


# 5: 2 arguments(board, next move)
def makeMove(board, move):
    # Updates the board with the move made by the user
    empty_row, empty_col = findEmptyTile(board)
    
    if move == 'W':
        board[empty_row][empty_col], board[empty_row - 1][empty_col] = board[empty_row - 1][empty_col], board[empty_row][empty_col]
    elif move == 'S':
        board[empty_row][empty_col], board[empty_row + 1][empty_col] = board[empty_row + 1][empty_col], board[empty_row][empty_col]
    elif move == 'A':
        board[empty_row][empty_col], board[empty_row][empty_col - 1] = board[empty_row][empty_col - 1], board[empty_row][empty_col]
    elif move == 'D':
        board[empty_row][empty_col], board[empty_row][empty_col + 1] = board[empty_row][empty_col + 1], board[empty_row][empty_col]


# teacher's code to display
def displayBoard(board_lst):
    
    n = len(board_lst)
    labels = []
    
    for row in board_lst:
        for tile in row:
            labels.append(tile)
    
    draw_board = ''
    horizontal_div = ('+' + '------') * n + '+'
    vertical_div = '|' + ' ' * 6
    vertical_label = '|' + ' ' * 2 + '{}' + ' ' * 2
    
    for i in range(n):
        draw_board += horizontal_div + '\n' + vertical_div * n + '|\n' + vertical_label * n + '|\n' + vertical_div * n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

# additional function to check if board is in solved state
def isSolved(board):
    
    n = len(board)
    solved_labels = tileLabels(n)
    expected_board = []
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(solved_labels[i * n + j])
        expected_board.append(row)
    
    return board == expected_board


# 6 main program - runs thegame, had the appropriate messages, etc
def main():
    """Main function to run the game."""
    print("Welcome to the Sliding Puzzle Game!")
    n = int(input("Enter board size (n x n, n > 2): "))
    while n <= 2:
        print("Invalid size. n must be greater than 2.")
        n = int(input("Enter board size (n x n, n > 2): "))
    
    board = getNewPuzzle(n)
    moves = 0
    max_moves = 31 if n == 3 else 80
    
    while moves < max_moves:
        displayBoard(board)
        if isSolved(board):
            print("Congratulations! You solved the puzzle!")
            return
        
        move = nextMove(board)
        makeMove(board, move)
        moves += 1
    
    print("Best of luck next time!")


'''
# testing variables

# Board for testing (3x3)
test_board = [
    ['3 ', '  ', '8 '], 
    ['1 ', '5 ', '2 '], 
    ['6 ', '4 ', '7 ']
]

# Board for testing (4x4)
test_board_4x4 = [
    ['  ', '2 ', '3 ', '4 '], 
    ['5 ', '6 ', '7 ', '8 '], 
    ['9 ', '10', '11', '12'], 
    ['13', '14', '15', '1 ']
]

print(tileLabels(3))  
print(tileLabels(4))

random_board = getNewPuzzle(3)
displayBoard(random_board)  

print(findEmptyTile(test_board))   # Expected: (0,1)
print(findEmptyTile(test_board_4x4))  # Expected: (0,0)


move = nextMove(test_board)  # 'W', 'A', 'S', 'D' 
print("Move chosen:", move)

print("Before Move:")
displayBoard(test_board)

makeMove(test_board, 'S')  # Moves '5 ' into empty space

print("After Move:")
displayBoard(test_board)  # Expected: Empty tile should swap places with '5 '


solved_board = [
    ['1 ', '2 ', '3 '], 
    ['4 ', '5 ', '6 '], 
    ['7 ', '8 ', '  ']
]
print(isSolved(test_board))  # Expected: False
print(isSolved(solved_board))  # Expected: True


'''