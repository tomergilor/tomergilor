from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", 3333))

while True:
    print ("Waiting for connection")
    data, client = server.recvfrom(2048)
    print (data.decode())

    if data.decode() == "exit":
        server.close()
        break

    data = input("Server: ")
    server.sendto(data.encode(), client)