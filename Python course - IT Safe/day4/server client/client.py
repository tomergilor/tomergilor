from socket import *


client = socket(AF_INET, SOCK_STREAM)
client.connect(("10.100.102.41", 1234))

while True:
    data = input("[+] Data > ")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break

    data = client.recv(2048).decode()
    print (data)