<# 
 The purpose of this script is to a resource group in Azure.
 This script is created by Frederik Vos, 
 last updated: 08-06-2018 
 #>

# include variables
$ScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
try {
  . ("$ScriptDirectory/azvariable.ps1")
}

catch {
    Write-Host "Error while loading supporting variables"
}

# test if the Resource Group already exist, if not: create it.
Get-AzureRmResourceGroup -Name $myResourceGroup -ErrorVariable notPresent -ErrorAction SilentlyContinue | out-null

if ($notPresent)
  {
    # ResourceGroup doesn't exist, create it:
    New-AzureRmResourceGroup -Name $myResourceGroup -Location $myLocation 
    
    Write-Host "The Resource Group $myResourceGroup is created in the location $myLocation"
  }

else

  {
    Write-Host "The Resource Group $myResourceGroup already existed in the location $myLocation"
  }
