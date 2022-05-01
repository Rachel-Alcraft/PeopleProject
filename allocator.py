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
days_in_cycle = 28 #how many working days in this scheduling cycle
randomise = True
days_alone = 15 #how many days is it ok for someone to work on a project alone?
#######################################################################
import lib.Person
import lib.Project
import lib.Allocation
import lib.Allocator
import lib.helper as hlp

import pandas as pd

# load csv files and create Person and Project objects 
people_df = pd.read_csv("data/PeopleList.csv")
projects_df = pd.read_csv("data/ProjectList.csv")
# randomly shuffle the order of the people in the list and the order of the projects
if randomise:
    people_df = people_df.sample(frac=1).reset_index(drop=True)
    projects_df = projects_df.sample(frac=1).reset_index(drop=True)
# create the list and dictionary of people and projects
people = hlp.createPeopleList(people_df)
projects = hlp.createProjectList(projects_df)
# create the allocator class
allocr = lib.Allocator.Allocator(people,projects,days_alone=days_alone)
########### RULE) Nobody available  #########################
allocr.addRule("cancel_nobody")
########### RULE) Important projects expiring soon  #########################
allocr.addRule("allocate",min_importance=10,max_fraction=0.5,expiry=days_in_cycle) 
allocr.addRule("allocate",min_importance=10,max_fraction=1,expiry=days_in_cycle) 
allocr.addRule("allocate",min_importance=5,max_fraction=0.5,expiry=days_in_cycle)
allocr.addRule("allocate",min_importance=5,max_fraction=1,expiry=days_in_cycle) 
########### RULE) Cancel projects that can't be completed  #########################
allocr.addRule("cancel_uncompleted_expired",min_importance=5,expiry=days_in_cycle)
########### RULE) Projects on priority of importance with a first attempt to share  #########################
allocr.addRule("allocate",min_importance=8,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=8,max_fraction=1) 
allocr.addRule("allocate",min_importance=5,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=5,max_fraction=1) 
allocr.addRule("allocate",min_importance=0,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=0,max_fraction=1) 
########### RULE) Cancel projects that can't be completed  #########################
allocr.addRule("cancel_uncompleted_expired",min_importance=0,expiry=days_in_cycle)
########### RULE) Projects on priority of importance with a first attempt to share  #########################
allocr.addRule("allocate",min_importance=8,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=8,max_fraction=1) 
allocr.addRule("allocate",min_importance=5,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=5,max_fraction=1) 
allocr.addRule("allocate",min_importance=0,max_fraction=0.5) 
allocr.addRule("allocate",min_importance=0,max_fraction=1) 
########### RULE) It may have not been scheduled at all  #########################
allocr.addRule("not_scheduled")
########### RUN THE RULEs  #########################
allocr.applyRules()
########### EXPORT THE RESULTS  #########################
allocr.exportResults("Output_ProjectAllocations.csv")
#########################################################################


