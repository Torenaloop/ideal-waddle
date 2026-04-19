
```dataview
LIST
FROM "02-Work"
WHERE length(filter(file.tasks, (t) => !t.completed)) > 0
SORT file.mtime DESC
```
