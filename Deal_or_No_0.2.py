import random

#defining some things
numbboxes = 15   #should equal len(prizes)
prizes = [1,5,10,25,50,100,250,500,1000,1250,5000,10000,25000,50000,100000]
showprizes = prizes.copy()
random.shuffle(prizes)
unopened = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  #remove opened boxes from this array when player selects them
opened = [0]    #add opened boxes (their box number) to this array to check if already opened late
openbox = 0       #temp variable to store the box user is currently opening
#error messages
msg1 = "This box is in your possession"
msg2 = "This box is already opened"

print(" ")
print("="*30)
print(" ")
print("Welcome to Deal or No!")
print("There are", numbboxes, "boxes in this game, please select one")
print(" ")

playerbox = input("  Type the number of the box you want:")

#this starts the checks if the input for playerbox is correct
while playerbox.isdigit() == False:
    print(" ")
    print("  Error: Please enter an integer")
    playerbox = input("  Your box #")

playerbox = int(playerbox)

while playerbox > numbboxes or playerbox < 1:
    print(" ")
    print("  Error: You selected an unexisting box, chose again between 1 &",numbboxes)
    playerbox = input("  Your box #")
    while playerbox.isdigit() == False:
        print(" ")
        print("  Error: Please enter an integer")
        playerbox = input("  Your box #")
    playerbox = int(playerbox)
# end of check for validity of input

print("You selected Box #", playerbox)

#remove player's box from available boxes
unopened.remove(playerbox)

print(" ")
print("="*10)
print(" ")

# ===========  opening boxes starts!! ================
print("You may now start opening boxes!")
print(" ")

#start of opening 1st box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Chose the first box you wish to open: ")

#check if integer
while openbox.isdigit() == False:
    print(" ")
    print("  Error: Please enter an integer")
    openbox = input("  Open box #")

openbox = int(openbox)

#check if already opened or if playerbox
while opened.count(openbox) > 0 or playerbox == openbox:
    print(" ")
    if playerbox == openbox:
        print("  Error:", msg1)
    else:
        print("  Error:", msg2)
    print("         You cannot open this box, choose again one of the following:")
    print(" ", unopened)
    openbox = input("  Open box #")
    while openbox.isdigit() == False:
        print(" ")
        print("  Error: Please enter an integer")
        openbox = input("  Open box #")
    openbox = int(openbox)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
print(" ")
print("OPENING BOX #", openbox)
print("  || Box contains:")
print("  || $", prizes[openbox-1])

#remove the prize
showprizes.remove(prizes[openbox-1])

#End of opening 1st box
