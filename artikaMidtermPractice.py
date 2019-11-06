"""
Name:  artikaMidtermPractice.py
Programmer:  artikacat
Date(s) of Development: 10/7/19 - 10/9/19
"""


import random
import time
readyName = "N"
readyStart = "N"
displayDiff = ""
invent = ["FLASHLIGHT"]
matchCount = 5


def main():
    opening()
    landing()
    roof()
    ladder()
    centralRoom()
    preCombat()
    combat(matchCount)
    endcard()

#portal transition setup
def portal(length):
    loop = 0
    while loop < length:
        time.sleep(0.1)
        print("""/\\//\\//\\//\\//\\//\\//\\//\\//\\/
\//\\//\\//\\//\\//\\//\\//\\//\\//\ """)
        loop += 1
    print("\n")

#text reading functions setup
def read(msg, speed = 0.035):
    for ch in msg:
        print(ch,end='')
        time.sleep(speed)
    print("\n")

def pause(delay = 0.5, msg = "..."):
    time.sleep(delay)
    read(msg)
    time.sleep(delay)
    
def sfx(msg, speed = 0.001):
    read(msg, speed)

#define actions
def pressButton1():
    read("\nYou decided to press the button. At first, nothing happens. Then...")
    sfx("\n*rumble-rumble*")
    read("\nA building begins to rise from underneath you!")
    sfx("\n*rumble-rumble*")
    read("\nAs the building rises, it shakes violently, knocking you down. Most of the dust \
is sifted off.")
    sfx("\n*rumble-rumble*")
    sfx("\n*rumble-rumble*")
    sfx("\n*click!*")
    pause(0.75)
    read("\nThe building has stopped shaking, and is now several feet above the planet's surface.")

def lookAround1():
    read("\nYou look around. There seems to be nothing there, no matter what direction you turn.\n\
It is but a wasteland of dust and craters.")

def pressButton2():
    read("\nYou decided to press the button.")
    pause()
    sfx("\n*whirrr*")
    sfx("\n*click!*")
    read("\nOh?")
    read("\nA panel slid open on the side of the podium.")
    pause()
    read("\nInside is a key!")
    sfx("\n*shff*")
    read("\nYou put it in your pocket.")
    read("\nYou have acquired OLD KEY.", 0.1)
    
def pressButton3():
    read("\nYou decided to press the button.")
    pause()
    read("\nNothing happened.")
    
def lookAround2():
    read("\nYour view is pretty much the same as from the ground, except you're much higher up now.")
    read("\nYou walk over to the edge of the roof.")
    pause()
    read("\nIt's really high up. Like, really.")
    read("\nMaybe it's not the best time to be practicing your parkour skills?")
    pause()

def tryHatch1():
    read("\nYou decided to try the hatch.")
    read("\nWalking over to the hatch, you give its handle a light tug.")
    sfx("\n*creeeaaak*")
    read("\nHmm...it didn't budge.")
    read("\nYou give it another (slightly stronger) tug.")
    sfx("\n*creeeaaak*")
    read("\nDrat, it's no good.")
    pause()
    read("\nOh?")
    time.sleep(0.2)
    read("\nThere's a keyhole?")
    read("\nMaybe there's a key lying around here somewhere...")
    pause()
    
def tryHatch2():
    read("\nMaybe there's a key lying around here somewhere...")
    
def tryHatch3():
    read("\nYou use the OLD KEY to unlock the hatch.")
    sfx("\n*k'chak*")
    read("\nThe hatch is now open!")

def inventory():
    read("\nYou decided to check your INVENTORY.")
    sfx("*shf*")
    print("You have...")
    print(invent)
    pause()

def inventorySplashes(action):
    if (action == "BUTTER KNIFE" or action == "butter knife") and "BUTTER KNIFE" in invent:
        read("\nThe BUTTER KNIFE is very blunt. It probably couldn't even slice through butter!")
        pause()
    elif (action == "CANDLESTICK" or action == "candlestick") and "CANDLESTICK" in invent:
        read("\nThe CANDLESTICK looks brand new, no wax drippings at all. Maybe someone was saving it for a special occasion.")
        combine = input("\nThe CANDLESTICK would drip wax onto you if you tried to light it in its current state. Combine with CANDLE HOLDER? Y or N  ")
        if combine == "Y" or combine == "y":
            sfx("*shp*")
            read("\nYou have combined the CANDLESTICK and the CANDLE HOLDER to make the CANDLE.")
            invent.remove("CANDLESTICK")
            invent.remove("CANDLE HOLDER")
            invent.append("CANDLE")
    elif (action == "CANDLE HOLDER" or action == "candle holder") and "CANDLE HOLDER" in invent:
        read("\nThe CANDLE HOLDER looks old and very ornate. It has something that looks like a craftsman's seal stamped on the bottom,\n\
but it's too obscure to make out. There is a lot of residual wax on it, but it seems to have no structural problems.")
        combine = input("\nThe CANDLE HOLDER, although beautiful, has no purpose in its current state. Combine with CANDLESTICK? Y or N  ")
        if combine == "Y" or combine == "y":
            sfx("*shp*")
            read("\nYou have combined the CANDLESTICK and the CANDLE HOLDER to make the CANDLE.")
            invent.remove("CANDLESTICK")
            invent.remove("CANDLE HOLDER")
            invent.append("CANDLE")
    elif (action == "CANDLE" or action == "candle") and "CANDLE" in invent:
            read("\nThe new CANDLESTICK and ornate CANDLE HOLDER are in their correct places. There's something quite rustic about a CANDLE.")
    elif action == "FLASHLIGHT" or action == "flashlight":
            read("The FLASHLIGHT is still on. If you turned it off, you wouldn't be able to see. Let's not do that.")
    elif action == "MATCHES" or action == "matches":
        read("\nnYou brush your thumb on the weathered paper. The box is old, but still in good shape. The striker plate appears unused.")
        read("\nThere are " + matchCount + " MATCHES in the box.")

def blue1():
    read("\nYou decided to pull the BLUE lever.")
    sfx("\n*k'klunk*")
    pause()
    read("\nThere is a metallic noise from the EAST. The lever is DOWN.")
    pause()
    return True
def blue2():
    read("\nYou decided to return the BLUE lever to its original position.")
    sfx("\n*k'klunk*")
    pause()
    read("\nThere is a metallic noise from the EAST. The lever is UP.")
    pause()
    return False
def yellow1():
    read("\nYou decided to flip the YELLOW switch.")
    pause()
    pause()
    read("\nThe YELLOW switch does not budge.")
    pause()
def yellow2():
    read("\nYou decided to flip the YELLOW switch.")
    pause()
    read("\nThe YELLOW switch moves!")
    sfx("*krrrrrrrrrrrrk*", 0.1)
    sfx("*rrrrrrr*")
    sfx("*klunk*")
    read("\nThere is a metallic noise from the WEST.")
def red1():
    read("\nYou decided to flip the RED switch.")
    pause()
    read("\nThat didn't do anything. The RED switch is DOWN.")
    pause()
    return True
def red2():
    read("\nYou decided to return the RED switch to its original position.")
    pause()
    read("\nThat didn't do anything. The RED switch is UP.")
    pause()
    return False
def green1():
    read("\nYou decided to press the GREEN button.")
    pause()
    sfx("\n*plink!*")
    read("\nThe screen turned on!")
    pause()
    read("\nAh...", 0.2)
    read("\nThere's text in a language you can't read.")
    pause()
def green2():
    read("\nYou decided to press the GREEN button again, but the screen stays on.")
    pause()
def green3():
    sfx("\n*plink!*")
    read("\nHuh. The screen turned off.")
def north1():
    read("\nYou have decided to investigate the NORTH.")
    sfx("\n*tnk tnk tnk tnk*")
    pause()
    read("\nThere appears to be a control board underneath the monitor. There is a BLUE lever, a YELLOW switch, a RED switch, and a GREEN button.")
    choiceMade = False
    redPOS = False
    greenCount = 0
    greenTriggered = False
    yellowActive = False
    bluePOS = False
    while choiceMade == False:
        action = input("What would you like to do? Interact with BLUE, YELLOW, RED, or GREEN, or RETURN to the ladder.  ")
        if action == "INVENTORY" or action == "inventory":
            inventory()
        elif action == "RETURN" or action == "return":
            return bluePOS, yellowActive
        elif (action == "BLUE" or action == "blue") and bluePOS == False:
            bluePOS = blue1()
        elif (action == "BLUE" or action == "blue") and bluePOS == True:
            bluePOS = blue2()
        elif (action == "YELLOW" or action == "yellow") and not(greenCount == 3 and redPOS == True and "MATCHES" in invent and ("CANDLE" in invent or "CANDLESTICK" in invent)):
            yellow1()
        elif (action == "RED" or action == "red") and redPOS == False:
            redPOS = red1()
        elif (action == "RED" or action == "red") and redPOS == True and greenCount > 1:
            redPOS = red2()
            greenCount = 0
            green3()
            pause()
        elif (action == "RED" or action == "red") and redPOS == True and greenCount == 1:
            redPOS = red2()
        elif (action == "GREEN" or action == "green") and greenCount == 0:
            green1()
            greenCount += 1
        elif (action == "GREEN" or action == "green")  and greenCount == 1 and redPOS == False:
            green2()
        elif (action == "GREEN" or action == "green") and greenCount in range(1, 3) and redPOS == True:
            green2()
            greenCount += 1
        elif (action == "GREEN" or action == "green") and greenCount >= 3:
            green3()
            greenCount = 0
        elif (action == "YELLOW" or action == "yellow") and greenCount == 3 and redPOS == True and "MATCHES" in invent and ("CANDLE" in invent or "CANDLESTICK" in invent):
            yellow2()
            yellowActive = True
            return bluePOS, yellowActive
        elif action.upper() in invent:
            inventorySplashes(action)
        else:
            read("You can't do that here.")
    return bluePOS, yellowActive

def west1():
    read("\nYou have decided to investigate the WEST.")
    read("\nYou try to spin the wheel on the door.")
    sfx("\n*krrrrrrk*")
    pause()
    read("\nNo good. It's locked.")
    pause()

def west2():
    read("\nYou have decided to investigate the WEST.")
    read("\nYou try to spin the wheel on the door.")
    sfx("\n*krrrrrrrrrrr*")
    pause()
    read("The door is open. All that's left to do is to head inside.")
    pause()
    
def east1(bluePOS = False):
    read("\nYou have decided to investigate the EAST.")
    read("\nThere are 5 small cabinets adjacent to the desk, which has 2 drawers.")
    choiceMade = False
    cabinetGet = False
    drawerGet = False
    deskCheck = False
    while choiceMade == False:
        action = input("What would you like to check? Inside the CABINETS, on top of the DESK, or inside the DRAWERS? You can always RETURN to the ladder.  ")
        if action == "INVENTORY" or action == "inventory":
            inventory()
        elif action == "RETURN" or action == "return":
            return cabinetGet, drawerGet, deskCheck
        elif (action == "CABINETS" or action == "cabinets") and bluePOS == False and cabinetGet == False:
            read("\nThe fronts of the cabinets are blocked by metal sliding doors.")
            pause()
            read("\nThere must be some way to get around that, but you don't see any clues on the cabinets themselves.")
        elif (action == "CABINETS" or action == "cabinets") and bluePOS == True and cabinetGet == False:
            read("The cabinets are empty, save for a box of MATCHES in one. As you reach up to grab the MATCHES, \n\
you notice that the backgrounds of the cabinets are strangely colored.")
            print("""First cabinet:  GREEN
Second cabinet:  RED
Third cabinet:  GREEN
Fourth cabinet:  GREEN
Fifth cabinet:  YELLOW""")
            read("\nMATCHES acquired!", 0.1)
            invent.append("MATCHES")
            cabinetGet = True
            pause()
        elif (action == "CABINETS" or action == "cabinets") and bluePOS == False and cabinetGet == True:
            read("\nYou already obtained the MATCHES from the cabinets. The sliding doors are CLOSED.")
        elif (action == "CABINETS" or action == "cabinets") and bluePOS == True and cabinetGet == True:
            read("\nYou already obtained the MATCHES from the cabinets. The cabinets have strange backgrounds!")
            print("""First cabinet:  GREEN
Second cabinet:  RED
Third cabinet:  GREEN
Fourth cabinet:  GREEN
Fifth cabinet:  YELLOW""")
        elif action == "DESK" or action == "desk":
            read("\nThe wooden desk is covered in dust, and there are notes strewn about that are written in a language you don't understand.")
            pause()
            read("\nUpon closer inspection, there are many gashes in the surface of the wood. Maybe someone cut vegetables here?")
            pause()
            read("\nSpace vegetables?")
            pause()
            deskCheck = True
        elif (action == "DRAWERS" or action == "drawers") and drawerGet == False:
            read("\nThe wood has warped, so these drawers are a little hard to open. However, with enough tugging--")
            sfx("*k-klunk!*")
            read("\n...you were able to force them open.")
            pause()
            read("\nThe left drawer contains a BUTTER KNIFE. Acquired BUTTER KNIFE!")
            invent.append("BUTTER KNIFE")
            pause()
            read("\nThe right drawer contains a CANDLESTICK and a CANDLE HOLDER. CANDLESTICK and CANDLE HOLDER acquired!")
            invent.append("CANDLESTICK")
            invent.append("CANDLE HOLDER")
            pause()
            drawerGet = True
        elif (action == "DRAWERS" or action == "drawers") and drawerGet == True:
            sfx("*k-klunk!*")
            pause()
            read("\nThe drawers are empty.")
            pause()
        elif action.upper() in invent:
            inventorySplashes(action)
        else:
            read("You can't do that here.")
        
#open
def opening():
    readyName = "N"
    readyStart = "N"
    displayDiff = ""
    read("This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. Visit https://creativecommons.org/licenses/by-nc-sa/4.0/ for more details.")
    read("\nEnjoy! -artikacat")
    time.sleep(1)

#landing
def landing():
    read("You land on a dry, dusty planet. There is no sun, but it is somehow not dark or cold; the terrain is pitted\nwith craters and crevices. A small podium with a big red button on it stands before you.")
    choiceMade = False
    while choiceMade == False:
        action = input("What would you like to do? You can PRESS the button or LOOK around.  ")
        if action == "PRESS" or action == "press":
            pressButton1()
            choiceMade = True
        elif action == "LOOK" or action == "look":
            lookAround1()
            read("All that's left is to PRESS the button.")
        else:
            read("\nYou can't do that here.")

#looking around the roof
def roof():
    read("Where there once was a layer of dust, a hatch is seen embedded into the roof. You can probably get in the building that way.")
    choiceMade = False
    hatchKey = False
    alreadyTried = False
    tryhatch3 = False
    while choiceMade == False:
        action = input("What would you like to do? You can PRESS the button, LOOK around, or TRY the hatch.  ")
        if (action == "PRESS" or action == "press") and hatchKey == False:
            pressButton2()
            hatchKey = True
            invent.append("OLD KEY")
        elif (action == "PRESS" or action == "press") and hatchKey == True:
            pressButton3()
        elif action == "LOOK" or action == "look":
            lookAround2()
        elif (action == "TRY" or action == "try") and hatchKey == False and alreadyTried == True:
            tryHatch2()
        elif (action == "TRY" or action == "try") and hatchKey == False and alreadyTried == False:
            tryHatch1()
            alreadyTried = True
        elif (action == "TRY" or action == "try") and hatchKey == True and tryhatch3 == False:
            tryHatch3()
            moveOn = input("Are you ready to move on? Y or N  ")
            tryhatch3 = True
            if moveOn == "Y" or moveOn == "y":
                choiceMade = True
            else:
                continue
        elif (action == "TRY" or action == "try") and tryhatch3 == True:
            moveOn = input("Are you ready to move on? Y or N  ")
            if moveOn == "Y" or moveOn == "y":
                choiceMade = True
            else:
                continue
        else:
            read("You can't do that here.")

#entering the base
def ladder():
    sfx("\n*clunk clunk clunk clunk*")
    read("\nYou descend a steel ladder into utter darkness.")
    sfx("\n*clunk clunk clunk clunk*")
    sfx("\n*clunk clunk clunk clunk*")
    read("\nThe ladder has to end sometime, right? It seems pretty...long...")
    sfx("\n*clunk clunk clunk clunk*")
    sfx("\n*clunk clunk clunk clunk*")
    read("\nAt last! You have reached the bottom rung.")
    read("\nYou step gingerly onto the floor.")
    pause()
    read("\nYou still can't really see anything... Maybe you have something in your INVENTORY that would help?")
    read("\nACQUIRED NEW ABILITY:  INVENTORY CHECK!\nType 'INVENTORY' any time you wish to access your obtained items.")
    choiceMade = False
    while choiceMade == False:
        action = input("Try checking your INVENTORY.  ")
        if action == "INVENTORY" or action == "inventory":
            inventory()
            print("Huh! Maybe that FLASHLIGHT will come in handy.")
            choiceMade = True
        else:
            read("You can't do that here.")
    read("You can use an item from your INVENTORY by inputting its name, even if it is not one of the available actions.")
    choiceMade = False
    while choiceMade == False:
        action = input("\nWhat do you want to do?  ")
        if action == "INVENTORY" or action == "inventory":
            inventory()
            print("Huh! Maybe that FLASHLIGHT will come in handy.")
        elif action == "FLASHLIGHT" or action == "flashlight":
            sfx("\n*klik*")
            read("You decided to use your FLASHLIGHT.")
            read("Wow! That's bright.\nYou can now see the interior of the room.")
            choiceMade = True
        elif action == "OLD KEY" or action == "old key":
            read("It's too dark to find a use for this.")
        else:
            read("You can't do that here.")

def centralRoom():
    read("\nThere is a giant monitor to the NORTH of the ladder. The screen is black, but it looks to be in good shape.")
    read("\nTo the WEST of the ladder is an industrial-looking door. It has a large, wheel-style opening mechanism, and is covered in dust.")
    read("\nTo the EAST of the ladder is a set of cabinets and a desk.")
    choiceMade = False
    cabinetGet = False
    drawerGet = False
    deskCheck = False
    yellowActive = False
    bluePOS = False
    while choiceMade == False:
        action = input("\nWhere would you like to investigate? You can go NORTH, WEST, or EAST.  ")
        if action == "INVENTORY" or action == "inventory":
            inventory()
        elif action.upper() in invent:
            inventorySplashes(action)
        elif action == "NORTH" or action == "north":
            bluePOS, yellowActive = north1()
        elif action == "WEST" or action == "west" and yellowActive == False:
            west1()
        elif action == "WEST" or action == "west" and yellowActive == True:
            west2()
            choiceMade = True
        elif action == "EAST" or action == "east":
            east1(bluePOS)
        else:
            read("You can't do that here.")

def preCombat():
    read("\nYou open the door…", 0.05)
    sfx("*creak*")
    pause()
    read("\nYou shine your FLASHLIGHT into the passage.")
    read("\nIt illuminates a dark mass. Oil, perhaps?")
    sfx("*glork glork*")
    read("\nOh… ", 0.1)
    read("There’s something inside…", 0.04)
    skipTutorial = input("Do you already know how to fight? Y or N  ")
    if skipTutorial == "Y" or skipTutorial == "y":
        print("The tutorial has been skipped.")
    else:
        read("\nFighting in this game is pretty simple. \nJust enter the action you would like to perform when prompted to do so!")
        read("\nHowever, be careful not to waste actions. After each move, you will take damage, regardless of your choice.")        
        read("Good luck!")
        pause()
             
def talk(messageFound):
    talkChoice = random.randint(1,3)
    read("You decide to talk to the pile of muck.")
    if talkChoice == 1:
        sfx("*brbl brbl*")
        pause()
        read("It doesn't seem to have anything to say right now.")
        messageFound = messageFound
    elif talkChoice == 2:
        sfx("*klk klk*")
        read("Bubbles pop, and a mouth you didn't know was there opens.")
        read("'I t ' s  s o  d a r k . . .'", 0.1)
        messageFound = True
    elif talkChoice == 3:
        sfx("*klk klk*")
        read("A wind softly whispers through the chamber.")
        messageFound = messageFound
    pause()
    return messageFound
        
def fight(equippedWeapon, globHealth, matchCount):
    if equippedWeapon == "NONE":
        read("\nYou ball a fist and punch the glob monster.")
        pause()
        read("\nThat didn't do anything. Congratulations, your hands are mucky and gross.")
        globHealth = globHealth
    elif equippedWeapon == "OLD KEY":
        read("\nYou toss the OLD KEY at the glob monster.")
        sfx("*plop*")
        sfx("*sizzle sizzle*")
        read("\nIt dissolved the OLD KEY!")
        invent.remove("OLD KEY")
        equippedWeapon = "NONE"
        globHealth = globHealth - 2
    elif equippedWeapon == "BUTTER KNIFE":
        read("\nYou stab the glob monster with the astonishingly blunt BUTTER KNIFE.")
        sfx("*sizzle sizzle*")
        read("\nIt dissolved the blade!")
        invent.remove("BUTTER KNIFE")
        equippedWeapon = "NONE"
        globHealth = globHealth - 4
    elif equippedWeapon == "CANDLESTICK":
        read("\nYou throw the CANDLESTICK at the glob monster.")
        sfx("*klk klk*")
        read("Bubbles pop, and a mouth you didn't know was there opens.")
        read("'F O O L I S H   M O R T A L . . .'", 0.1)
        read("Uh-oh.")
        read("It gobbled it up.")
        invent.remove("CANDLESTICK")
        equippedWeapon = "NONE"
        globHealth = 666
    elif equippedWeapon == "CANDLE HOLDER":
        read("\nYou throw the CANDLE HOLDER at the glob monster.")
        sfx("*klk klk*")
        read("Bubbles pop, and a mouth you didn't know was there opens.")
        read("'F O O L I S H   M O R T A L . . .'", 0.1)
        read("Uh-oh.")
        read("It gobbled it up.")
        invent.remove("CANDLE HOLDER")
        equippedWeapon = "NONE"
        globHealth = 666
    elif equippedWeapon == "CANDLE":
        if matchCount > 0:
            read("\nYou hold the CANDLE in your hand, and you take out a MATCH.")
            read("\nYou strike the MATCH.")
            sfx("*shfffffff*")
            read("\nAs the glob monster watches curiously, you light the CANDLE.")
            read("\nYou drop the CANDLE onto the GLOB MONSTER.")
            sfx("*plop*")
            read("\nIt absorbs the lit CANDLE, and it glows from the inside. Satisfied, the monster slithers away.")
            invent.remove("CANDLE")
            equippedWeapon = "NONE"
            globHealth = 0
            matchCount -= 1
        elif matchCount == 0:
            read("\nYou throw the CANDLE at the glob monster.")
            sfx("*boink*")
            read("\nIt bounced off!")
            invent.remove("CANDLE")
            equippedWeapon = "NONE"
            globHealth = globHealth
    elif equippedWeapon == "FLASHLIGHT":
        read("Without this flashlight, you would be unable to see the glob monster. It would be unwise to use it as a weapon.")
        globHealth = globHealth
    elif equippedWeapon == "MATCHES":
        if matchCount > 0:
            matchCount -= 1
            sfx("*shfffffff*")
            read("\nYou strike a MATCH as the glob monster watches curiously.")
            read("\nYou drop the MATCH onto the glob monster.")
            pause()
            read("\nThe MATCH is snuffed out.")
            globHealth = globHealth - 1
        elif matchCount == 0:
            read("All out of those, buddy.")
            globHealth = globHealth
    return globHealth

def combat(matchCount):
    equippedWeapon = "NONE"
    globHealth = 20
    playerHealth = 50
    messageFound = False
    while globHealth > 0 and playerHealth > 0:
        read("\n<GLOB MONSTER> has " + str(globHealth) + " health!")
        read("\nYou have " + str(playerHealth) + " health!")
        read("\n<GLOB MONSTER> sprays you with goop, and you take 5 damage.")
        playerHealth += -5
        read("\nWhat would you like to do?")
        if messageFound == True:
            action = input("FIGHT, EQUIP, INVENTORY:  ")
        else:
            action = input("TALK, FIGHT, EQUIP, INVENTORY:  ")
        
        if action == "TALK" or action == "talk" and messageFound == False:
            messageFound = talk(messageFound)
        elif action == "FIGHT" or action == "fight":
            globHealth = fight(equippedWeapon, globHealth, matchCount)
        elif action == "EQUIP" or action == "equip":
            inventory()
            successfulEquip = False
            while successfulEquip == False:
                read("What would you like to equip?")
                equippedWeapon = input()
                equippedWeapon = equippedWeapon.upper()
                if equippedWeapon in invent:
                    read("You have equipped:  " + equippedWeapon)
                    successfulEquip = True
                else:
                    read("Invalid input.")
        elif action == "INVENTORY" or action == "inventory":
            inventory()
        elif action.upper() in invent:
            inventorySplashes(action)
        else:
            read("\nYou can’t do that here.")
            continue
    endcard()

def endcard():
    pause()
    read("GAME OVER", 0.2)
    pause()
    read("Hey! Thanks for playing. I had a lot of fun making this game, and I hope you enjoyed playing it. I know it's short, but I might make a sequel sometime, so look out for that! \
Who knows. :) Thanks again!")
    print("--program end--")

if __name__ == "__main__":
    main()
        

   
