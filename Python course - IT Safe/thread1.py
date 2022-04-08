import os
import time
import threading


def pinger(website):
    os.system("ping {0}".format(website))


start_time = time.time()
urls = ["www.google.com","www.facebook.com","www.itsafe.co.il"]
threads = []

for url in urls:
    t = threading.Thread(target=pinger, args=(url,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print (time.time() - start_time)
