print("Welcome to an adventure, press Y to play or Q to Exit")

player_classes = ["Warrior", "Mage", "Rouge"]
class_index = 0

while True:
    user = input("Your choice: ").upper() #what to enter to play (Y,Q)


    if user == "Y":
        print("Starting the game...")
        break #Exit loop

    elif user == "Q":
        print("Closing the game")
        break #Exit loop

    else:
        print("Please enter valid command (Y,Q)")

character_name = input("What is your name? ")
print (f"{character_name} What class would you like to play (press N) to show next class available")


