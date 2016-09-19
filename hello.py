# This program says hello and asks for my name

#Variables
year = 1
decade = 10
century = 100

yearQ = 'A: How old you are in a year?'
decadeQ = 'B: How old you are in a decade?'
centuryQ = 'C: How old you are in a century?'

print('Hello World!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()



x = 0
while x < 1:
    print('Choose from one of the following options: ')
    print(yearQ)
    print(decadeQ)
    print(centuryQ)
    myChoice = input()
    if myChoice == ("A") :
            print('You will be ' +str(int(myAge) + year) + ' in a year.')
            print('Do you want to try again?')
            myChoice = input()
            if myChoice == "N" :
                x +=1
            else:
                print('Restarting')
            
    elif myChoice == ("B") :
        print('You will be ' +str(int(myAge) + decade) + ' in a decade.')
        x += 1
    elif myChoice == ("C") :
        print('You will be ' +str(int(myAge) + century) + ' in a century.')
        x += 1
    else:
        print('ERROR: Please enter a choice A,B or C')




