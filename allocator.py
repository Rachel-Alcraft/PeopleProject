"""
RSA 29/4/22
This file allocates people to projects
It can attempts to blend people's preferences and project priority
There is an inevitable element of randomness, especially if everything is of equal priority

It takes 2 csv files:
### ProjectList.csv ###
ID,Name,Importance,PersonDaysNeeded,DaysAvailable,DaysToExpiry
1,Allocator,10,1,28,5
(10 is high in importance, time is in days)

### PeopleList.csv ###
Name Preferences Time
Rachel,1 2 3 4,100

- The person preferences start at those they most want to do, but include all those they COULD POSSIBLY do even if they'd rather not.
- The seperation of project-importance and person-preference removes guilt and bias from the planning stage.
- If nobody can do a project then it is not scheduled

"""
################################# GLOBALS ##############################
people_first = True #otherwise it prioritises projects                                    
#######################################################################
import lib.Person
import lib.Project
import lib.Allocation
import lib.helper as hlp

import pandas as pd

## - First load csv files and create Person and Project objects 
people_df = pd.read_csv("data/PeopleList.csv")
projects_df = pd.read_csv("data/ProjectList.csv")

# randomly shuffle the order of the people in the list and the order of the projects
people_df = people_df.sample(frac=1).reset_index(drop=True)
projects_df = projects_df.sample(frac=1).reset_index(drop=True)

people = hlp.createPeopleList(people_df)
projects = hlp.createProjectList(projects_df)
num_projects = len(projects.items())

## - first pass is to eliminate anything that cannot be allocated
### RULE) Nobody available
print(" ### Running rule: Nobody available ###")
for person in people:
    for i in range(len(person.preferences)):
        prf = int(person.preferences[i])
        pjc = projects[prf]
        pjc.addPersonPreference(i,pjc)

for id,pjct in projects.items():
    if len(pjct.people.items()) == 0:
        pjct.addEmptyAllocation(lib.Allocation.EmptyAllocation("Nobody"))

#### Allocator) changes the time left for all the people and project objects by reference
### we optionally choose the importance that we can try to allocate each time
### (if it is 0 straight away someone could immediately get their favourite project even if it is not very important)
### Also with a preference not to have only 1 person on a project we can try a maximum fraction of the project, but then all of it if ncessary
print(" ### Running allocation: 7-10 ###")
hlp.runAllocator(num_projects,people,projects,max_importance=7,max_fraction=0.5)
hlp.runAllocator(num_projects,people,projects,max_importance=7,max_fraction=1)
print(" ### Running allocation: 4-6 ###")
hlp.runAllocator(num_projects,people,projects,max_importance=4,max_fraction=0.5)
hlp.runAllocator(num_projects,people,projects,max_importance=4,max_fraction=1)
print(" ### Running allocation: 0-3 ###")
hlp.runAllocator(num_projects,people,projects,max_importance=0,max_fraction=0.5)
hlp.runAllocator(num_projects,people,projects,max_importance=0,max_fraction=1)
        
## - Finally print out the allocations
projallocs = []
for id,pjct in projects.items():
    projallocs.append([pjct,pjct.getAllocations()])

# We have a static function to print them out
print(" ### Export dataframe results ###")
pjct.printAllocations(projallocs)





