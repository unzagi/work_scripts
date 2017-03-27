from netmiko import ConnectHandler

cisco_ios = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id10387.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios1 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id34220.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios2 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id36317.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios3 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id36409.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios4 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id33958.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios5 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id1770872.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios6 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id35562.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios7 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id36446.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios8 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id33822.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }
cisco_ios9 = {
    'device_type': 'cisco_ios',
    'ip':   'csr01.id37470.cpe.ifl.net',
    'username': 'sbrooks',
    'password': 'X7{}xiph',
    'verbose': False,
    }

all_devices = [cisco_ios]

#all_devices = [cisco_ios1,cisco_ios2,cisco_ios3,cisco_ios4,cisco_ios5,cisco_ios6,cisco_ios7,cisco_ios8,cisco_ios9]

x = 0
while x < 1:

##    Write to file commented out
##    print("Enter Filename with .txt extension")
##    fileName = input()
    
    print("Enter an operational command: ")
    myInput = input()
    
    for a_device in all_devices:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command(myInput)
        print ("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
        print (output)
        print (">>>>>>>>> End <<<<<<<<<")
        
##    Write to file commented out
##    text_file = open(fileName, "w")
##    text_file.write(output)
##    text_file.close()
##    print(fileName,"has been written to disk")

    x += 1
