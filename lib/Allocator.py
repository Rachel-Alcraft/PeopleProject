"""
The Allocator class takes rules for allocation and then applies them in order
"""

import lib.Allocation as alo
import pandas as pd

class Allocator:
    def __init__(self, people, projects):        
        self.people = people
        self.projects = projects
        self.num_projects = len(projects.items())
        self.rules = []
        # inventory of the projects people want to do
        for person in self.people:
            for i in range(len(person.preferences)):
                prf = int(person.preferences[i])
                pjc = projects[prf]
                pjc.addPersonPreference(i,pjc)

    def addRule(self,name,min_importance=0,max_fraction=1,expiry=0):
        self.rules.append([name,min_importance,max_fraction,expiry])

    def applyRules(self):
        for name,min_importance,max_fraction,expiry in self.rules:
            if name == "cancel_nobody":
                self.cancelNobody()
            elif name == "cancel_uncompleted_expired":
                self.cancelUncompletedExpired(expiry,min_importance)
            elif name == "not_scheduled":
                self.cancelUnscheduled()
            elif name == "allocate":
                self.allocate(min_importance,max_fraction,expiry)

    def cancelNobody(self):        
        for id,pjct in self.projects.items():
            if len(pjct.people.items()) == 0:
                pjct.addEmptyAllocation(alo.EmptyAllocation("Nobody"))
    
    def cancelUnscheduled(self):
        for id,pjct in self.projects.items():
            if len(pjct.getAllocations()) == 0:
                pjct.addEmptyAllocation(alo.EmptyAllocation("Unscheduled"))
    
    def cancelUncompletedExpired(self,expiry,min_importance):
        for id,pjc in self.projects.items():
            if pjc.daysToExpiry <= expiry and pjc.importance >= min_importance:
                if not pjc.isAllocated():
                    for allo in pjc.allocations:
                        tm = allo.time                    
                        psn = allo.person                
                        psn.changeTimeLeft(tm)
                    pjc.allocations = []
                    pjc.addEmptyAllocation(alo.EmptyAllocation("No Time"))

    def allocate(self,min_importance,max_fraction,expiry):
        finished = False
        while not finished:
            finished = True #only set it to false if any change is made
            for i in range(self.num_projects):
                for peos in self.people:
                    if not peos.isAllocated():
                        if len(peos.preferences) > i:
                            next_preferred_project = self.projects[int(peos.preferences[i])]
                            if next_preferred_project.importance >= min_importance and not next_preferred_project.isAllocated():
                                if expiry == 0 or next_preferred_project.daysToExpiry <= expiry: 
                                    alloc = alo.Allocation(next_preferred_project,peos,max_fraction)
                                    next_preferred_project.addAllocation(alloc)
                                    finished = False

    
    def exportResults(self,filename):
        allocs = []
        for id,pjct in self.projects.items():
            allocs.append([pjct,pjct.getAllocations()])

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
        pd.DataFrame.to_csv(projalloc_df,filename,index=False)
        
        