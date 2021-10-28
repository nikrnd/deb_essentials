import subprocess

def netCon():
    ms = str(subprocess.Popen("ping 8.8.8.8 -c 1 -t 5",shell=True, stdout=subprocess.PIPE).stdout.read())
    if ms.find("time=")!=-1:
        print("OFFLINE")
    else:
        print("ONLINE")