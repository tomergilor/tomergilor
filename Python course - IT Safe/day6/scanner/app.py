import eel
import threading
import os


@eel.expose
def start_scan(network_to_scan):
    my_ip = get_ip()
    network = network_to_scan[:network_to_scan.rfind(".")+1]
    clients = []
    threads = []
    lock = threading.Lock()

    for item in range(1, 255):
        test = network + str(item)

        if my_ip == test:
            continue

        t = threading.Thread(target=scanner, args=(test, clients, lock,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    return clients


def get_ip():
    ip = os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
            break


def scanner(ip_address, clients, lock):
    result = os.popen("ping {0} -n 1".format(ip_address)).read()

    if "TTL" in result:
        with lock:
            clients.append(ip_address)


eel.init('web')


try:
    eel.start('index.html', size=(850,400))
except (SystemExit, MemoryError, KeyboardInterrupt):
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
    print ("client")