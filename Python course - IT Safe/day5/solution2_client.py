from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1",1337))

while True:
    data = client.recv(2048).decode()
    print (data)

    data = input("[+] Client: ")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break
