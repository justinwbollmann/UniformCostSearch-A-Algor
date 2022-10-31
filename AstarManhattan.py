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



def aStarManhattan(array):
    numNodesExpand2 = 0
    maxQ3 = 1
    unknown3 = []
    known3 = []
    keepGoing3 = False
    endState3 = [1,2,3,4,5,6,7,8,0]
    levelAStarManhattan = 0
    tracker3 = 0
    #creating sequence with range function for 9-digits [0-8]
    #Reference: https://www.w3schools.com/python/ref_func_range.asp 
    #Creating our tracker to check where we are node-wise
    for x in range(9):
        #Reference: https://www.geeksforgeeks.org/sum-manhattan-distances-pairs-points/
        xValue = array.index(x)
        yValue = []
        #generates x value for each tile
        yValue.append(math.floor(xValue/3)) 
        #generates y value for each tile
        #We use modulus operand to find the coordinate location of each tile
        yValue.append(xValue%3) 
        xValueEnd = endState3.index(x)
        yValueEnd = []
        #generates another x value for each tile
        yValueEnd.append(math.floor(xValueEnd/3)) 
        #generates another y value for each tile
        #We use modulus operand to find the coordinate location of each tile
        yValueEnd.append(xValueEnd%3) 
        #Keeps track of our depth in nodes known to us
        levelAStarManhattan += math.sqrt(pow(yValueEnd[0] - yValue[0], 2) + pow(yValueEnd[1] - yValue[1], 2))
   
    unknown3.append((levelAStarManhattan, tracker3, node(array, None)))
    weKnow3 = False

    while not keepGoing3:
        if(len(unknown3) > maxQ3):
            maxQ3 = len(unknown3)
        if len(unknown3) == 0:
            print("Unknown.")
            keepGoing3 = True
        elif unknown3[0][2].input == endState3:
            print("Solution depth was: " + str(howDeep(unknown3[0][2])))
            print("Nodes expanded: " + str(numNodesExpand2))
            print("Max queue size: " + str(maxQ3))
            print(unknown3[0][2].input[0:3])
            print(unknown3[0][2].input[3:6])
            print(unknown3[0][2].input[6:9])
            print("Goal State!")
            keepGoing3 = True
        else:
            numNodesExpand2 += 1
            order = []
            order = unknown3[0][2].input[:]
            print("Unknown")
            for x in unknown3:
                print(x[2].input)

            #Swaps bottom row to other row
            if not 0 in unknown3[0][2].input[6:9]: 
                #copy above value south to blank 
                order[unknown3[0][2].empty] = unknown3[0][2].input[unknown3[0][2].empty + 3] 
                order[unknown3[0][2].empty + 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known3:
                    if order == x.input:
                        #halts if node is already known
                        weKnow3 = True
                #check if node is unknown
                if not weKnow3:
                    levelAStarManhattan = 0
                    for x in range(9):
                        xValue = order.index(x)
                        yValue = []
                        #generates x value for each tile
                        yValue.append(math.floor(xValue/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValue.append(xValue%3) 
                        xValueEnd = endState3.index(x)
                        yValueEnd = []
                        #generates x value for each tile
                        yValueEnd.append(math.floor(xValueEnd/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValueEnd.append(xValueEnd%3) 
                        #Keeps track of our depth in nodes known to us
                        levelAStarManhattan += math.sqrt(pow(yValueEnd[0] - yValue[0], 2) + pow(yValueEnd[1] - yValue[1], 2))
                    tracker3 += 1 #increases our depth of the node known to us
                    level =  howDeep(unknown3[0][2]) + 1
                    levelAStarManhattan += level
                    unknown3.append((levelAStarManhattan, tracker3, node(order, unknown3[0][2]))) 

                weKnow3 = False
                print(order)
                order = unknown3[0][2].input[:]


            #Swaps top row to other row
            if not 0 in unknown3[0][2].input[0:3]: 
                #copy above value north to blank
                order[unknown3[0][2].empty] = unknown3[0][2].input[unknown3[0][2].empty - 3] 
                order[unknown3[0][2].empty - 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known3:
                    if order == x.input:
                        #halts if node is already known
                        weKnow3 = True
                #check if node is unknown
                if not weKnow3:
                    levelAStarManhattan = 0
                    for x in range(9):
                        xValue = order.index(x)
                        yValue = []
                        #generates x value for each tile
                        yValue.append(math.floor(xValue/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValue.append(xValue%3) 
                        xValueEnd = endState3.index(x) 
                        yValueEnd = []
                        #generates another x value for each tile
                        yValueEnd.append(math.floor(yValueEnd/3)) 
                        #generates another y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValueEnd.append(yValueEnd%3) 
                        #Keeps track of our depth in nodes known to us
                        levelAStarManhattan += math.sqrt(pow(yValueEnd[0] - yValue[0], 2) + pow(yValueEnd[1] - yValue[1], 2))
                    tracker3 += 1 #increases our depth of the node known to us
                    level =  howDeep(unknown3[0][2]) + 1
                    levelAStarManhattan += level
                    unknown3.append((levelAStarManhattan, tracker3, node(order, unknown3[0][2]))) 

                weKnow3 = False
                print(order)
                order = unknown3[0][2].input[:]

            #Swap West for columns
            #This selects the columns for the left side
            if not 0 == unknown3[0][2].input[0] and not 0 == unknown3[0][2].input[3] and not 0 == unknown3[0][2].input[6]: 
                #copies the values of the left column
                order[unknown3[0][2].empty] = unknown3[0][2].input[unknown3[0][2].empty - 1] 
                #empties left column
                order[unknown3[0][2].empty - 1] = 0 
                for x in known3:
                    if order == x.input:
                        weKnow3 = True
                #pastes the left column values into new node pushing into queue
                if not weKnow3:
                    levelAStarManhattan = 0
                    for x in range(9):
                        xValue = order.index(x)
                        yValue = []
                        #generates x value for each tile
                        yValue.append(math.floor(xValue/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValue.append(xValue%3) 
                        xValueEnd = endState3.index(x)
                        yValueEnd = []
                        #generates x value for each tile
                        yValueEnd.append(math.floor(xValueEnd/3)) 
                        #generates y tile for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValueEnd.append(xValueEnd%3) 
                        #Keeps track of our depth in nodes known to us
                        levelAStarManhattan += math.sqrt(pow(yValueEnd[0] - yValue[0], 2) + pow(yValueEnd[1] - yValue[1], 2))
                    tracker3 += 1 #increases our depth of the node known to us
                    level =  howDeep(unknown3[0][2]) + 1
                    levelAStarManhattan += level
                    unknown3.append((levelAStarManhattan, tracker3, node(order, unknown3[0][2]))) 
                
                weKnow3 = False
                print(order)
                order = unknown3[0][2].input[:]


            #Swap East for columns
            #This selects the columns for the right side
            if not 0 == unknown3[0][2].input[2] and not 0 == unknown3[0][2].input[5] and not 0 == unknown3[0][2].input[8]: 
                #Copies the values of the right column
                order[unknown3[0][2].empty] = unknown3[0][2].input[unknown3[0][2].empty + 1] 
                #empties right column
                order[unknown3[0][2].empty + 1] = 0 
                for x in known3:
                    if order == x.input:
                        weKnow3 = True
                #pastes the right column values into new node pushing into queue
                if not weKnow3:
                    levelAStarManhattan = 0
                    for x in range(9):
                        xValue = order.index(x)
                        yValue = []
                        #generates x value for each tile
                        yValue.append(math.floor(xValue/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValue.append(xValue%3) 
                        xValueEnd = endState3.index(x)
                        yValueEnd = []
                        #generates x value for each tile
                        yValueEnd.append(math.floor(xValueEnd/3)) 
                        #generates y value for each tile
                        #We use modulus operand to find the coordinate location of each tile
                        yValueEnd.append(xValueEnd%3) 
                        #Keeps track of our depth in nodes known to us
                        levelAStarManhattan += math.sqrt(pow(yValueEnd[0] - yValue[0], 2) + pow(yValueEnd[1] - yValue[1], 2))
                    tracker3 += 1 #increases our depth of the node known to us
                    level =  howDeep(unknown3[0][2]) + 1
                    levelAStarManhattan += level
                    unknown3.append((levelAStarManhattan, tracker3, node(order, unknown3[0][2]))) 
                weKnow3 = False
                print(order)
        
        known3.append(unknown3[0][2])
        unknown3.pop(0)
        unknown3.sort()


array = [1,0,3,4,2,6,7,5,8]
aStarManhattan(array)
