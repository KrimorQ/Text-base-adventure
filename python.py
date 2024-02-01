print("Press Y to enter or Q to quit") #start screen

user = input("Your choice: ").upper() #what to enter to play (Y,Q)

if user == "Y":
    print("Starting the game...")

elif user == "Q":
    print("Closing the game")

else:
    print("Please enter valid command (Y,Q)")


