import os
import socket

computer_name = socket.gethostname()
print(computer_name)

ip_address = socket.gethostbyname(computer_name)
## or we could do this:
ip_address2 = socket.gethostbyname(socket.gethostname())

interface = "Local Area Connection"
ipAddress = "192.168.1.10"
gateway = "192.168.1.254"
subnetMask = "255.255.255.0"
ip = "ipv4"


command = 'netsh interface ' + ip + ' set address name="' + interface + '" static ' + ipAddress + ' ' + subnetMask
print("This script needs to run as Administrator")
print(command)

try:
    os.system(command)
    print("Changed")
except:
    print("Error")


print(ip_address)
print(ip_address2)

