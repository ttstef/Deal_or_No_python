import random
import math

##TO CHANGE:    make deals adaptable to what player has in box!
##              make inteface using tkinter (long term)

#checks if the input is an integer
def checkint(x):
    while x.isdigit() == False:
        print(" ")
        print("  Error: Please enter an integer")
        x = input("  Open box #")
    return x

#checks if selected box is out of bounds bounds, returns true if within bounds
def checkbounds(box, max):
    if box < 1 or box > max:
        return False
    else:
        return True

#checks if the box the player is opening has already been opened or is the player's box
#ALWAYS INPUT SAME PARAMETERS AS FIRST BOX OPENED
#returns integer
def checkopen(box,pbox,max,opar,unopar,str1,str2,str3):
    while opar.count(box) > 0 or pbox == box or checkbounds(box, max) == False:
        print(" ")
        if pbox == box:
            print("  Error:", str1)
        elif checkbounds(box,max) == False:
            print("  Error:", str3)
        else:
            print("  Error:", str2)
        print("         You cannot open this box, choose again one of the following:")
        print(" ", unopar)
        box = input("  Open box #")
        box = int(checkint(box))
    return box

#checks the answer of the Deal or No Deal question
#returns boolean True if deal, False if No Deal
def checkans(ans):
    ans = ans.lower()
    ans = ans.replace(" ", "")

    while ans != "deal" and ans != "nodeal" and ans != "yes" and ans != "no":
        print(" ")
        print("  Please write 'Deal' or 'No Deal'")
        ans = input("  ")
        ans = ans.lower()
        ans = ans.replace(" ", "")

    if ans == "deal" or ans == "yes":
        return True
    else:
        return False

#opens the box
def opening(box,prizar):
    print(" ")
    print("OPENING BOX #", box)
    print("  || Box contains:")
    print("  || $", prizar[box-1])
    print(" ")

#calculates the value of the deal
#the deal is 5% below the average of the remaining prizes, floored to be rounded with two sig figs
def calcdeal(showprizar):
    sum = 0
    for i in range (len(showprizar)-1):
        sum = sum + showprizar[i]
    avg = sum / len(showprizar)
    deal = avg - 0.05*avg
    l = len(str(math.floor(deal)))
    deal = deal / (10**(l-2))
    deal = math.floor(deal) * (10**(l-2))
    return deal

#defining some things
numbboxes = 15   #should equal len(prizes)
prizes = [1,5,10,25,50,100,250,500,1000,1250,5000,10000,25000,50000,100000]
showprizes = prizes.copy()
random.shuffle(prizes)
unopened = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  #remove opened boxes from this array when player selects them
opened = [0]    #add opened boxes (their box number) to this array to check if already opened later
openbox = 0       #temp variable to store the box user is currently opening
#error messages
msg1 = "This box is in your possession"
msg2 = "This box is already opened"
msg3 = "This box does not exist"

print(" ")
print("="*30)
print(" ")
print("Welcome to Deal or No!")
print("There are", numbboxes, "boxes in this game, please select one")
print(" ")

playerbox = input("  Type the number of the box you want: ")

#this starts the checks if the input for playerbox is correct
while playerbox.isdigit() == False:
    print(" ")
    print("  Error: Please enter an integer")
    playerbox = input("  Your box #")

playerbox = int(playerbox)

while playerbox > numbboxes or playerbox < 1:
    print(" ")
    print("  Error: You selected an unexisting box, choose again between 1 &",numbboxes)
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

openbox = input("  Choose the first box you wish to open: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

#2nd box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Choose the second box you wish to open: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

#3rd box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Choose the third box you wish to open: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

#4th box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Choose the fourth box you wish to open: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

#5th box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Choose the fifth box you wish to open: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

# 6th box
print("Available boxes:", unopened)
print("Remaining prizes:", showprizes)
print(" ")

openbox = input("  Choose the last box you wish to open before the deal: ")

#checks
openbox = int(checkint(openbox))
openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

#store information
unopened.remove(openbox)
opened.append(openbox)

#opening the box
opening(openbox,prizes)

#remove the prize
showprizes.remove(prizes[openbox-1])

#=========== DEAL ===============
print("   ===  THE DEAL  ===   ")
print(" ")
print("Remaining prizes:", showprizes)
print("The Banker has considered your case, and is offering you the following deal:")
print(" ")
deal = calcdeal(showprizes)
print("  $", deal)
print(" ")

ans = input("  DEAL, OR NO DEAL?   ")

#if the user takes the deal
if(checkans(ans)):
    print(" ")
    print("  We have a Deal!")
    print("  You have won $", deal, "today!")
    print(" ")
    print("  Would you like to see what was inside your box?")
    ans = input("  ")
    ans = ans.lower()
    ans = ans.replace(" ", "")

    while(ans != "yes" and ans != "no"):
        print(" ")
        ans = input("  Please write 'Yes' or 'No' : ")
        ans.lower()
        ans.replace(" ", "")

    if(ans == "yes"):
        opening(playerbox, prizes)

else:

# ===========  opening boxes second round ================
    print("="*10)
    print("")
    print("You have refused the Deal, the Game continues!")
    print("You may now open four more boxes before the next deal.")
    print("")

    #start of opening 7th box
    print("Available boxes:", unopened)
    print("Remaining prizes:", showprizes)
    print(" ")

    openbox = input("  Choose the first box you wish to open: ")

    #checks
    openbox = int(checkint(openbox))
    openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

    #store information
    unopened.remove(openbox)
    opened.append(openbox)

    #opening the box
    opening(openbox,prizes)

    #remove the prize
    showprizes.remove(prizes[openbox-1])

    #8th box
    print("Available boxes:", unopened)
    print("Remaining prizes:", showprizes)
    print(" ")

    openbox = input("  Choose the second box you wish to open: ")

    #checks
    openbox = int(checkint(openbox))
    openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

    #store information
    unopened.remove(openbox)
    opened.append(openbox)

    #opening the box
    opening(openbox,prizes)

    #remove the prize
    showprizes.remove(prizes[openbox-1])

    #9th box
    print("Available boxes:", unopened)
    print("Remaining prizes:", showprizes)
    print(" ")

    openbox = input("  Choose the third box you wish to open: ")

    #checks
    openbox = int(checkint(openbox))
    openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

    #store information
    unopened.remove(openbox)
    opened.append(openbox)

    #opening the box
    opening(openbox,prizes)

    #remove the prize
    showprizes.remove(prizes[openbox-1])

    #10th box
    print("Available boxes:", unopened)
    print("Remaining prizes:", showprizes)
    print(" ")

    openbox = input("  Choose the last box you wish to open before the next deal: ")

    #checks
    openbox = int(checkint(openbox))
    openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

    #store information
    unopened.remove(openbox)
    opened.append(openbox)

    #opening the box
    opening(openbox,prizes)

    #remove the prize
    showprizes.remove(prizes[openbox-1])

    #11th box
    print("Available boxes:", unopened)
    print("Remaining prizes:", showprizes)
    print(" ")

#========= SECOND DEAL ============

    print("   ===  THE DEAL  ===   ")
    print(" ")
    print("Remaining prizes:", showprizes)
    print("The Banker has considered your case, and is offering you the following deal:")
    print(" ")
    deal = calcdeal(showprizes)
    print("  $", deal)
    print(" ")

    ans = input("  DEAL, OR NO DEAL?   ")

    #if the user takes the deal
    if(checkans(ans)):
        print(" ")
        print("  We have a Deal!")
        print("  You have won $", deal, "today!")
        print(" ")
        print("  Would you like to see what was inside your box?")
        ans = input("  ")
        ans = ans.lower()
        ans = ans.replace(" ", "")

        while(ans != "yes" and ans != "no"):
            print(" ")
            ans = input("  Please write 'Yes' or 'No' : ")
            ans.lower()
            ans.replace(" ", "")

        if(ans == "yes"):
            opening(playerbox, prizes)

    else:

#=========== opening boxes third round ================

        print("="*10)
        print("")
        print("You have refused this Deal as well, the Game continues!")
        print("You may now open three more boxes before the next deal.")
        print("")

        #12th box
        print("Available boxes:", unopened)
        print("Remaining prizes:", showprizes)
        print(" ")

        openbox = input("  Choose the first box you wish to open: ")

        #checks
        openbox = int(checkint(openbox))
        openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

        #store information
        unopened.remove(openbox)
        opened.append(openbox)

        #opening the box
        opening(openbox,prizes)

        #remove the prize
        showprizes.remove(prizes[openbox-1])

        #13th box
        print("Available boxes:", unopened)
        print("Remaining prizes:", showprizes)
        print(" ")

        openbox = input("  Choose the second box you wish to open: ")

        #checks
        openbox = int(checkint(openbox))
        openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

        #store information
        unopened.remove(openbox)
        opened.append(openbox)

        #opening the box
        opening(openbox,prizes)

        #remove the prize
        showprizes.remove(prizes[openbox-1])

        #14th box
        print("Available boxes:", unopened)
        print("Remaining prizes:", showprizes)
        print(" ")

        openbox = input("  Choose the last box you wish to open before the next deal: ")

        #checks
        openbox = int(checkint(openbox))
        openbox = checkopen(openbox,playerbox,numbboxes,opened,unopened,msg1,msg2,msg3)

        #store information
        unopened.remove(openbox)
        opened.append(openbox)

        #opening the box
        opening(openbox,prizes)

        #remove the prize
        showprizes.remove(prizes[openbox-1])

#=========== LAST DEAL ===========

        print("   ===  THE DEAL  ===   ")
        print(" ")
        print("Your box: [", end="")
        print(playerbox,end="")
        print("]")
        print("Remaining box:", unopened)
        print("Remaining prizes:", showprizes)
        print("")
        print("This is your last deal, and the Banker is offering you the following:")
        print("")
        print("   Switch your Box with the last remaining Box.")
        print("")

        ans = input("  DEAL, OR NO DEAL?   ")
        print("")

        if(checkans(ans)):

            print("The boxes have been switched! Your box is now box #", unopened[0])
            print("It is now time to open them both!")
            print("")
            ans = ""

            #just to stall a little bofre opening, you know... makin it tense
            while ans != "open":
                ans = input("  Type 'open' to open the boxes: ")
                ans = ans.lower()
                ans = ans.replace(" ", "")

            print("")
            print("Your old box:")
            opening(playerbox, prizes)
            print("")
            print("Your new box:")
            opening(unopened[0], prizes)

            print("Today you have won $", prizes[unopened[0]-1])
            print("Thank you for playing Deal or No!")

        else:

            print("You have chosen to keep your box! Your box is still box #", playerbox)
            print("It is now time to open them both!")
            print("")
            ans = ""

            #just to stall a little bofre opening, you know... makin it tense
            while ans != "open":
                ans = input("  Type 'open' to open the boxes: ")
                ans = ans.lower()
                ans = ans.replace(" ", "")

            print("")
            print("The last remaining box:")
            opening(unopened[0], prizes)
            print("")
            print("Your box:")
            opening(playerbox, prizes)

            print("Today you have won $", prizes[playerbox-1])
            print("Thank you for playing Deal or No!")

#End of Deal_or_No_0.3.py
#Coded by Todor Stefanov ;)
