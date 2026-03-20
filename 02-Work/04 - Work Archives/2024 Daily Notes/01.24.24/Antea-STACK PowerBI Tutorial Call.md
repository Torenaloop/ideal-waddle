1. Open Power BI Desk Top App
2. Click on Transform Data
3. Click on "gear" next to "Source"
4. Enter url: "stackinfrastructure.sharepoint.com"
5. Open "Advanced Editor"
6. Copy "line" (See Meeting Chat) and click "enter" - 
Source = SharePoint.Files("https://stackinfrastructure.sharepoint.com", [ApiVersion = 15]),  
   #"Filtered Rows" = Table.SelectRows(Source, each ([Folder Path] = "[https://stackinfrastructure.sharepoint.com/STACK](https://stackinfrastructure.sharepoint.com/STACK?xsdata=MDV8MDJ8fDkxNzY0M2JjM2Y1YzQyNGExNDg4MDhkYzFkMGI1Yzk5fGI4Zjk0NWFhOTkzYTRhOWVhZDRmN2QyNDM5MDU2MWNifDB8MHw2Mzg0MTcxODE4MTUxNDk3MDR8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPbTFsWlhScGJtZGZUMWROZWs1RVFtMU5WRmwwVGxSQk0wMURNREJhYWtGNFRGUm5NRTE2V1hSWmJVWnRUbFJqZVU1cVJtaE9WRUpxUUhSb2NtVmhaQzUyTWk5dFpYTnpZV2RsY3k4eE56QTJNVEl4TXpnd09UUXh8NzExYTRmOTU3ZjBkNDJlNTE0ODgwOGRjMWQwYjVjOTl8ZDNkZGFlOTVkYWJkNGYzM2JjZjcyNjk2ZDcxYWNmZmU%3D&sdata=VGxGZitMTGZYdHR6RnRCeFViRU5Jd0wzazhod0QvVkdTNzB4NFE4UVFJbz0%3D&ovuser=42909416-4ba8-4195-a595-6ae640290c7d%2Cdnuckolls%40stackinfra.com) Corporate Data/23. Safety/Programs and Procedures_Working Folder_Final in Playbook/Auditing/EHS Audit Dashboard/STACK EHS Audits Site Data/"))
 10. Result should look like the following:
    ![Exported image](Files/Exported%20image%2020260127142137-0.png)      
***Connecting to SharePoint Folder***
 
Not thru C: Drive
 
***Must be thru SharePoint/Cloud***
 
PowerBi updates monthly - usually "big" updates