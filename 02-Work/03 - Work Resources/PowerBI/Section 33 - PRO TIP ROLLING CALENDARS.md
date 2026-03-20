M code to create a calendar based on the current date and time.
   

1. Create a new **blank query** & name it **"Rolling Calendar"**
    1. **Power Query**_: New Source \> Blank Query_
    2. **Front end**_: Get Data \> Blank Query_
2. In the formula bar, type a "literal" to generate a start date
    1. **Format as**_: YYYY, MM, DD_
   

==Example== ➡️ =#date(2020,1,1)
 
1. Click the **fx** icon to **add a custom step**, and enter the following formula to generate a list of dates between the start date and the current day:
    1. **Note**_: if your first applied step is named something other than "S_**ource**_", use that name in your formula (this is common for non-US users)_
    
|   |
|---|
|\|   \|   \|<br>\|---\|---\|<br>\|**🛈**\|**Information**  <br>***M Code IS CASE SENSITIVE***\||

|   |
|---|
|**M Code for Rolling Calendars**|
|```<br>= List.Dates(<br>Source,<br>Number.From(DateTime.LocalNow()) - Number.From(Source), <br>#duration(1,0,0,0)<br>```|
   

1. Convert the resulting list into a Teable and set the data type as a Date
2. Rename the column to "date" and add calculated date columns (year, month, quarter, etc.) using the Add Column tools
   
![PRO TIP ROLLING CALENDARS In the formula bar, type...](Files/Exported%20image%2020260127130919-0.png) ![PRO TIP ROLLING CALENDARS Convert the resulting li...](Files/Exported%20image%2020260127130922-1.png)