# Nicole Slanina 2332374
import random
# 1: function tileLabels: arguments(n) returns(list of strings 1 to (n^2-1)'  ')

def tileLabels(n):
    tiles = []
    for i in range(1, (n**2-1)):
        tiles.append(str(i))
    tiles.append('  ')
   
    return tiles


#2: function getNewPuzzle argument(n), returns(n*n puzzles ready) LIST OF SUBLISTS

''' def getNewPuzzle(n):
    puzzle = []
    tiles = tileLabels(n)
    random.shuffle(tiles)
    for i in range(0, n):
        sublist = []
        for i in range(0, n):
            sublist.append(tiles[i])
            if len(sublist[i]) == 1:
                sublist[i] += ' '
        puzzle.append(sublist)
    
    print(puzzle)
'''

# getNewPuzzle(3)

# 3: function findEmptyTile argument(puzzle) returns(row_number, column_number)

def findEmptyFile(puzzle):
    for row in range(len(puzzle)):
        for column in range(len(puzzle)):
            if puzzle[row][column] == '  ':
                return(row, column)
        

# 4:

''' def nextMove(puzzle):
    empty = findEmptyFile(puzzle)
    n = len(puzzle)
    possible = []


'''
