<#
  The purpose of this script is to provide vm networking in Azure.
  This script is created by Frederik Vos,
  last updated: 08-06-2018
                          #>

$ScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
try {
  . ("$ScriptDirectory/azvariable.ps1")
}

catch {
    Write-Host "Error while loading supporting variables"
}

# Test if the vnet name not already exist:

get-AzureRmVirtualNetwork -Name $myVnet -ResourceGroupName $myResourceGroup -ErrorVariable notPresent -ErrorAction SilentlyContinue | out-null

if ($notPresent)
  {
    # vnet doesn't exist, create the subnet configuration first:
    $subnetConfig = New-AzureRmVirtualNetworkSubnetConfig -Name $myVnet -AddressPrefix $mySubnet

    # create the actual vnet
    $vnet = New-AzureRmVirtualNetwork -ResourceGroupName $myResourceGroup -Location $myLocation -Name $myVnet -AddressPrefix $mySubnet -Subnet $subnetConfig

     Write-Host "The virtual network $myVnet with $mySubnet configured is created in the location $myLocation"
  }
