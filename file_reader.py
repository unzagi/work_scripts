print("Please enter the file location: ")
myFile = input()

f = open(myFile)

for line in f:
    print(line)

print("Your File is " + myFile)
