<#
  The purpose of this script is to add a disk to an existing vm
  This script is created by Frederik Vos,
  last updated: 08-10-2018
                          #>

$ScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
try {
  . ("$ScriptDirectory/azvariable.ps1")
}

catch {
    Write-Host "Error while loading supporting variables"
}

# Create the disk configuration

$diskConfig = New-AzureRmDiskConfig -SkuName $sku -Location $myLocation -CreateOption 'Empty' -DiskSizeGB $disksize

# Create the disk using this configuration

$dataDisk1 = New-AzureRmDisk -DiskName $diskname -Disk $diskConfig -ResourceGroupName $myResourceGroup

# Attach the disk to the virtual machine

$vm = Get-AzureRmVM -Name $myTestVM -ResourceGroupName $myResourceGroup
$vmdisk = Add-AzureRmVMDataDisk -VM $vm -Name $diskname -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun $lun 

Update-AzureRmVM -VM $vm -ResourceGroupName $myResourceGroup
