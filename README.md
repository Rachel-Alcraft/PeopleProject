RSA 29/4/22
## People To Projects Allocator

##### This script attempts to blend people's preferences and project priority to perform automatic allocation.
- There is an inevitable element of randomness, especially if everything is of equal priority
- Projects expiring soon are prioritised, but cancelled if they can't be allocated
- There is a preference for sharing projects if they are longer than 10 days (arbitrary)
- It will first try to allocate important preferred projects to at least 2 people, but then will try just 1 person for the preferred important projects 
- - (These rules can be changed just by shuffling the order around)

### It takes 2 csv files:
1) ProjectList.csv 
```
ID,Name,Importance,PersonDaysNeeded,DaysAvailable,DaysToExpiry
1,Allocator,10,1,28,5
(10 is high in importance, time is in days)
```
2) PeopleList.csv 
```
Name Preferences Time
Rachel,1 2 3 4,100
```
- The person preferences start at those they most want to do, but include all those they COULD POSSIBLY do even if they'd rather not.
- The separation of project-importance and person-preference removes guilt and bias from the planning stage.
- If nobody can do a project then it is not scheduled
### Output
- A single csv file with a line for every person-project allocation
```
Project,Importance,Needed,Allocated,Unallocated,DaysToExpiry,Reason,Person,Time,PersonLeft
Allocator,10,1,1,0,5,,RSA,1,0
Project1,10,56,28,28,28,,RSA,28,0
Project2,8,125,62,1,2,,RSA,62,0
Project2,8,125,62,1,2,,TJJ,62,0
```

### Allocator class
- The main class is Allocator, which takes rules which are then applied in order
```
def addRule(self,name,min_importance=0,max_fraction=1,expiry=0):        
```
-  Possible rules:
- - "cancel_nobody": There is nobody capable of doing it
- - "cancel_uncompleted_expired": (expiry,min_importance) : The project can't be scheduled in the time frame
- - "not_scheduled": It just hasn't been scheduled
- - "allocate": (min_importance,max_fraction,expiry) The main allocation, allocates on peoples preferences
- The main inputs are
- - min_importance: it will only schedule up to something of the given priority in this scheduling round
- - max_fraction: it will not schedule a single person more than this fraction of the total work, if the work is longer than the given work-alone time.
- - expiry: allocates within the time frame, 0 means anything

### Installation
- To test, just clone the repo and run the allocator.py script
- For real allocation, modify the 2 csv files in the data directory
