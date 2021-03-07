<#
  The purpose of this script is to create a NSG in Azure.
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

# Test if the Network Security Group not already exist:

Get-AzureRmNetworkSecurityGroup -ResourceGroupName $myResourceGroup -Name $myNSG -ErrorVariable notPresent -ErrorAction SilentlyContinue | out-null

if ($notPresent)
  {
    # NSG doesn't exist, create the rules
    $NSGSSH = New-AzureRmNetworkSecurityRuleConfig -Name "SSHRule" -Protocol "Tcp" -Direction "Inbound" -Priority 1000 -SourceAddressPrefix * -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 22 -Access "Allow" 
    $NSGHTTP = New-AzureRmNetworkSecurityRuleConfig -Name "HTTPRULE" -Protocol "Tcp" -Direction "Inbound" -Priority 1001 -SourceAddressPrefix * -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 80 -Access "Allow"

    # create the NSG
    $NSG = New-AzureRmNetworkSecurityGroup -ResourceGroupName $myResourceGroup -Location $myLocation -Name $myNSG -SecurityRules $NSGSSH,$NSGHTTP

   # associate NSG with subnet
   $myVnet = Get-AzureRmVirtualNetwork -ResourceGroupName $myResourceGroup -Name $myVnet
   $NSGsubnet = Set-AzureRmVirtualNetworkSubnetConfig -Name $myVnet.Subnets.Name -VirtualNetwork $myVnet -NetworkSecurityGroupID $NSG.Id -AddressPrefix $mySubnet
   $NSGsubnet | Set-AzureRmVirtualNetwork | out-null

   Write-Host "The NSG: $myNSG is configured is created with rules for SSH and HTTP in the resource group $myResourceGroup"
  }

else
  {
   Write-Host "The NSG $myNSG already existed in the resource group $myResourceGroup"
   
  Write-Host "Configured Rules:"
    Get-AzureRmNetworkSecurityGroup -Name $myNSG -ResourceGroupName $myResourceGroup | Get-AzureRmNetworkSecurityRuleConfig
  }
