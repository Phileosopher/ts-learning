#!/bin/sh

# The purpose of this script is to provide an ubuntu in Azure,
# Customized with cloud-init
# This script is created by Frederik Vos,
# Last updated: 08-10-2018

resourcegroup="LinuxOnAzure"
vmname="ubuntu-cloudinit"
admin="linuxadmin"
image="UbuntuLTS"
customdata="cloudinit.txt"

az vm create --resource-group $resourcegroup --name $vmname --image $image --admin-username $admin --generate-ssh-keys --custom-data $customdata

nsg=$(az network nsg list --resource-group LinuxonAzure --query "[].name" --output tsv | grep $vmname)

az network nsg rule create --resource-group $resourcegroup \
   --name ALLOW-HTTP-INTERNET-OUTBOUND --nsg-name $nsg \
   --access allow --direction outbound --protocol tcp \ 
   --destination-address-prefix 'internet' --destination-port-range 80 \
   --source-address-prefix '*' --source-port-range 80 \
   --description "Allow outbound HTTP traffic from all VMs to Internet" \
   --priority 101
