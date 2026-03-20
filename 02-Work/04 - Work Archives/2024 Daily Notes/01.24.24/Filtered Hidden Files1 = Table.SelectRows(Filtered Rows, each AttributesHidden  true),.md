#"Filtered Hidden Files1" = Table.SelectRows(#"Filtered Rows", each [Attributes]?[Hidden]? \<\> true),  
#"Invoke Custom Function1" = Table.AddColumn(#"Filtered Hidden Files1", "Transform File", each #"Transform File"([Content])),  
#"Renamed Columns1" = Table.RenameColumns(#"Invoke Custom Function1", {"Name", "Source.Name"}),  
#"Removed Other Columns1" = Table.SelectColumns(#"Renamed Columns1", {"Source.Name", "Transform File"}),  
#"Expanded Table Column1" = Table.ExpandTableColumn(#"Removed Other Columns1", "Transform File", Table.ColumnNames(#"Transform File"(#"Sample File"))),  
#"Split Column by Delimiter" = Table.SplitColumn(#"Expanded Table Column1", "Source.Name", Splitter.SplitTextByDelimiter("-", QuoteStyle.Csv), {"Source.Name.1", "Source.Name.2", "Source.Name.3", "Source.Name.4"}),  
#"Changed Type" = Table.TransformColumnTypes(#"Split Column by Delimiter",{{"Source.Name.1", type text}, {"Source.Name.2", type text}, {"Source.Name.3", type text}, {"Source.Name.4", type text}}),  
#"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Source.Name.3", "Source.Name.4", "Source.Name.1"}),  
#"Split Column by Delimiter1" = Table.SplitColumn(#"Removed Columns", "Source.Name.2", Splitter.SplitTextByDelimiter(".", QuoteStyle.Csv), {"Source.Name.2.1", "Source.Name.2.2"}),  
#"Changed Type1" = Table.TransformColumnTypes(#"Split Column by Delimiter1",{{"Source.Name.2.1", type text}, {"Source.Name.2.2", type text}}),  
#"Removed Columns1" = Table.RemoveColumns(#"Changed Type1",{"Source.Name.2.2"}),  
#"Trimmed Text" = Table.TransformColumns(#"Removed Columns1",{{"Source.Name.2.1", Text.Trim, type text}}),  
#"Renamed Columns" = Table.RenameColumns(#"Trimmed Text",{{"Source.Name.2.1", "Site Code"}})  
in  
#"Renamed Columns"
    
Add the columns needed and "move things around"
 
Status now