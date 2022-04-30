import lib.Person
import lib.Project
import lib.Allocation
############################## HELPER FUNCTIONS ##########################################
def createPeopleList(people_df):
    people = []
    for i in range(len(people_df.index)):
        nm = people_df["Name"][i]
        prefs = people_df["Preferences"][i].split(" ")    
        tm = people_df["Time"][i]
        prsn = lib.Person.Person(nm,prefs,tm)
        people.append(prsn)
    return people
##########################################################################################
def createProjectList(projects_df):
    projects = {}
    for i in range(len(projects_df.index)):        
        id = projects_df["Id"][i]
        nm = projects_df["Name"][i]
        imp = projects_df["Importance"][i]
        p_d = projects_df["PersonDaysNeeded"][i]        
        exp = projects_df["DaysToExpiry"][i]
        pjct = lib.Project.Project(id,nm,imp,p_d,exp)
        projects[int(id)]=pjct
    return projects
##########################################################################################
def runAllocator(num_projects,people,projects,min_importance = 0,max_fraction=1, expiry=0):
    finished = False
    while not finished:
        finished = True #only set it to false if any change is made
        for i in range(num_projects):
            for peos in people:
                if not peos.isAllocated():
                    if len(peos.preferences) > i:
                        next_preferred_project = projects[int(peos.preferences[i])]
                        if next_preferred_project.importance >= min_importance and not next_preferred_project.isAllocated():
                            if expiry == 0 or next_preferred_project.daysToExpiry <= expiry: 
                                alloc = lib.Allocation.Allocation(next_preferred_project,peos,max_fraction)
                                next_preferred_project.addAllocation(alloc)
                                finished = False
##########################################################################################
def cancelUncompletedProjects(projects, expiry):
    for id,pjc in projects.items():
        if pjc.daysToExpiry <= expiry:
            if not pjc.isAllocated():
                for allo in pjc.allocations:
                    tm = allo.time                    
                    psn = allo.person                
                    psn.changeTimeLeft(tm)
                pjc.allocations = []
                pjc.addEmptyAllocation(lib.Allocation.EmptyAllocation("No Time"))
##########################################################################################


