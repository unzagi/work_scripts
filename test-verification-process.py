import os

tmp = os.popen("tasklist").read()

if "OUTLOOK.EXE" in tmp:
	print("success")
else:
    print("no dice")
