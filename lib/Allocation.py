
class Allocation:
    def __init__(self, proj,pers):        
        self.project = proj
        self.person = pers
        self.time = 0        
        # the person will do as much of it as they have available
        if self.person.time_left > self.project.daysStillNeeded: 
            #one person can do it all 
            # TODO we probably don't want that, but if we fill on preference first it could make sense
            self.time = self.project.daysStillNeeded
            self.project.daysStillNeeded = 0
            self.project.allocated = True
            self.person.time_left -= self.project.daysStillNeeded
        else: #the person can do what they can
            self.time = self.person.time_left
            self.project.daysStillNeeded -= self.person.time_left
            self.person.allocated = True
            self.person.time_left = 0
    
    def allocType(self):
        return "PersonPeople"






class EmptyAllocation:
    def __init__(self, reason):
        self.reason = reason
    def allocType(self):
        return "Empty"