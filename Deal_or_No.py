import random

numbboxes = 5

print("Welcome to Deal or No!")
print("There are", numbboxes, "boxes in this game, please select one")
print("Type the number of the box you selected (1 to 5):")

playerbox = input()

#this strats the checks if the input is correct
while playerbox.isdigit() == False:
    print("Error: Please enter an integer")
    playerbox = input()

playerbox = int(playerbox)

print("You selected Box #", playerbox)

while playerbox > numbboxes or playerbox < 1:
    print("  Error: you selected an unexisting box, chose again between 1 & 5")
    playerbox = input()
    while playerbox.isdigit() == False:
        print("  Error: Please enter an integer")
        playerbox = input()
    playerbox = int(playerbox)
# end of check for validity of input

print("You selected Box #", playerbox)
