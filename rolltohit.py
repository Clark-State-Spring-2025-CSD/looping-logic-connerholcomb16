#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.
#Video Link: https://youtu.be/89G5DN0-O3k

import random 

random.seed()

print("enter the number of dice and the hit target: ")

dicecount = int(input("number of dice: "))
hittarget = int(input("enter the hit target: "))

hitcount = 0
diceroll = 0

for i in range(dicecount):
    diceroll = random.randint(1,6)
    

if diceroll >= hittarget:
        hitcount += 1
        hitcount = hitcount + 1 

print (f"you rolled {dicecount} dice with a hit target of {hittarget} and hit {hitcount} times.")









