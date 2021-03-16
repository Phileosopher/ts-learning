#inputfile - filelocation of the CSV file
$inputfile='/tmp/input.CSV'

#Ouput file 
$outfile='/tmp/out.html'
#Email variable declaration
$from = 'donotreply@packtpublinux.com'
$to = 'pjayaram@gmail.com'
$cc = 'pjayaram@gmail.com'
$sub = 'Process Info-PowerShell Remoting'
$body = 'PowerShell script automation email to pull process related information from Windows and Linux machines'
$attachment = $outfile
$smtpserver = 'packpublinux@smtp.com'

#declare the array to hold multiple values
$Top = @()
#the output of import-csv is assigned to a variable
$process =Import-Csv $inputfile|% { Invoke-Command -HostName $_.Server -UserName $_.User -ScriptBlock { Param($Server)
 Get-Process | Sort-Object CPU-Descending |`
 Select-Object Handles, CPU, `
 @{name = "NPM"; Expression = {[int]($_.NPM / 1024)}}, `
 @{name = "PM"; Expression = {[int]($_.PM / 1024)}}, `
 @{name = "WS"; Expression = {[int]($_.WS / 1024)}}, `
 @{name = "VM"; Expression = {[int]($_.VM / 1MB)}},`
 @{name = "ServerName"; Expression = {($server)}},`
 Id, ProcessName -First 5 }-Args $_.Server
}
foreach ($proc in $process) 
{ 
  $row = New-Object -Type PSObject -Property @{
          ServerName = $proc.Servername 
          ID = $proc.ID
          ProcessName = $proc.ProcessName
          NPM_KB = $proc.NPM
          PM_KB = $proc.PM
          WS_KB = $proc.WS
          VM_MB = $proc.VM
         CPU_S = $proc.CPU 
        } 
 $Top += $row
 }
 $Top | ConvertTo-Html |Out-File $outfile

#Send Email outout to intended receipients

$message = new-object System.Net.Mail.MailMessage
$message.From = $from
$message.To.Add($to)
$message.CC.Add($cc)
$message.IsBodyHtml = $True
$message.Subject = $sub
$attach = new-object Net.Mail.Attachment($attachment)
$message.Attachments.Add($attach)
$message.body = $body
$smtp = new-object Net.Mail.SmtpClient($smtpserver)
$smtp.Send($message)