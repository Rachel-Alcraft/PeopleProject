

class Person:
    def __init__(self, name,preferences,time):
        self.name = name
        self.preferences = preferences
        self.time = time
        self.time_left = time
        self.allocs = []

    def addAllocation(self,alloc):
        self.allocs.appebd(alloc)

    def isAllocated(self):
        return self.time_left  == 0
