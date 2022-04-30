
class Allocation:
    def __init__(self, proj,pers,max_fraction=1):        
        self.project = proj
        self.person = pers
        self.time = 0
        self.arbitrary_cap_on_sharing_projects = 10
        
        if proj.personDaysNeeded < self.arbitrary_cap_on_sharing_projects:
            can_be_allocated = self.project.daysStillNeeded
        else:
            can_be_allocated = min(int(proj.personDaysNeeded*max_fraction),self.project.daysStillNeeded)
        
        # the person will do as much of it as they have available
        if self.person.time_left > can_be_allocated: 
            #one person can do it all 
            # TODO we probably don't want that, but if we fill on preference first it could make sense
            self.time = can_be_allocated
            self.project.daysStillNeeded -= can_be_allocated
            if self.project.daysStillNeeded == 0:
                self.project.allocated = True
            self.person.time_left -= can_be_allocated
        else: #the person can do what they can
            self.time = self.person.time_left
            self.project.daysStillNeeded -= self.person.time_left
            self.person.allocated = True
            self.person.time_left = 0
    
    def allocType(self):
        return "PersonPeople"

######################################################################################################
class EmptyAllocation:
    def __init__(self, reason):
        self.reason = reason
    def allocType(self):
        return "Empty"