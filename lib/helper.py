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

def createProjectList(projects_df):
    projects = {}
    for i in range(len(projects_df.index)):        
        id = projects_df["Id"][i]
        nm = projects_df["Name"][i]
        imp = projects_df["Importance"][i]
        p_d = projects_df["PersonDaysNeeded"][i]
        days = projects_df["DaysAvailable"][i]
        exp = projects_df["DaysToExpiry"][i]
        pjct = lib.Project.Project(id,nm,imp,p_d,days,exp)
        projects[int(id)]=pjct
    return projects