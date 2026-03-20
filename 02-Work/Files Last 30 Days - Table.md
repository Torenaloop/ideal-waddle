```dataview
TABLE file.link AS File, file.mtime AS Modified, file.ctime AS Created
WHERE file.mtime >= (date(today) - dur(30 days)) OR file.ctime >= (date(today) - dur(30 days))
SORT file.mtime DESC
```
