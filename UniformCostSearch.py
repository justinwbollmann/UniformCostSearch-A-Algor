#Implementing Uniform Search
#Reference https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
def uniformCostSearchAlgo(array):
    nodesExpanded = 0
    maxQ = 1
    unknown = []
    known = []
    keepGoing = False
    endState = [1,2,3,4,5,6,7,8,0]
    level = 0
    tracker = 0
    unknown.append((level, tracker, node(array, None)))
    weKnow = False
    
    #keeps track of maxQ
    while not keepGoing:
        if(len(unknown) > maxQ):
            maxQ = len(unknown)
        if len(unknown) == 0:
            print("Unknown.")
            keepGoing = True
        elif unknown[0][2].input == endState:
            print("Nodes expanded: " + str(nodesExpanded))
            print("Max queue: " + str(maxQ))
            print("Solution depth was: " + (str(howDeep(unknown[0][2]))))
            print("Goal State!")
            print(unknown[0][2].input[0:3])
            print(unknown[0][2].input[3:6])
            print(unknown[0][2].input[6:9])
            keepGoing = True
        
        #find data within array node when expanded
        else:
            nodesExpanded += 1
            order = []
            order = unknown[0][2].input[:]
            print("unknown:")
            

            #Swaps bottom row to other row
            if not 0 in unknown[0][2].input[6:9]: 
                #copy above value south to blank
                order[unknown[0][2].empty] = unknown[0][2].input[unknown[0][2].empty + 3] 
                order[unknown[0][2].empty + 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known:
                    if order == x.input:
                        #halts if node is already known
                        weKnow = True
                #check if node is unknown        
                if not weKnow:
                    level =  howDeep(unknown[0][2]) + 1
                    tracker += 1
                    unknown.append((level, tracker, node(order, unknown[0][2]))) 
                weKnow = False
                print(order)
                order = unknown[0][2].input[:]

            #Swaps top row to other row
            for x in unknown:
                print(x[2].input)   
            if not 0 in unknown[0][2].input[0:3]:
                #copy above value noth to blank
                order[unknown[0][2].empty] = unknown[0][2].input[unknown[0][2].empty - 3] 
                order[unknown[0][2].empty - 3] = 0 
                #checks if nodes hasnt been known, adds child node into queue if it has.
                for x in known:
                    if order == x.input:
                        #halts if node is already known
                        weKnow = True
                #check if node is unknown
                if not weKnow:
                    level =  howDeep(unknown[0][2]) + 1
                    tracker += 1
                    unknown.append((level, tracker, node(order, unknown[0][2]))) #create new node with order 2d array and push to the back of the unknown
                weKnow = False
                print(order)
                order = unknown[0][2].input[:]



            #Swap East for columns
            #This selects the columns for the right side
            if not 0 == unknown[0][2].input[2] and not 0 == unknown[0][2].input[5] and not 0 == unknown[0][2].input[8]:
                #Copies the values of the right column
                order[unknown[0][2].empty] = unknown[0][2].input[unknown[0][2].empty + 1] 
                #empties right column
                order[unknown[0][2].empty + 1] = 0 
                for x in known:
                    if order == x.input:
                        weKnow = True
                if not weKnow:
                    level =  howDeep(unknown[0][2]) + 1
                    tracker += 1
                    unknown.append((level, tracker, node(order, unknown[0][2]))) 
                weKnow = False
                print(order)

            #Swap West
            #This selects the columns for the left side
            if not 0 == unknown[0][2].input[0] and not 0 == unknown[0][2].input[3] and not 0 == unknown[0][2].input[6]: 
                #copies the values of the left column
                order[unknown[0][2].empty] = unknown[0][2].input[unknown[0][2].empty - 1] 
                #empties left column
                order[unknown[0][2].empty - 1] = 0 
                for x in known:
                    if order == x.input:
                        weKnow = True
                if not weKnow:
                    level =  howDeep(unknown[0][2]) + 1
                    tracker += 1
                    unknown.append((level, tracker, node(order, unknown[0][2]))) 
                weKnow = False
                print(order)
                order = unknown[0][2].input[:]



        known.append(unknown[0][2])
        unknown.pop(0) #removes index
        unknown.sort()


array = [1,0,3,4,2,6,7,5,8]
uniformCostSearchAlgo(array)
