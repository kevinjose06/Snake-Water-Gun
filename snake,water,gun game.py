import random

#game control defined as a function
def game(userop,compop):
    if(userop==compop):
        print("Its a tie!")
    elif(userop==1 and compop==0):
        print("Computer wins!")
    elif(userop==1 and compop==-1):
        print("You won!")
    elif(userop==0 and compop==1):
        print("You won!")
    elif(userop==0 and compop==-1):
        print("Computer wins!")
    elif(userop==-1 and compop==0):
        print("You won!")
    elif(userop==-1 and compop==1):
        print("Computer wins!")
    else:
        print("System error!")
    return

#selecting the input
while(True):
    choice=input('''Enter your choice:
    g for Gun
    w for water 
    s for Snake
    x to exit\n''')

    if(choice=='x'):
        print("Thank you!")
        break
    #storing the values of input in 2 dictionaries
    options={'g':1,'w':0,'s':-1}
    values={1:"gun",0:"water",-1:"snake"}

    #checking the input
    if(choice not in options):
        print("Invalid input!Try again!")
        continue

    #assigning the input charecter with associated integer from the dictionary options
    userop=options[choice]
    compop=random.choice([-1, 0, 1])

    #assigning the integer with the associated value from the dictionary values
    userval=values[userop]
    compval=values[compop]

    #comparing user and computer and giving appropriate results
    print(f"You chose {userval} and the Computer chose {compval}")
    game(userop,compop)