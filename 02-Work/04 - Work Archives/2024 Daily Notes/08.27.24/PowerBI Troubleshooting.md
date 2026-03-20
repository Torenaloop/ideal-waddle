It sounds like the reorganization of your SharePoint library has broken the links to your source spreadsheets in Power BI. Here’s how you can re-link them:

1. **Open Power BI Desktop**: Start by opening your Power BI Desktop application.
2. **Edit Queries**:
    - Go to the **Home** tab.
    - Click on **Transform data** to open the Power Query Editor.
3. **Locate Broken Links**:
    - In the Power Query Editor, look for any queries that are showing errors. These are likely the ones with broken links.
4. **Update Data Source Settings**:
    - Select the query with the broken link.
    - In the **Query Settings** pane, click on the **Source** step.
    - Update the file path to the new location of your spreadsheet in the reorganized SharePoint library.
5. **Re-authenticate if Necessary**:
    - If prompted, re-enter your credentials to access the SharePoint library.
6. **Apply Changes**:
    - After updating all necessary links, click **Close & Apply** to save your changes and refresh the data.
7. **Verify Data Refresh**:
    - Ensure that the data refreshes correctly and that your dashboard reflects the latest changes.

If you have multiple spreadsheets, you might need to repeat these steps for each one. Let me know if you need more detailed guidance on any of these steps! 😊  
Have you encountered any specific issues while trying to re-link the spreadsheets?
 \> From \< [https://www.bing.com/chat?form=NTPCHB](https://www.bing.com/chat?form=NTPCHB)\>     

────────────────────────────────────────────────────────────────────────────────────────────────────
 
Feedback Type:  
Frown (Error)
 
Timestamp:  
2024-08-27T18:11:54.6383119Z
 
Local Time:  
2024-08-27T14:11:54.6383119-04:00
 
Session ID:  
f645a3e9-f310-4e09-8981-9262d72ce52f
 
Release:  
August 2024
 
Product Version:  
2.132.1053.0 (24.08) (x64)
 
Error Message:  
We couldn't open the file C:\Users\dnuckolls\Downloads\Stack EHS Audit Summary Dashboard.pbix. It may have been renamed, moved, or deleted.
 
Stack Trace:  
at Microsoft.PowerBI.Client.Windows.Storage.FileOpenError.HandleError(IWindowService windowService, LocalizedString title)  
at Microsoft.PowerBI.Client.CommandLineFileService.TryOpenOrCreateReport(IPowerBIWindowService windowService, IExceptionHandler exceptionHandler, Boolean forceCreate)  
at Microsoft.PowerBI.Client.Program.\<\>c__DisplayClass7_0.\<RunApplicationLegacy\>b__0()  
at Microsoft.PowerBI.Client.Windows.IExceptionHandlerExtensions.\<\>c__DisplayClass3_0.\<HandleExceptionsWithNestedTasks\>b__0()  
at Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)
 
Stack Trace Message:  
We couldn't open the file C:\Users\dnuckolls\Downloads\Stack EHS Audit Summary Dashboard.pbix. It may have been renamed, moved, or deleted.
 
Invocation Stack Trace:  
at Microsoft.Mashup.Host.Document.ExceptionExtensions.GetCurrentInvocationStackTrace()  
at Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo..ctor(String message, Exception exception, Nullable`1 stackTraceInfo, String messageDetail)  
at Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleKnownExceptions(Exception e)  
at Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleException(Exception e)  
at Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)  
at Microsoft.PowerBI.Client.Program.RunApplicationLegacy(String[] args)  
at Microsoft.PowerBI.Client.Program.Main(String[] args)
   

InnerException0.Stack Trace Message:  
Could not find file 'C:\Users\dnuckolls\Downloads\Stack EHS Audit Summary Dashboard.pbix'.
 
InnerException0.Stack Trace:  
at System.IO.__Error.WinIOError(Int32 errorCode, String maybeFullPath)  
at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32 rights, Boolean useRights, FileShare share, Int32 bufferSize, FileOptions options, SECURITY_ATTRIBUTES secAttrs, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)  
at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access, FileShare share)  
at Microsoft.PowerBI.Client.Windows.LocalPowerBIFile.OpenSync()  
at Microsoft.PowerBI.Client.Windows.LocalPowerBIFile.Open()  
at Microsoft.PowerBI.Client.Windows.Services.BiPackageOperationHandler.\<LoadArtifact\>d__24.MoveNext()  
--- End of stack trace from previous location where exception was thrown ---  
at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  
at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)  
at Microsoft.PowerBI.Client.Windows.Services.CurrentArtifactManager.\<ExecuteAndHandleFileOpenErrors\>d__50.MoveNext()
 
InnerException0.Invocation Stack Trace:  
at Microsoft.Mashup.Host.Document.ExceptionExtensions.GetCurrentInvocationStackTrace()  
at Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromException(Exception e, String prefix)  
at Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.GetFeedbackValuesFromInnerExceptions(Exception e, Int32 depth)  
at Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo.CreateAdditionalErrorInfo(Exception e)  
at Microsoft.Mashup.Client.UI.Shared.FeedbackErrorInfo..ctor(String message, Exception exception, Nullable`1 stackTraceInfo, String messageDetail)  
at Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleKnownExceptions(Exception e)  
at Microsoft.PowerBI.Client.PowerBIUnexpectedExceptionHandler.HandleException(Exception e)  
at Microsoft.Mashup.Host.Document.ExceptionHandlerExtensions.HandleExceptions(IExceptionHandler exceptionHandler, Action action)  
at Microsoft.PowerBI.Client.Program.RunApplicationLegacy(String[] args)  
at Microsoft.PowerBI.Client.Program.Main(String[] args)
   

OS Version:  
Microsoft Windows NT 10.0.22631.0 (x64 en-US)
 
CLR Version:  
4.8 or later [Release Number = 533320]
 
Peak Virtual Memory:  
70.5 GB
 
Private Memory:  
216 MB
 
Peak Working Set:  
743 MB
 
IE Version:  
11.1.22621.0
 
User ID:  
a2382e78-57cb-493a-b4e8-b68e380363e7
 
Telemetry Enabled:  
True
 
PowerBINonFatalError_ErrorCode:  
FileNotFound
 
DPI Scale:  
100%
 
Supported Services:  
Power BI

Data source error: {"error":{"code":"DMTS_OAuthTokenRefreshFailedError","pbi.error":{"code":"DMTS_OAuthTokenRefreshFailedError","details":[{"code":"DM_ErrorDetailNameCode_UnderlyingErrorMessage","detail":{"type":1,"value":"AADSTS50076: Due to a configuration change made by your administrator, or because you moved to a new location, you must use multi-factor authentication to access '00000003-0000-0ff1-ce00-000000000000'. Trace ID: 3b33636c-b603-4f83-bd30-1fceaef5a600 Correlation ID: b1738978-0085-4ed0-9e77-16d56d6d8464 Timestamp: 2024-06-26 05:06:04Z"}}],"exceptionCulprit":1}}} Table: Compiled Findings.  
Cluster URI: WABI-US-WEST2-redirect.analysis.windows.net  
Activity ID: 0fcb8f79-fb57-46f1-9125-0c2be8819a76  
Request ID: 4748b809-871a-4e24-a7a4-cd32fe57c1b1  
Time: 2024-06-26 05:06:04Z