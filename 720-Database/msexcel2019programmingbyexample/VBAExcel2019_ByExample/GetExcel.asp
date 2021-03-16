
<% @Language=VBSCRIPT %>
<%
dim myConn
dim myExcel
dim strCon
dim mySQL

' Create the connection object
 set myConn = Server.CreateObject("ADODB.Connection")

' Specify the connection string
' The OLEDB connect string for Office14 (2010 version) 
' still requires Microsoft.ACE.OLEDB.12.0

 strCon="Provider=Microsoft.ACE.OLEDB.12.0;Data Source="
 strCon=strCon & server.MapPath("ExcelDb.xlsx") & ";"
 strCon=strCon & "Extended Properties=Excel 12.0"


' Open the connection
 myConn.Open strCon

' Create the Recordset
 set myExcel=Server.CreateObject("ADODB.Recordset")
 mySQL="Select * from [Sheet1$]"

' Open the Recordset
 myExcel.Open mySQL, myConn

' Show data in a table
 Response.Write("<table border=""1""><tr>")

' Get the column names
  For Each fld in myExcel.Fields
   Response.Write ("<td>") & fld.Name & ("</td>")
  Next
 Response.Write("</tr>")

' Get the actual data
 Response.Write "<tr><td>" & myExcel.GetString( _ 
	,,"</td><td>","</td></tr><tr><td>","&nbsp;")
 Response.Write("</table>")


' Close the Recordset and release the object
  myExcel.Close
  set myExcel = Nothing

' Close the connection
  myConn.Close
  set myConn = Nothing
%>
