#Program Automation Script
#Simon Brooks
#Adapted from http://www.blog.pythonlibrary.org/2010/09/04/python-101-how-to-open-a-file-or-program/
#Change log
# a. Added menu
# b. Added verification of programs already running
# c. changed menu to function
import os



#Define the menu function
def menu(): print("\n1. Day to Day applications\n2. Instant Messaging\n3. Network Applications\n4. Project Files\n5. Run RMI\n6. Check what COM port is connected\nPress Q to quit")
x = 0

while x < 1:
##    check the current running program task list and place into "tmp" value for querying
    menu()
    myChoice = input()
    if myChoice == ("1") :
        #Run day to day applications
        tmp = os.popen("tasklist").read() 

        if "OUTLOOK.EXE" in tmp:
            print("Outlook is already running!\n")
            
        else:
            print("Starting Outlook....\n")
            os.startfile("outlook")
            
        if "vpnui.exe" in tmp:
            print("Cisco Anyconnect is already running!\n")
            
        else:
            print("Starting Cisco Anyconnect\n")
            os.startfile(r"C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe")
            
        if "Greenshot.exe" in tmp:
            print("Greenshot is already running!\n")
            
        else:
            print("Starting Greenshot\n")
            os.startfile(r"C:\Program Files\Greenshot\Greenshot.exe")
            
        print("Starting Tomighty...\n")
        os.startfile(r"C:\Program Files\Tomighty\tomighty-0.7.1.exe")

    elif myChoice == ("2") :
            #Run instant messaging applications
        tmp = os.popen("tasklist").read() 

        if "Skype.exe" in tmp:
            print("Skype is already running!\n")

        else:
            print("Starting Skype....\n")
            os.startfile("skype")
            
        if "slack.exe" in tmp:
            print("Slack is already running!\n")
            
        else:
            print("Starting Slack....\n")
            os.startfile(r"C:\Users\sbrooks\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Slack Technologies\Slack.lnk")

            
        if "UcMapi.exe" in tmp:     
            print("Skype for Business is already running!\n")
            
        else:
            print("Starting Skype for Business....\n")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Skype for Business 2016.lnk")
            
    elif myChoice == ("3") :
        tmp = os.popen("tasklist").read() 
        #Run network application
        if "gns3.exe" in tmp:
            print("GNS3 is already running\n")
            
        else:
            print("Starting GNS3....\n")
            os.startfile(r"C:\Program Files\GNS3\gns3.exe")
            
    elif myChoice == ("4") :
        #Open up specific files
        os.startfile(r"C:\Users\sbrooks\OneDrive - RM PLC\IHG\Kanban Projects\Old Core Decomissioning\Project Plan - 10916 - Step 2 mitigate and Remove.mpp")

    elif myChoice == ("5") :
        #Open up specific files
        import firefoxrmi

    elif myChoice == ("6") :
        import re
        import subprocess
        try:
            out = subprocess.check_output("mode", shell = True)
            m = re.search('COM(.+?):', str(out)).group(1)
            comPort =(r"C:\putty.exe -serial com" + m)
            print(comPort)
            print("\nYour Com port is COM" + m)
            print("Press a key to start putty")
            myChoice = input()
            import subprocess
            os.system(r"C:\putty.exe -serial com6")
            
        except:
            print("Error: COM port not connected or may already be in use. Press a key to continue")
            myChoice = input()
            
    elif myChoice == ("Q") :
        x += 1
        
    else:
        print('ERROR: Please enter a choice from above')
