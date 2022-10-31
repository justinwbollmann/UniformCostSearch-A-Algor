import math

class node:
    def __init__(self, array, previous):
        self.input = array[:]
        self.empty = array.index(0)
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.previous = previous

def howDeep(node):
    level = 0
    keepGoing3 = True
    while keepGoing3:
        if(node.previous == None):
            keepGoing3 = False
        else:
            level +=1
            node = node.previous
    return level



def userInput(array):
    print("Create the puzzle, enter 0 for the blank space.")
    for x in range(9):
        array.append(int(input("Enter a number:")))
    print("Here is your created puzzle:")
    print(array[0:3])
    print(array[3:6])
    print(array[6:9])


print("Welcome to the 8 puzzle solver. Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. Enter the puzzle delimiting the numbers with a space. Type RETURN only when finished. ")
array = []
userInput(array)

selection = (int(input("Select algorithm: (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) the Manhattan Distance Heuristic: ")))

if selection == 1:
    uniformCostSearchAlgo(array)
if selection == 2:
    aStarAlgor(array)

if selection == 3:
    aStarManhattan(array)

