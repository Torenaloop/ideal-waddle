What is the problem that is attempting to be solved for? As a (relatively new) AMER Regional #EHS Manager, I have noticed that their are several different repositories/libraries in which #EHS-related content exists.  At present, the structure for some document libraries is lacking (in my opinion) and accessing important information can become a guessing game, game of memory, and is very tribal knowledge.

## The Exercise 

Identify the main "parent" libraries of [[EHS-related content]], mirror the existing [[folder structure]] with "dummy" folders in this Vault, and then attempt to reorganize the the same "dummy" folders in a more intuitive way. 


## Up Next....

Find the main "parent" libraries of [[EHS-related content]] and begin sorting out the existing structure in this Vault

I believe the first pass of "parent" libraries will be as follows:

1. [[0.00.00.00 OneSource - Safety Tile]]
2. [[1.00 OneSource - 23. Safety]]
3.  [[2.00.00.00 Environmental, Health & Safety - AMR EHS Operations]] 
4. [[3.00.00.00 Operations - STACK Playbook - STACK Americas - 1. Safety]]



**List of all folders in 23. Safety**
~~~dataview
TABLE
FROM "C - OneSource - 23. Safety"
~~~





# Agenda



# Notes



# Follow-up Tasks



**Folders tagged with "ConstructionEHS" tag in our document libraries
~~~dataview
TABLE
FROM #ConstructionEHS 
~~~


**Files with the "OperationsEHS" tag across document libraries
~~~dataview
TABLE 
FROM #OperationsEHS 
~~~




**Files with "OperationsEHS" tag in Folder C - OneSource - 23. Safety**
~~~dataview
TABLE
FROM "C - OneSource - 23. Safety" AND (#OperationsEHS)
~~~




**Files with "ConstructionEHS" tag in Folder C - OneSource - 23. Safety**
~~~dataview
TABLE
FROM "C - OneSource - 23. Safety" AND (#ConstructionEHS)
~~~





**Open Tasks**
~~~dataview
TASK
WHERE !completed
LIMIT 10
GROUP BY file.link
SORT rows.file.ctime ASC
~~~




**Who created what folders in our document libraries**

~~~dataview
TABLE "C - OneSource - 23. Safety", created-by
SORT created-by ASC
~~~




**Folders that Donna Lynch Created**

~~~dataview
TABLE
WHERE created-by = "Donna Lynch"
~~~


Folders that Kate Crawford created
~~~dataview
TABLE where created-by = "Kate Crawford"
~~~
