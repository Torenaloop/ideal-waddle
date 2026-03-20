

| File | Folder | Created By |
| ---- | ------ | ---------- |
|      |        |            |
|      |        |            |
|      |        |            |
|      |        |            |
|      |        |            |



### **Who created what folders in our document libraries**

~~~dataview
TABLE "C - OneSource - 23. Safety", created-by
SORT created-by ASC
~~~


### **Folders with "OperationsEHS" tag across document libraries**

~~~dataview
TABLE 
FROM #OperationsEHS 
~~~

### **Folders with "OperationsEHS" tag in "C - OneSource - 23. Safety"

~~~dataview
TABLE
FROM "C - OneSource - 23. Safety" AND (#OperationsEHS)
~~~

### Folders with "ConstructionEHS" tag in "C - OneSource - 23. Safety"

~~~dataview
TABLE
FROM "C - OneSource - 23. Safety" AND (#ConstructionEHS)
~~~


### Folders that Donna Lynch created

~~~dataview
TABLE
WHERE created-by = "Donna Lynch"
~~~


### Folders that Kate Crawford created

~~~dataview
TABLE where created-by = "Kate Crawford"
~~~

