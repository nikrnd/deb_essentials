import subprocess

ms = str(subprocess.Popen("ping 8.8.8.8 -c 4",shell=True, stdout=subprocess.PIPE).stdout.read())
#print(ms)
if ms.find("time=")==-1:
    #print(ms.find("time="))
    print("OFFLINE")
else:
    #print(ms.find("time="))
    print("ONLINE")