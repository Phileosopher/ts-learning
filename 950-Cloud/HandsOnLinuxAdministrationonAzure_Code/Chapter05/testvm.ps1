<#
  The purpose of this script is to provide a vm.
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

# Create the resource group

New-AzureRmResourceGroup -Name $myResourceGroup -Location $myLocation

# create a virtual machine, the fast way

New-AzureRmVm -ResourceGroupName $myResourceGroup -Name $myTestVM -ImageName $myImage -Location $myLocation -VirtualNetworkName "$myTestVM-Vnet" -SubnetName $myTestVM-Subnet -SecurityGroupName "$myTestVM-NSG" -PublicIpAddressName $myTestVM-pip
