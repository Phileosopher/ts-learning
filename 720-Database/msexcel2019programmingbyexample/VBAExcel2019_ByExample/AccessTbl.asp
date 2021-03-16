<% @Language = VBScript %>
<%

' Send the output to Excel

Response.ContentType = "Application/vnd.ms-excel"
Response.AddHeader "Content-Disposition", _
     "attachment;filename = Shippers.xls"

' declare variables
Dim accessDB
Dim conn
Dim rst
Dim sql

' name of the database
accessDB = "Northwind 2007.accdb"


' prepare connection string
conn = "Provider=Microsoft.ACE.OLEDB.12.0;" & _
   "Data Source=" & Server.MapPath(accessDB) & _
  "; Persist Security Info = False;"

    
' Create a Recordset
Set rst = Server.CreateObject("ADODB.Recordset")

' select records from Shippers table
sql = "SELECT ID, Company, Address, City FROM Shippers"

' Open Recordset (and execute SQL statement above)
' using the open connection

rst.Open sql, conn

%>

<html>
<body>
<Table Border = "1">

    <%
    For Each fld in rst.Fields
        Response.Write("<th>") & fld.Name
    Next
    rst.MoveFirst
    Do While Not rst.EOF
        Response.Write("<tr>")
           For Each fld in rst.Fields
            Response.Write("<td>") & fld.Value & "</td>"
           Next
        Response.Write("</tr>")
        rst.MoveNext
        Loop
        %>
</table>
</body>
</html>

<%
' close the Recordset
rst.Close
Set rst = Nothing
%>

