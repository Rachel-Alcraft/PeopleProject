"""
RSA 29/4/22
This file allocates people to projects
It can prioritise people or projects in the allocation

It takes 2 csv files

ProjectList.csv
ID,Name,Importance,PersonDaysNeeded,DaysAvailable,DaysToExpiry
1,Allocator,10,1,28,5

PeopleList.csv
Name Preferences Time
Rachel,1 2 3 4,100

The person preferences start at those they most want to do, but include all those they COULD POSSIBLY do even if they'd rather not.
The seperation of project-importance and person-preference removes guilt and bias from the planning stage.

There is an inevitable element of randomness, especially if everything is of equal priority
Some inbuilt rules are:
- If it it too late to complete the project then it is not scheduled
- If nobody can do a project then it is not scheduled

(currently all in one file for distribution purposes)

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
print(projects)

## - first pass is to eliminate anything that cannot be allocated
### RULE 1) Nobody available
for person in people:
    for i in range(len(person.preferences)):
        prf = int(person.preferences[i])
        pjc = projects[prf]
        pjc.addPersonPreference(i,pjc)

for id,pjct in projects.items():
    if len(pjct.people.items()) == 0:
        pjct.addEmptyAllocation(lib.Allocation.EmptyAllocation("Nobody"))



### RULE 2) EXPIRED PROJECTS
for id,pjct in projects.items():
    if not pjct.isAllocated():
        if pjct.isExpired():
            pjct.addEmptyAllocation(lib.Allocation.EmptyAllocation("Expired"))



if people_first:
    deadlock = False
    while not deadlock:
        deadlock = True #only set it to false if any change is made
        for peos in people:
            if not peos.isAllocated():
                print("")







## - Finally print out the allocations
projallocs = []
for id,pjct in projects.items():
    projallocs.append([pjct,pjct.getAllocations()])

# We have a static function to print them out
pjct.printAllocations(projallocs)





