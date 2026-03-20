```dataview
LIST file.link
WHERE file.mtime >= (date(today) - dur(30 days)) OR file.ctime >= (date(today) - dur(30 days))
SORT file.mtime DESC
```
