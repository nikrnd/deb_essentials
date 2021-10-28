import os
import sys

dir = sys.path[0]

switcher = [
    "apt update",
    "apt full-upgrade",
    "htop",
    "cbm",
    "nano /etc/samba/smb.conf",
    "service smbd restart",
    "nano /etc/dhcpcd.confs",
    "route",
    "dig +short myip.opendns.com @resolver1.opendns.com",
    dir,
    "nano /etc/dnsmasq.conf",
    "service dnsmasq restart",
    "nano /etc/hosts"
]

def menu(int_argument):
    os.system(switcher[int_argument - 1])
    print("\n\033[1mDONE\033[0m")
    input("Press any key...")