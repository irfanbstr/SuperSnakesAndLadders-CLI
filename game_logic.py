#SUPER SNAKES AND LADDERS CLI v0.1
#by irfanbstr

import random

class Board:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} (Board) was created.")
# ---

class Dice:
    def __init__(self,name):
        self.name = name
        self.value = 0
        print(f"{self.name} (Dice) was created.")
    
    def dice_roll(self):
        self.value = random.randint(1, 6)
        return self.value
# ---

#Player class will handle the position of each player and the move function
class Player:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} (Player) was created.")
        self.position = 0  # Give it a starting value

    def move(self, steps):
        self.position += steps
        print(f"{self.name} moved to {self.position}")
# ---

# Objects serve as a superclass for our snakes and ladders
class Object:
    def __init__(self, name, type, val):
        self.name = name
        self.val = val
        print(f"{self.name} ({type} was created.")
# ---

#setup game loop:

print("Hello! Welcome to Super Snakes And Ladders!\n")

# --- Get Player Count (with validation) ---
playercount = 0
while True:
    playercount_str = input("How many players are we having today? (1-4): ")
    if playercount_str.isdigit():
        playercount = int(playercount_str)
        if 1 <= playercount <= 4:
            break  # Valid input, exit the loop
        else:
            print("Please enter a number between 1 and 4.")
    else:
        print("That's not a number. try again!")

# --- Get Player Names ---
# This list will hold all your Player objects
players = [] 

print(f"\nGreat! Let's get names for the {playercount} players.")
for i in range(playercount):
    # 'i + 1' makes it "Player 1", "Player 2", etc.
    name = input(f"Enter name for Player {i + 1}: ")
    players.append(Player(name))

# --- Get Player Names done ---

print("\nLet's begin! Our players are:")
for player in players:
    print(f"- {player.name} (starting at {player.position})")

#main game loop:
diceval = 0
mydice = Dice("1d6")

game_is_running = True
while game_is_running:
    for current_player in players:            
        print(f"\nIt's {current_player.name}'s turn.")
        print(f"{current_player.name} is now on square {current_player.position}.")
        # We ask the user to just press Enter
        user_action = input("Press ENTER to roll the dice (or type 'quit' to exit): ")

        if user_action == "":
            # The user just pressed Enter
            print("Rolling the dice!")
            diceval = mydice.dice_roll()
            input("...The Result is...")
            input(f"...{diceval}")
            # ... add your game logic here ...2
            current_player.move(diceval)
            # print(f"{current_player.name} moves forward {diceval} squares!")
            # print(f"{current_player.name} is now on square {current_player.position}.\n")
            
        elif user_action == "quit":
            print("Thanks for playing!")
            break # Exit the loop
            
        else:
            # The user typed something else
            print(f"I don't understand '{user_action}'. Please just press ENTER.")
            
        if current_player.position >= 100:
           print(f"{current_player.name} WINS!")
           game_is_running = False # This will end the 'while' loop
           break # This will end the 'for' loop

