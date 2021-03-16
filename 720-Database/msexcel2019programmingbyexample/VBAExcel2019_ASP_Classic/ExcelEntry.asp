<% @Language = "VBScript"%>

<%

' Variable Declarations
'----------------------------------    
Dim adoConn    ' The ADODB connection object
Dim rst        ' The ADODB recordset object
Dim strConn    ' Connection string to Excel workbook
Dim strSQL1    ' SQL query string (Select...Where)
Dim strSQL2    ' SQL query string (Insert Into...) 
Dim strSQL3    ' SQL query string (Select count(*) ...)
Dim strName    ' Patient's name
Dim strPhone   ' Patient's phone number
Dim strFile    ' Name of Excel Workbook (holds Patient list)

' assign values to string variables        
'----------------------------------    
strFile = "ExcelDb.xlsx"
strName = Trim(Request.Form("Patient_Name"))
strPhone = Trim(Request.Form("Patient_Phone"))

' define connection string
'----------------------------------    
strConn = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source="
strConn = strConn & server.MapPath(strFile) & ";"
strConn = strConn & "Extended Properties=Excel 12.0"

' define common error handling subroutine
'--------------------------------------
Sub ErrorHandler()
    If err.number <> 0 then
      If err.number = 3709 or err.number = -2147467259 then
        Response.Write("<font color='red'>")
        Response.Write("Attention: The Excel file is in use.</br>")
        Response.Write("Please close the " & strFile &  " workbook ") 
        Response.Write("and refresh the Browser.") 
        Response.Write("</font></br>")
      Elseif err.number = -2147217865 then
        Response.Write "<font color='red'>Excel Workbook File " & _
          strFile & " cannot be found.</font>"
      Else
        Response.Write err.number & ":" & err.Description 
      End if
      Err.Clear
      Response.End
    End if
End Sub

'Enable error handling
'-------------------------------------------
On Error Resume Next

If not isEmpty(Request.Form("cmdSubmit")) then
    
    ' prepare name and phone number for entry into Excel
    ' this will prevent errors in SQL statements
    '-------------------------
    Dim strNameFormat
    strNameFormat = Replace(strName, "'", "''")    
        
    Dim strPhoneFormat
    strPhoneFormat = "(" & Left(strPhone, 3) & ")" & _ 
                     Mid(strPhone, 4,3) & "-" & _ 
                     Right(strPhone, 4)
    
    ' validate data entry fields prior to insert
    '-------------------------------------------    
    Dim isValid
    isValid = true
    
    For Each key In Request.Form
        If key = "Patient_Name" or key = "Patient_Phone" then
            If Request.Form(key) = "" Then
              Response.Write("<font color = 'blue'>")
              Response.Write("Please enter the " & key & ".</font>")
              Response.Write("<br />")
              isValid = false
              Exit For
            End If
            If key = "Patient_Phone" then
              If len(strPhone) <> 10 or not isNumeric(strPhone) then
                Response.Write("<font color = 'red'>")
                Response.Write("Enter the 10-digit phone number.")
                Response.Write("</font><br />")
                isValid = false
                Exit For
              End if        
            End if
        End if
    Next

    'if passed validation check if data already exists in Excel
    '----------------------------------------------------------            
    If isValid then
                                    
        strSQL1 = "Select count(*) from [Sheet1$] Where Patient = '" 
        strSQL1 = strSQL1 & strNameFormat & "'" & " AND phone = '" 
        strSQL1 = strSQL1 & strPhoneFormat & "'"

        Set adoConn = Server.CreateObject("ADODB.Connection")
        With adoConn
             .Open strConn
             set rst1 = .Execute(strSQL1)
        End with
                
        Call ErrorHandler()
        
        Dim recCount
        recCount = rst1(0).value
        
        Dim insertFlag
        insertFlag = True

        If recCount <> 0 then
          Response.Write("<br /><u>This record cannot be inserted.")
          Response.Write(" It already exists in Excel!</u>")
          insertFlag = false
        End if

       ' close the Recordset and cleanup
       '----------------------------------
       rst1.Close
       set rst1 = Nothing
    End if
  
    If isValid = true and insertFlag = true then

      ' define SQL Insert statement
      '----------------------------------    
      strSQL2 = "INSERT INTO [Sheet1$] (Patient, Phone)"
      strSQL2 = strSQL2 & " VALUES ('" & strNameFormat & "'"
            strSQL2 = strSQL2 & ",'" & strPhoneFormat & "')"

      Response.Write strSQL2 & "<br />"  

      'insert data into Excel
      '----------------------------------    
      Set adoConn = Server.CreateObject("ADODB.Connection")
      'On Error Resume Next
      With adoConn
         .Open strConn
         .Execute(strSQL2)
      End with 

      Call ErrorHandler()

      Response.Write("<i><font color = 'green'>")
      Response.Write("The following Data was inserted:")
      Response.Write("</font></i><hr style=""width:50%; text-align: left"" />")
      Response.Write("Patient Name: <b>" & strName & "</b><br />")
      Response.Write("Phone Number: <b>" & strPhoneFormat & "</b>")
      Response.Write("<p/>")
        
      ' clear /reset form fields
      '---------------------------------------------------------------
      document.form1.Patient_Name.value = ""
      document.form1.Patient_Phone.value = ""
      strPhone = ""
      strName = ""
    End if    
End if

'connect to Excel to retrieve data
'---------------------------------------------------- 
strSQL3 = "Select Patient, Phone From [Sheet1$]"

On Error Resume Next
Set adoConn = Server.CreateObject("ADODB.Connection")
adoConn.Open strConn

set rst2 = Server.CreateObject("ADODB.Recordset")
set rst2.ActiveConnection = adoConn
rst2.Open strSQL3

Call ErrorHandler()

%>
<!-- display the data entry form -->
<html>
<head>
   <title>Patient Data Entry Page</title>
</head>

<body>
  <form name="form1" action="ExcelEntry.asp" method="POST">
  </p>
     <table style="background-color: orange; border: 1;">
       <tr>
         <td>
           <table style="border:0">
             <tr>
               <td colspan="2" style="background-color: yellow; text-align:center">
                  Patient Data Entry Form<br />
               </td>
             </tr>
             <tr><td>&nbsp;</td></tr>
             <tr>
               <td>Patient Name: &nbsp;
                  <input type="text" name="Patient_Name"
                   size="30" value="<%=strName%>">
                   &nbsp;&nbsp;Phone:&nbsp;
                  <input type="text" name="Patient_Phone" 
                  value="<%=strPhone%>" >
               </td>
             </tr>
             <tr><td>&nbsp;</td></tr>
             <tr>
               <td style="text-align: center">
                 <input type="submit" name="cmdSubmit"  
                 value="Submit to Excel">
               </td>
             </tr>  
         </table>
       </td>
     </tr>
   </table>
  </form>
  <hr style="width: 50%; text-align: left" />
<%

'write out Excel data to the Web page
'---------------------------------- 
If Not rst2.EOF And Not rst2.BOF Then
    Dim cCode 'color code

    cOne = "#fffacd" 'yellow chiffon
    cTwo = "#E0E0E0" 'light gray
    cCode = cOne
    Response.Write("<table style=""width: 300; text-align: left; border: 0"">")
    Response.Write("<tr><td colspan='2' style=""text-align: center"">")
    Response.Write("<h3>Patient List in Excel</h3><br />") 
    Response.Write("</td></tr>")

    '---- print out column headings -------------------
    Response.Write("<tr>")
    For Each fld in rst2.Fields
       Response.Write("<td  NoWrap style=""text-align: center""><b>")
       Response.Write fld.name
       Response.Write("</b></td>")
    Next
    Response.Write("</tr>")

    '---- print out data rows -------------------
    Do While not rst2.EOF
      Response.Write("<tr>")
      For each fld in rst2.Fields
        Response.Write("<td nowrap style=""text-align: center"" bgcolor='" & _
            cCode & "'>")
        Response.Write fld.value & ("<br /></td>")
      Next
      If cCode = cOne then 
         cCode = cTwo
      Else
         cCode = cOne
      End if
      Response.Write("</tr>")
      rst2.MoveNext
    Loop
    Response.Write("</table>")
else
    '---no Patient records were found in the Excel workbook --------
    Response.Write("<table style:""border: 1; width: 50%"" >")
    Response.Write("<tr style=""valign: top"">")
    Response.Write("<td style=""text-align: left"">")
    Response.Write("<font color='Red' size='2px' face='Verdana'>")
    Response.Write("There are no records in the Excel workbook.<br />") 
    Response.Write("Use the Form above to add data.")
    Response.Write("</font></td></tr>")
    Response.Write("</table>")
End if

rst2.Close
set rst2 = nothing
adoConn.Close
set adoConn = Nothing         
  
%>
</body>
</html>


