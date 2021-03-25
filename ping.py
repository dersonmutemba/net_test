import time
import os

def ping():
    hosts = ["www.google.com", "www.msn.com"]
    responses = 0
    pos = 0

    responses = os.system("ping -n 1 " + hosts[pos])
    print("\n\n\n\n")
    
    if(responses != 0):
        responses = os.system("ping -n 1 " + hosts[pos + 1])
        print("\n\n\n\n")
    
    return responses    

answ = ["Connected", "Desconnected"]
print("----------", answ[ping()], "----------")

while input("Press 's' to exit, any key to continue...") != "s":
    answ = ["Connected", "Desconnected"]
    print("----------", answ[ping()], "----------")
    """ time.sleep(10) """