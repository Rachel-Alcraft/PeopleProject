
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
    
    def printAllocations(self,allocs):
        dic_allocs = {"Project":[],"Importance":[],"Needed":[],"Allocated":[],"Unallocated":[],"DaysToExpiry":[],"Reason":[],"Person":[],"Time":[],"PersonLeft":[]}
        for pjct,alloc in allocs:
            if len(alloc) == 0:
                dic_allocs["Project"].append(pjct.name)                
                dic_allocs["Importance"].append(pjct.importance)                
                dic_allocs["Needed"].append(pjct.personDaysNeeded)                
                dic_allocs["DaysToExpiry"].append(pjct.daysToExpiry)                                    
                dic_allocs["Allocated"].append(0)
                dic_allocs["Unallocated"].append(pjct.personDaysNeeded)
                dic_allocs["Reason"].append("Not scheduled")
                dic_allocs["Person"].append("")
                dic_allocs["Time"].append("")
                dic_allocs["PersonLeft"].append("")                    
            else:
                for allo in alloc:
                    dic_allocs["Project"].append(pjct.name)                
                    dic_allocs["Importance"].append(pjct.importance)                
                    dic_allocs["Needed"].append(pjct.personDaysNeeded)                
                    dic_allocs["DaysToExpiry"].append(pjct.daysToExpiry)                
                    if allo.allocType() == "Empty":
                        dic_allocs["Allocated"].append(0)
                        dic_allocs["Unallocated"].append(pjct.personDaysNeeded)
                        dic_allocs["Reason"].append(allo.reason)
                        dic_allocs["Person"].append("")
                        dic_allocs["Time"].append("")
                        dic_allocs["PersonLeft"].append("")                    
                    else:
                        dic_allocs["Allocated"].append(allo.time)
                        dic_allocs["Unallocated"].append(allo.project.daysStillNeeded)                               
                        dic_allocs["Reason"].append("")
                        dic_allocs["Person"].append(allo.person.name)
                        dic_allocs["Time"].append(allo.time)                   
                        dic_allocs["PersonLeft"].append(allo.person.time_still_left)                     
                                                                                
        projalloc_df = pd.DataFrame.from_dict(dic_allocs)
        projalloc_df.sort_values(by=['Project'], inplace=True)
        pd.DataFrame.to_csv(projalloc_df,"Output_ProjectAllocations.csv",index=False)