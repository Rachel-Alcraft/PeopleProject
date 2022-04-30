

class Person:
    def __init__(self, name,preferences,time):
        self.name = name
        self.preferences = preferences
        self.time = time
        self.time_still_left = time        
    
    def isAllocated(self):
        return self.time_still_left  == 0

    def changeTimeLeft(self,tm):
        self.time_still_left += tm
        if self.time_still_left < 0:
            assert("Can't do negative work")
