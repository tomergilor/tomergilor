import os
from functions import get_ip, scanner
import threading



my_ip  = get_ip()
network = my_ip[:my_ip.rfind(".")+1]
clients = []
threads = []
lock = threading.Lock()

for item in range(1,255):
    test = network+str(item)
    t = threading.Thread(target=scanner,args=(test, clients,lock, ))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print (clients)