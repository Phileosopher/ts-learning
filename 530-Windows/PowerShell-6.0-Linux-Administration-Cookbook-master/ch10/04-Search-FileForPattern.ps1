$ReportPath = "$HOME/random/FileSearchReport.txt"
$CheatsheetPath = "$HOME/Documents/code/github/powershell/cheatsheets"

if (!(Test-Path $ReportPath)) {
    New-Item $ReportPath -ItemType File -Force
}

"Here are the PowerShell code blocks present within the cheatsheets." | Out-File $ReportPath
Select-String '```powershell' $CheatsheetPath/*.md | 
    ForEach-Object {
        $PSItem = $PSItem -split ':'
        Write-Output "File Name: $($PSItem[0])"
        Write-Output "Line number: $($PSItem[1])"
        Write-Output "Pattern: $($PSItem[2])`n"
    } | Out-File $ReportPath -Append

<# Verbose version:
Select-String -Pattern '```powershell' -Path $CheatsheetPath/*.md
#>

"Here is a contextual report of all the PowerShell code blocks:" | Out-File $ReportPath -Append
Select-String '```powershell' $CheatsheetPath/*.md -Context 2, 2 |
    Select-Object Path, LineNumber, `
    @{ Name = "Before"; Expression = { $PsItem.Context.PreContext -join "`n" } }, `
    @{ Name = "After"; Expression = { $PsItem.Context.PostContext -join "`n" } } |
        Format-List | Out-File $ReportPath -Append

"Here are the files that contain the word, 'command' in them, except the cheatsheet for the first chapter:" | Out-File $ReportPath -Append
Select-String 'command' $CheatsheetPath/*.md -Exclude '*chapter-01.md' |
    Group-Object Path |
        Select-Object Name, Count |
            Format-Table -AutoSize | Out-File $ReportPath -Append

"Here are the files that contain the word, 'PowerShell' in them." | Out-File $ReportPath -Append
Select-String -CaseSensitive 'PowerShell' $CheatsheetPath/*.md -Exclude '*chapter-01.md' | 
    Select-Object Path -Unique | 
        Format-Table -AutoSize | Out-File $ReportPath -Append