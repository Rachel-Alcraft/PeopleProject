
class Allocation:
    def __init__(self, alloc_kind,proj,pers):
        self.alloc_kind = alloc_kind
        self.project = proj
        self.person = pers

class PersonAllocation:
    def __init__(self, name,time,timeleft):
        print("Allocation")    
    def allocType(self):
        return "Person"

class ProjectAllocation:
    def __init__(self, project,time,timeleft):
        print("Allocation")
    def allocType(self):
        return "Project"

class EmptyAllocation:
    def __init__(self, reason):
        self.reason = reason
    def allocType(self):
        return "Empty"