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
def display_map(game_map, character_pos, character_initial):
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
    #move up
    if direction == 'w' and y > 0:
        y -= 1
    elif direction == 's' and y < height - 1:
        y += 1
    elif direction == 'a' and x > 0:
        x -= 1
    elif direction == 'd' and x < width - 1:
        x += 1
    return x, y

#movement inside the map and can not exit map
def get_available_directions(character_pos, width, height):
    #unpack the characters current position
    x, y = character_pos
    directions = []

    #check for each direction if the move is possible
    if y > 0: #can move up
        directions.append(('w', 'up'))
    if y < height - 1: #can move down
        directions.append(('s', 'down'))
    if x > 0: #can move left
        directions.append(('a', 'left'))
    if x < width - 1: #can move right
        directions.append(('d', 'right'))

    return directions

def prompt_direction(directions):
    direction_keys = [direction[0] for direction in directions]
    direction_names = [direction[1] for direction in directions]
    direction_input = input(f"Choose a direction to move ({'/'.join(direction_names)}): ").lower()
    if direction_input in direction_keys:
        return direction_input
    else:
        print("Invalid direction,")
        return None

#Initialize character name and position
character_initial = character_name[0].upper()
game_map = generate_map(width, height)
character_pos = (width // 2, height // 2)


#Game loop
while True:
    #example adventure text
    print("You enter the forest where there is a building and some berries on the side of the road ")
    print("Would you like to [Enter] the building or [Continue] on your journey?")

    #Display the minimap
    display_map(game_map, character_pos, character_initial)

    action = input("Your action (enter/continue/q to quit): ").lower()

    #process action
    if action == "enter":
        print("Entering the building...")
        #add logic for entering the building
    elif action == "continue":
        print("Continuing on your journey...")
        #get avalible directions based on the current potition
        available_directions = get_available_directions(character_pos, width, height)

        if not available_directions:
            print("No availble directions to move.")
            continue

        direction = prompt_direction(available_directions)
        if direction:
            character_pos = move_character(direction, character_pos, width, height)
    elif action == "q":
        print("Quiting game.")
        break
    else:
        print("Invaldid action.")