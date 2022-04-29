
import pandas as pd

class Project:
    def __init__(self, id,name,importance,personDaysNeeded,daysAvailable,daysToExpiry):
        self.id = id
        self.name = name
        self.importance = importance
        self.personDaysNeeded = personDaysNeeded
        self.daysAvailable = daysAvailable
        self.daysToExpiry = daysToExpiry
        self.daysStillNeeded = personDaysNeeded
        self.allocated = False
        self.allocations = []
        self.people = {}

    def isExpired(self):
        if self.daysToExpiry < self.daysAvailable:
            return True
        return False
    
    def isAllocated(self):
        return self.allocated
    
    def addEmptyAllocation(self,alloc):
        self.allocations.append(alloc)
        self.allocated = True

    def getAllocations(self): 
        return self.allocations

    def addPersonPreference(self,pref,proj):
        if pref not in self.people:
            self.people[pref] = []        
        self.people[pref].append(proj)
    
    def printAllocations(self,allocs):
        dic_allocs = {"Project":[],"Allocated":[],"Reason":[],"Person":[],"Time":[],"PersonLeft":[],"ProjectLeft":[]}
        for pjct,alloc in allocs:
            for allo in alloc:
                dic_allocs["Project"].append(pjct.name)
                dic_allocs["ProjectLeft"].append("")                               
                if allo.allocType() == "Empty":
                    dic_allocs["Allocated"].append("N")
                    dic_allocs["Reason"].append(allo.reason)
                    dic_allocs["Person"].append("")
                    dic_allocs["Time"].append("")
                    dic_allocs["PersonLeft"].append("") 
                    
                    
        
        projalloc_df = pd.DataFrame.from_dict(dic_allocs)
        pd.DataFrame.to_csv(projalloc_df,"ProjectAllocations.csv",index=False)