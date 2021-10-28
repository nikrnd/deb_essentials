import os
import menu
import packages

os.system("clear")

#check if you are root
if os.geteuid() != 0:
    exit("You must be root")

#check packages
packages.check_packages()

#show menu
menu.menu()
