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
        selected_class = current_class
        print(f"{character_name}, you have chosen to be a {current_class}.")
        break
    elif choise == "q":
        print("Exiting the game")
        break
    
    else:
        print("Invalid input. press [N] to cycle throu classes and [Y] to conferm current class")
    
import random

#map size in cells
width = 5
height = 5

#symbols on the map for different cell types
cell_symbols = {
    'Empty': '?',
    'Treasure': 'T',
    'Enemy': 'E',
}
hidden_cell = '?' #unexplored location

#funtion to generate map
def generate_map(width, height,):
    #initialize all cells as hidden
    return [[hidden_cell for _ in range(width)] for _ in range(height)]


#display the minimap
def display_map(game_map, character_pos):
    print("\nMinimap:")
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            #print the character initial if the current position matches
            if (x, y) == character_pos:
                print(character_initial + ' | ', end='')
            else:
                print(cell + ' | ', end='')
        print()#new line at the end of each row
    print() #extra space aftetr the map for claraity

def move_character(direction, character_pos, width, height):
    x, y = character_pos
    if direction == 'w' and  y > 0: y -= 1 # move up
    elif direction == 's' and  y < height - 1: y += 1 # move down
    elif direction == 'a' and x > 0: x -= 1 # move left
    elif direction == 'd' and x < width - 1: x += 1 # move right
    return x, y


#Main game logic
character_initial = character_name[0].upper() #First letter of character_name
game_map = generate_map(width, height)
character_pos = (width // 2, height // 2) #start character in the center of the map

#Game loop
while True:
    #example adventure text
    print("You enter the forest where there is a building and some berries on the side of the road ")
    print("Would you like to [Enter] the building or [Continue] on your journey?")

    #Display the minimap
    display_map(game_map, character_pos)

    action = input("Your action (enter/continue/q to quit): ").lower()

    #process action
    if action == "enter":
        print("Entering the building...")
        #add logic for entering the building
    elif action == "continue":
        print("Continuing on your journey...")
        #ask for direction since the player chose to continue
        direction = input("Choose a direction to move ([w] for up, [a] for left, [s] for down): ").lower()
        if direction in ['w', 'a', 's']:
            #ensure not moving right if at the edge
            new_pos = move_character(direction, character_pos, width, height)
            #Only update the position if it's valid move
            character_pos = new_pos
        else:
            print("Invalid direction. Use [W] [A] [S] to move")
    elif action == "q":
        print("Quiting game.")
        break
    else:
        print("Invalid action.")
