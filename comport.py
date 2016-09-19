import re
import subprocess

out = subprocess.check_output("mode", shell = True)

m = re.search('COM(.+?):', str(out)).group(1)

print("Your Com port is COM" + m)
