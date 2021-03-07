# Introducing PowerShell Core

Get help on any command:

```powershell
# Get-Help <cmdlet name>
Get-Help Get-Command
```

Get more help on a certain cmdlet (e.g. `Get-Command`):

```powershell
# Full help text
Get-Help Get-Command -Full

# Show examples
Get-Help Get-Command -Examples

# Read the help in a browser
Get-Help Get-Command -Online
```

Update the help information:

```powershell
Update-Help
```

Select specific string from the output:

```powershell
Get-Help Get-Command | Out-String -Stream | Select-String 'common'
```

Get help on a specific parameter:

```powershell
Get-Help Get-Command -Parameter Noun
```

Work with `about_` topics:

```powershell
# List out all the `about_` topics
Get-Help about_*

# Pick the topic you would like to read about and then
Get-Help about_Modules
```

Search for cmdlets:

```powershell
# Discover cmdlets based on the noun
Get-Command -Noun Process

# Dicsover cmdlets based on the verb as well
Get-Command -Verb Get -Noun Process

# Dicsover cmdlets based on the module
Get-Command -Noun Process -Module Microsoft.PowerShell.Management
```

Search for a module in the PowerShell Gallery

```powershell
Find-Module 'Docker'
```

Install a module:

```powershell
# Install directly from the PowerShell Gallery
Install-Module 'Docker'

# To save the module and import it instead
# Create a folder where you would like to store the modules:
New-Item -ItemType Directory -Path ~/PSModules

# Save the module in the directory you just created
Save-Module Docker ~/PsModules

# Import the module
Import-Module ~/PsModules/Docker/1.3.2/Docker.psm1
```

Update a module:

```powershell
Update-Module Docker
```

Remove a module from the system:

```powershell
# Would work on the modules installed with `Install-Module`
Uninstall-Module Docker

# For modules you saved, simply delete the directory that contains the module files
Remove-Item ~/PsModules/Docker -Recurse
```

List out all the providers in PowerShell:

```powershell
Get-PsProvider
```

Navigate to one of the drives in one of the providers:

```powershell
Set-Location Alias:
```

Get information on a certain directory:

```powershell
# Using the .NET class
New-Object -TypeName System.IO.DirectoryInfo -ArgumentList '/home/ram'

# Using PowerShell
Get-Item '/home/ram'
```

Get the members that are part of the returned object:

```powershell
Get-Item '/home/ram' | Get-Member
```

Get one of the members from the output:

```powershell
# Find the time the directory was written to, last
(Get-Item /home/ram).LastWriteTime

# Find the parent of the directory
(Get-Item /home/ram).Parent

# Find the time the parent was created
(Get-Item /home/ram).Parent.CreationTime

# Pick just the year property
(Get-Item /home/ram).Parent.CreationTime.Year
```

Create a subdirectory within a directory using one of the methods available in the output object:

```powershell
(Get-Item /home/ram).CreateSubdirectory('test-directory')
```

Use a .NET type accelerator to convert text to an object:

```powershell
[datetime]'21 June 2018'

# Verify if the text was indeed converted into an object
[DateTime]'21 June 2018' | Get-Member
```

Use PowerShell to convert the same string into a date object:

```powershell
Get-Date '21 June 2018'

# Pick just the Year property to verify the output is indeed an object
(Get-Date '21 June 2018').Year
```

Convert text in the form of comma-separated values, to a PowerShell custom object:

```powershell
# Create a file from text
@'
WS,CPU,Id,SI,ProcessName
161226752,23.42,1914,1566,io.elementary.a
199598080,77.84,1050,1040,gnome-shell
216113152,0.67,19250,1566,atom
474685440,619.05,1568,1566,Xorg
1387864064,1890.29,15720,1566,firefox
'@ | Out-File sample.csv

# Read the contents of the CSV file
Get-Content ./sample.csv

# Import the file into PowerShell instead of just reading the content
Import-Csv ./sample.csv
```

Compare output of Bash and PowerShell; work with files within a directory:

```powershell
# Use Linux commandline tools
ls -l | awk '{print $6, $7, $8, $9}'

# Identify the output object type
ls -l | awk '{print $6, $7, $8, $9}' | Get-Member

# Use PowerShell
Get-ChildItem | select LastWriteTime, Name

# Identify the output object type
Get-ChildItem | select LastWriteTime, Name | Get-Member
```

Work with aliases in PowerShell:

```powershell
# List out all the available aliases
Get-Alias

# Get information on a specific alias
Get-Alias gbp

# Find all aliases for a certain cmdlet
Get-Alias -Definition Get-ChildItem
```

Create a custom alias:

```powershell
New-Alias listdir Get-ChildItem
```

Export aliases to a file for future use:

```powershell
# As a CSV file to use with Import-Alias
Export-Alias aliases.csv

# As a script, if you do not want to use CSV
Export-Alias aliases.ps1 -As Script
```

Working with execution policies (Windows only for now):

```powershell
# Find the execution policy in effect
Get-ExecutionPolicy

# List out all the execution policies set at different levels
Get-ExecutionPolicy -List

# Set an execution policy at the machine level
Set-ExecutionPolicy Undefined -Scope LocalMachine

# Set an execution policy at the user level
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```