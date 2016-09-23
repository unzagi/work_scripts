from netmiko import ConnectHandler

cisco_ios = {
    'device_type': 'juniper',
    'ip':   'csr01.id76492.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }

all_devices = [cisco_ios]

x = 0
while x < 1:

    print("Enter Filename with .txt extension")
    fileName = input()
    print("Enter an operational command: ")
    myInput = input()
    
    for a_device in all_devices:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command(myInput)
        print ("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type']))
        print (output)
        print (">>>>>>>>> End <<<<<<<<<")

    text_file = open(fileName, "w")
    text_file.write(output)
    text_file.close()
    print(fileName,"has been written to disk")

    x += 1


##    for a_device in all_devices:
##        net_connect = ConnectHandler(**a_device)
##        output = net_connect.config_mode(myInput)
##        print ("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['device_type']))
##        print (output)
##        print (">>>>>>>>> End <<<<<<<<<")


