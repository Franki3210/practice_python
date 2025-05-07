import os
shutdown=input("quieres apagar tu ordenador s/n:\n")
if shutdown.lower()=="s":
    os.system("shutdown /s /t /1")
else:
    exit()

