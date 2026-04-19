```dataview
TASK
FROM "02-Work"
WHERE !completed
  AND !contains(file.folder, "04 - Work Archives")
GROUP BY file.link
SORT file.mtime DESC
```
