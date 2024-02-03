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
    game_map = [[hidden_cell for _ in range(width)] for _ in range(height)]
   ##center_x, center_y = width // 2, height // 2
    #game_map[center_y][center_x] = character_initial #place the character initial in the center of map
    return game_map

#display the map with the character potition in
def display_map(game_map, character_pos):
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            #print the character initial if the current position matches
            if (x, y) == character_pos:
                print(character_initial + ' | ', end='')
            else:
                print(cell + ' | ', end='')
        print()#new line at the end of each row
    print("\n") #extra space aftetr the map for claraity

def move_character(direction, character_pos, width, height):
    x, y = character_pos
    if direction == 'w' and  y > 0: # move up
        y -= 1
    elif direction == 's' and  y < height - 1: # move down
        y += 1
    elif direction == 'a' and x > 0: # move left
        x -= 1
    elif direction == 'd' and x < width - 1: # move right
        x += 1
    return x, y


#Main game logic
character_initial = character_name[0].upper() #First letter of character_name
game_map = generate_map(width, height)
character_pos = (width // 2, height // 2) #start character in the center of the map

#Main game loop for movement
while True:
    display_map(game_map, character_pos)
    direction = input("Move (WASD)? ").lower()
    if direction in ['w', 'a', 's', 'd']:
        character_pos = move_character(direction, character_pos, width, height)
    elif direction == 'q': #quit the game
        print("Quiting game.")
        break
    else:
        print("Invalid input. use WASD to move, or Q to quit.")

#creating the map
#game_map = generate_map(width, height, character_initial)

#display the map
#display_map(game_map)