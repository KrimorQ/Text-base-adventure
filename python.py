print("Welcome to an adventure, press [Y] to play or [Q] to Exit")

player_classes = ["Warrior", "Mage", "Rouge"] #playable classes available at the start
class_index = 0 #start with the first in line (warrior)

while True:
    user = input("Your choice: ").upper() #what to enter to play (Y,Q)


    if user == "Y":
        print("Starting the game...")
        break #Exit loop

    elif user == "Q":
        print("Closing the game")
        break #Exit loop

    else:
        print("Please enter valid command ([Y] [Q])")

character_name = input("What is your name? ") #name the player character
print (f"{character_name} what class would you like to play (press N) to show next class available") #get the option to choose what class to play


while True:
    print(f"Current class: {player_classes[class_index]} press N to view the next class, or Y to choose") #view the class options available
    choise = input()

    if choise == "n":
        class_index = (class_index + 1) % len(player_classes)

    elif choise == "y":
        character_name = player_classes[class_index]
        print(f"{character_name}, you have chosen to be a {character_name}.")
        break
    else:
        print("Invalid input. press [N] to cycle throu classes and [Y] to conferm current class")
    
