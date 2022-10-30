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
    keepGoing = True
    while keepGoing:
        if(node.previous == None):
            keepGoing = False
        else:
            level +=1
            node = node.previous
    return level


#Reference https://www.geeksforgeeks.org/a-search-algorithm/

def aStarAlgor(array):
    numNodesExpand = 0
    maxQ2 = 1
    unknown2 = []
    known2 = []
    keepGoing2 = False
    endState2 = [1,2,3,4,5,6,7,8,0]
    levelAStar = 0
    tracker2 = 0
    #creating sequence with range function for 9-digits [0-8]
    #Reference: https://www.w3schools.com/python/ref_func_range.asp 
    for x in range(9):
        if not array[x] == endState2[x]:
            levelAStar += 1
    unknown2.append((levelAStar, tracker2, node(array, None)))
    weKnow2 = False
    while not keepGoing2:
        if(len(unknown2) > maxQ2):
            maxQ2 = len(unknown2)
        if len(unknown2) == 0:
            keepGoing2 = True
        elif unknown2[0][2].input == endState2:
            print("Solution depth was: " + (str(howDeep(unknown2[0][2]))))
            print("Nodes expanded: " + str(numNodesExpand))
            print("Max queue size: " + str(maxQ2))
            print(unknown2[0][2].input[0:3])
            print(unknown2[0][2].input[3:6])
            print(unknown2[0][2].input[6:9])
            print("Goal State!")
            keepGoing2 = True
        else:
            numNodesExpand += 1
            order = []
            order = unknown2[0][2].input[:]
            for x in unknown2:
                print(x[2].input)

            #Swaps bottom row to other row
            if not 0 in unknown2[0][2].input[6:9]: 
                #copy above value south to blank
                order[unknown2[0][2].empty] = unknown2[0][2].input[unknown2[0][2].empty + 3] 
                order[unknown2[0][2].empty + 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known2:
                    if order == x.input:
                        #halts if node is already known
                        weKnow2 = True
                #check if node is unknown 
                if not weKnow2:
                    levelAStar = 0
                    for x in range(9):
                        if not order[x] == endState2[x]:
                            levelAStar += 1
                    tracker2 += 1
                    level =  howDeep(unknown2[0][2]) + 1
                    levelAStar += level
                    unknown2.append((levelAStar, tracker2, node(order, unknown2[0][2]))) 
                weKnow2 = False
                print(order)
                order = unknown2[0][2].input[:]
                
            #Swaps top row to other row
            if not 0 in unknown2[0][2].input[0:3]: 
                #copy above value noth to blank
                order[unknown2[0][2].empty] = unknown2[0][2].input[unknown2[0][2].empty - 3] 
                order[unknown2[0][2].empty - 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known2:
                    if order == x.input:
                         #halts if node is already known
                        weKnow2 = True
                #check if node is unknown
                if not weKnow2:
                    levelAStar = 0
                    for x in range(9):
                        if not order[x] == endState2[x]:
                            levelAStar += 1
                    tracker2 += 1
                    level =  howDeep(unknown2[0][2]) + 1
                    levelAStar += level
                    unknown2.append((levelAStar, tracker2, node(order, unknown2[0][2]))) 
                weKnow2 = False
                print(order)
                order = unknown2[0][2].input[:]
            
            #Swap East for columns
            #This selects the columns for the right side
            if not 0 == unknown2[0][2].input[2] and not 0 == unknown2[0][2].input[5] and not 0 == unknown2[0][2].input[8]:
                #Copies the values of the right column
                order[unknown2[0][2].empty] = unknown2[0][2].input[unknown2[0][2].empty + 1]
                #empties right column
                order[unknown2[0][2].empty + 1] = 0 
                for x in known2:
                    if order == x.input:
                        weKnow2 = True
                #pastes the left column values into new node pushing into queue
                if not weKnow2:
                    levelAStar = 0
                    for x in range(9):
                        if not order[x] == endState2[x]:
                            levelAStar += 1
                    tracker2 += 1
                    level =  howDeep(unknown2[0][2]) + 1
                    levelAStar += level
                    unknown2.append((levelAStar, tracker2, node(order, unknown2[0][2]))) 
                weKnow2 = False
                print(order)

            
            #Swap West for columns
            #This selects the columns for the left side
            if not 0 == unknown2[0][2].input[0] and not 0 == unknown2[0][2].input[3] and not 0 == unknown2[0][2].input[6]: 
                #copies the values of the left column
                order[unknown2[0][2].empty] = unknown2[0][2].input[unknown2[0][2].empty - 1]
                #empties left column 
                order[unknown2[0][2].empty - 1] = 0 
                for x in known2:
                    if order == x.input:
                        weKnow2 = True
                #pastes the right column values into new node pushing into queue        
                if not weKnow2:
                    levelAStar = 0
                    for x in range(9):
                        if not order[x] == endState2[x]:
                            levelAStar += 1
                    tracker2 += 1
                    level =  howDeep(unknown2[0][2]) + 1
                    levelAStar += level
                    unknown2.append((levelAStar, tracker2, node(order, unknown2[0][2])))
                weKnow2 = False
                print(order)
                order = unknown2[0][2].input[:]


        known2.append(unknown2[0][2])
        unknown2.pop(0)
        unknown2.sort()

array = [1,0,3,4,2,6,7,5,8]
aStarAlgor(array)
