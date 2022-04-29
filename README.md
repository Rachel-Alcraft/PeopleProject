RSA 29/4/22
## People To Projects Allocator
#### This script attempts to blend people's preferences and project priority to perform automatic allocation.
#### There is an inevitable element of randomness, especially if everything is of equal priority

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
- The seperation of project-importance and person-preference removes guilt and bias from the planning stage.
- If nobody can do a project then it is not scheduled

### Installation
- To test, just clone the repo and run the allocator.py script
- For real allocation, modify the 2 csv files in the data directory
