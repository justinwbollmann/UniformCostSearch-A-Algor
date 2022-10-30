import math
# This is my reference: https://www.tutorialspoint.com/python/python_nodes.htm

class node:
    def __init__(self, array, previous):
        self.data = array[:]
        self.blankLocation = array.index(0)
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.previous = previous
