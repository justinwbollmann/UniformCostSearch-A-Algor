#Tracking function to find how deep we are in nodes

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