from re import escape
import menu_items
import packages

isInstalled = False

def menu():
    text = 0
    while True:
        
        print("")
        print("-------------------------------------------")
        print("")

        print("\033[1mMENU - select an option\033[0m")
        print("    [1] update available packages - require: apt")
        print("    [2] upgrade system - require: apt")
        print("    [3] show processes - require: htop")
        print("    [4] show bandwidth - require: cbm")
        
        print("\n  \033[1mSAMBA\033[0m")
        print("    [5] samba configuration file  - require: samba, nano")
        print("    [6] samba service restart - require: samba")

        print("\n  \033[1mNETWORK\033[0m")
        print("    [7] interface priority - require: nano")
        print("    [8] routing table - require: net-tools")
        print("    [9] public ip - require: dnsutils")
        print("    [10] online or offline? - require: none")

        print("\n  \033[1mDNS\033[0m")
        print("    [11] show dns .conf file - require: dnsmasq, nano")
        print("    [12] dns service restart - require: dnsmasq, nano")
        print("    [13] show dns hosts file - require: dnsmasq, nano")
        
        print("\n  \033[1mOTHERS\033[0m")
        print("    [i] install no-installed packages - require: apt")
        print("    [q] exit")
        text = input("\nSelect: ")

        if text == "q":
            exit(0)
        elif text == "i":
            packages.install()
            input("Press any key...")
        else:
            print("")
            menu_items.menu(int(text))