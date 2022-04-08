import os


# this function return the ip address of the system
def get_ip():
    ip =  os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start+2:end]
            break

    return output


def scanner(ip_address, clients, lock):
    result = os.popen("ping {0} -n 1".format(ip_address)).read()

    if "TTL" in result:
        with lock:
            print(ip_address)
            clients.append(ip_address)