# Nicole Slanina 2332374
import random
# 1: function tileLabels: arguments(n) returns(list of strings 1 to (n^2-1)'  ')

def tileLabels(n):
    tiles = []
    for i in range(1, (n**2)):
        tiles.append(str(i))
    tiles.append('  ')
   
    return tiles


#2: function getNewPuzzle argument(n), returns(n*n puzzles ready) LIST OF SUBLISTS

def getNewPuzzle(n):

    tiles = tileLabels(n)
    random.shuffle(tiles)

    index = 0
    puzzle = []
    for i in range(0, n):
        sublist = []
        for j in range(0, n):
            if index < len(tiles):
                sublist.append(tiles[index])
                index += 1
            if len(sublist[j]) == 1:
                sublist[j] += ' '
        puzzle.append(sublist)
    
    
    return puzzle




# 3: function findEmptyTile argument(puzzle) returns(row_number, column_number)

def findEmptyTile(puzzle):
    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            if puzzle[row][column] == '  ':
                return(row, column)
puzzle = getNewPuzzle(3)
for row in puzzle:
    print(row)

'''# visualize
empty_tile_position = findEmptyTile(puzzle)
print('Empty tile is at:', empty_tile_position)
'''

# 4:
import sys
def nextMove(puzzle):
    n = len(puzzle)
    empty_row, empty_col = findEmptyTile(puzzle)

    valid_moves = {} # USE DICTIONNARY, make WASD

    if empty_row > 0:
        valid_moves['W'] = '(W)'

    if empty_row < n - 1:
        valid_moves['S'] = '(S)'

    if empty_col > 0:
        valid_moves['A'] = '(A)'

    if empty_col < n - 1:
        valid_moves['D'] = '(D)'

    while True:
        move_lst = []
        for i in ['A', 'S', 'W', 'D']:
            move_lst.append(valid_moves.get(i, '( )'))
      
        move_prompt = move_lst
        print(f'    {move_prompt[0]}')
        
        user_input = input(f'enter WASD (or QUIT): {' '.join(move_prompt[1:])} \n').strip().upper()

        if user_input == 'QUIT':
            print('Game over')
            sys.exit()
        
        elif user_input in valid_moves:
            return user_input
        
        else:
            print('Does not work')
    



def displayBoard(puzzle):
    n = len(puzzle)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(puzzle[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

# testing it
puzzle = getNewPuzzle(3)  

displayBoard(puzzle)



move = nextMove(puzzle) 
if move:
    print(f"User selected move: {move}")
    
else:
    print("Game ended.")
