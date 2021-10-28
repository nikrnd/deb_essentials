import subprocess
from tqdm import *
import os


not_installed = []

def get_shell_columns():
    columns_position = str(os.get_terminal_size()).find("columns")
    lines_position = str(os.get_terminal_size()).find(", lines")
    return int(str(os.get_terminal_size())[(columns_position + 8):lines_position])

def get_shell_lines():
    columns_position = str(os.get_terminal_size()).find("lines")
    return int(str(os.get_terminal_size())[(columns_position + 6):-1]) - 3

def check_packages():
    packages = [
        "apt",
        "cbm",
        "htop",
        "samba",
        "nano",
        "net-tools",
        "dnsmasq",
        "dnsutils"
    ]

    print("Installed packeges:")
    print("")

    prgbar = tqdm(range(len(packages)), desc = "Computing: ", leave=False)

    for i in prgbar:
        cmd = "apt list " + packages[i]
        ms = str(subprocess.Popen(cmd,shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE).stdout.read())
        #print("@@" + ms + "@@")
        if ms.find("installed") != -1:
            tqdm.write(("[\033[32mok\033[0m] : " + cmd).replace("apt list ", ""))
        else:
            tqdm.write(("[\033[31mx\033[0m] : " + cmd).replace("apt list ", ""))
            not_installed.append("apt install " + (cmd).replace("apt list ", ""))

    prgbar.close()

def install():
    while len(not_installed) > 0:
        os.system(not_installed[0])
        del not_installed[0]
    print("\033[32m\033[1mAll packages installed\033[0m\n")
    check_packages()