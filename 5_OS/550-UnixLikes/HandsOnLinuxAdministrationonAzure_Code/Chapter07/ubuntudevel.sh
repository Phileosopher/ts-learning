#!/bin/sh

# The purpose of this script is to provide an ubuntu vm in Azure.
# This script is created by Frederik Vos,
# Last updated: 08-10-2018

resourcegroup="capture"
location="westus"
vmname="ubuntu-cloudinit"
admin="linvirt"
image="UbuntuLTS"

az group create --name $resource-group --location $location

az vm create --resource-group $resourcegroup --name $vmname --image $image --admin-username $admin --generate-ssh-keys 
