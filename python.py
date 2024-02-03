print("Welcome to an adventure, press [Y] to play or [Q] to Exit")


classes = {
    "Warrior":{
        "Stats": "Strenght: 10, Agility: 7, Intelligence: 4",
        "Backstory": "Warriors are skilled fighter and can use 1h or 2h melee weapons."
    },
    "Mage":{
        "Stats": "Strenght: 4, Agility: 7, Intelligence: 10",
        "Backstory": "Mages are skilled caster of spells and can use 1h wand or 2h staff."
    },
    "Rogue":{
        "Stats": "Strenght: 6, Agility: 10, Intelligence: 5",
        "Backstory": "Rogue rely on stealth and can use 1h daggers or shortbow."
    }


    }


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

class_name = list(classes.keys())
class_index = 0#start with the first in line (warrior)


while True:
    #print(f"Current class: {classes[class_index]} press N to view the next class, or Y to choose") #view the class options available
    #choise = input()

    current_class = class_name[class_index]
    class_info = classes[current_class]

    print(f"Class: {current_class}")
    print(f"Stats: {class_info['Stats']}")
    print(f"Backstory: {class_info['Backstory']}\n")
    print("Press [N] to view next class, or [Y] to choose this class")

    choise = input()

    if choise == "n":
        class_index = (class_index + 1) % len(classes)

    elif choise == "y":
        character_name = classes[class_index]
        print(f"{character_name}, you have chosen to be a {character_name}.")
        break
    elif choise == "q":
        print("Exiting the game")
        break
    
    else:
        print("Invalid input. press [N] to cycle throu classes and [Y] to conferm current class")
    
