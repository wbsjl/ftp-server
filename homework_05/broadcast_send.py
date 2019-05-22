from socket import *
from time import sleep

dest = ('176.122.17.255',9999)

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = """
 


    

"""


while True:
    sleep(2)
    s.sendto(data.encode(),dest)

s.close()
