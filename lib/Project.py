
import pandas as pd

class Project:
    def __init__(self, id,name,importance,personDaysNeeded,daysToExpiry):
        self.id = id
        self.name = name
        self.importance = importance
        self.personDaysNeeded = personDaysNeeded        
        self.daysToExpiry = daysToExpiry
        self.daysStillNeeded = personDaysNeeded
        self.allocated = False
        self.allocations = []
        self.people = {}
        
    def isAllocated(self):
        return self.allocated

    def addAllocation(self,persn_alloc):
        self.allocations.append(persn_alloc)

    
    def addEmptyAllocation(self,alloc):
        self.allocations.append(alloc)
        self.allocated = True

    def getAllocations(self): 
        return self.allocations

    def addPersonPreference(self,pref,proj):
        if pref not in self.people:
            self.people[pref] = []        
        self.people[pref].append(proj)
    
    