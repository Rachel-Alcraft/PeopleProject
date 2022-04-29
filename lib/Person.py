

class Person:
    def __init__(self, name,preferences,time):
        self.name = name
        self.preferences = preferences
        self.time = time
        self.timeLeft = time
        self.projects = []

    def isAllocated(self):
        return self.timeLeft  == 0
