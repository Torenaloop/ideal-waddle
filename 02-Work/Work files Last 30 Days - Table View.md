```dataview
TABLE file.link AS File, file.mtime AS Modified, file.ctime AS Created
FROM "02-Work"
WHERE file.mtime >= (date(today) - dur(30 days)) OR file.ctime >= (date(today) - dur(30 days))
SORT file.mtime DESC
```
