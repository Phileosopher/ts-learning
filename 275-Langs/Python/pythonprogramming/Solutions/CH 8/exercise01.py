# Exercise 8.1

files = {'.gif':'Graphics Interchange Format',
         '.jpg':'Joint Photographic Experts Group',
         '.tif':"Tagged Image File Format",
         '.png':"Portable Networked Graphics",
         '.wav':'Microsoft Sound File',
         '.exe':'Windows Executable',
         '.dll':"Dynamically Linked Library"}

name = input ("Enter a file name:")
sub = name[-4:]
try:
    print ("This file is a", files[sub])
except:
    print ("Don't know what ", name, " is.")
