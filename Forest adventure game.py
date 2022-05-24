#We'll need this library for the die function.
from sys import exit

#die function
def dead(why):
    print(why, "What a shame!")
    exit(0)



#start of the game/first room
def start ():
    print("You're a treasure hunter lost in a dense forest.")
    print("Fortunately for you, a temple is in sight!")
    print("Stepping onto the temple grounds you're in awe of what lies before you.")
    print("What would you like to do first? \n 1.Throw a rock. Check for traps and circle the temple. \n 2.Charge forward!")


    choice = input("Enter a number or some text> ")

    if choice.isnumeric() == 1:
        print("You throw a rock, setting off some nearby traps that might've skewered you.")
        gremlin_enc()
    elif choice.isnumeric() == 2:
        dead("You charge towards the temple with reckless abandon and are ripped apart by elaborate contraptions.")
    else:
        print("You {}. is this really the time to be doing that?".format(choice))
        start()

#gremlin event.
def gremlin_enc():
    print("Bypassing the traps you climb toward a secret entrance. It's guarded by a gremlin eating lunch.")
    print("The gremlin hasn't seen you.")
    print("What would you like to do? \n 1. Sneak on by. \n 2. Attack unawares.")

    enc_choice_1 = input("Enter a number or some text> ")

    if enc_choice_1.isnumeric() == 1:
        print("You toss a noisemaker into a nearby bush. The gremlin drops his sandwich, annoyed and climbs down to investigate.")
        print("You sneak inside.")
        temple_room()
    elif enc_choice_1.isnumeric() == 2:
        print("You attack the goblin..unfortunately you weren't close enough to catch it off guard completely.")
        print("Your sword splits its sandwich as it scurries for its equipment and engages you in combat!")
        enc_1()
    else:
        dead("You {}. The gremlin notices you, sounds the horn and the grounds are covered in minutes.".format(enc_choice_1))


def enc_1():
    print("The gremlin charges you. It's wielding a short blade and a small shield.")
    print("What would you like to do? \n 1. Counterattack. \n 2. Dodge \n 3.Raise your shield.")

    enc_choice_2 = input("Enter a choice (number)> ")

    if enc_choice_2.isnumeric() == 1:
#let the player choose their weapon for fun.
        weapon = input("What will you attack with? > ")

        #using the format method to add a placeholder inside the string. User input will be the weapon.
        print("You attempt to catch the gremlin off guard again with a quick strike of your {}.".format(weapon))
        print("The gremlin lets out a growl and deftly dodges your strike!")
        print("Surprised by your {} catching air you hesitate.".format(weapon))
        dead("The gremlin takes the opportunity to bury its blade in your stomach.")

    elif enc_choice_2.isnumeric() == 2:
        print("Readying yourself for the gremlins assault you watch its movements closely.")
        print("Feinting as if to attack, you bait the creature into striking at you.")
        print("Sidestepping the creatures strike you kick it off the ledge. Good job!")
        print("Its death scream might have alerted the rest though..")
        temple_room()

    elif enc_choice_2.isnumeric() == 3:
        print("You shield bash the gremlin into the wall following its charge, knocking it unconscious instantly.")
        print("Your shield was severely damaged in the process. You loot the gremlins remains and make do before proceeding into the temple.")
        temple_room()
    else:
        dead("You  {}. The gremlin skewers you like a stuck pig.".format(enc_choice_2))
#temple room and guard event
def temple_room():
    print("You walk down a long passageway that appears to split in 2 directions.")
    print("A set of stairs descending down is to your right. To your left You see a large room.")
    print("What would you like to do? 1. Take the stairs. 2. Explore the room.")

    temple_choice = input("Enter a choice>")

    if temple_choice.isnumeric() == 1:
        print("You descend the stairs into the worship chamber.")
        worship_room()
    elif temple_choice.isnumeric() == 2:
        guards_sleep = 0
        print("You enter the guard quarters.")
        print("The guards appear to be sleeping. It would be wise not to spend too much time here..")
        print("You notice a satchel on a guards belt.")
        print("There is a sturdy looking shield on the far wall.")

        while guards_sleep < 3:
            guards_choice = input("What would you like to do? >")
            guards_sleep += 1
            if "satchel" in guards_choice:
                print("You quietly take the satchel.")
            elif "shield" in guards_choice:
                print("You take the shield..it's a little heavy.")
            elif guards_sleep == 3:
                print("The guards stir restlessly from their sleep..")
                dead("The guards awaken from their slumber. This isn't going to end well for you!")
            elif "leave" or "exit" in guards_choice:
                print("You return to the hallway quietly.")
                temple_room()
            else:
                print("You {}. Is this really the time to be doing that?".format(guards_choice))


    else:
        dead("You took too long! Creatures of the temple find you and rip you apart.")
#worship room
def worship_room():
    print("You enter the worship room. It's quite large and filled with sunlight.")
    print("Several gremlins are kneeling in prayer facing large statues of their presumable gods.")
    print("There are some double doors located behind the worshippers. It is slightly ajar.")
    print("They haven't noticed you.")

    worship_choice = input("What would you like to do?")

    if "door" or "sneak" in worship_choice:
        print("You sneak over to the gathering hall.")
        gathering_hall()
    else:
        dead("You {}. The commotion disturbs the creatures worship and enrages them. You are then sacrificed to appease the gods!".format(worship_choice))
#gathering hall
def gathering_hall():
    print("You enter the gathering hall.")
    print("There is a prepared snack on the table and some footsteps nearby.")
    print("You should probably hide..but you're hungry.")
    print("Will you take the snack or hide?")

    hall_choice = input("What would you like to do?")

    if "snack" in hall_choice:
        print("You devour the snack greedily.")
        print("An ogre is in the doorway with a tear in its eye.")
        print("\"MY SNACK!!\" it shouts angrily as it charges toward you!")
        ogre_enc()
    elif "hide" in hall_choice:
        print("You hide under the large wooden table.")
        print("An ogre enters the room, sits down and begins eating its snack.")
        print("You quietly make your way over to the door it emerged from.")
        treasure_room()
    else:
        dead("You {}. The foosteps get louder as an ogre enters the room and promptly crushes your skull.".format(hall_choice))
#ogre encounter
def ogre_enc():
print("The ogre is barrelling toward you blindly at a high speed.")
print("It is likely to smash you to paste if you don't act quickly!")

ogre_choice = input("What would you like to do?")

if "dodge" or "move" in ogre_choice:
    print("You step out of the way of the rampaging ogre.")
    print("The ogre slams into the door to the worship room, collapsing it.")
    print("The ogre appears to be stunned..you hear a commotion on the other side of the rubble.")
    print("deciding not to wait around, you move along..")
    treasure_room()
elif "attack" or "strike" or "fight" or "weapon" or "sword" in ogre_choice:
    print("you hold your weapon out, attempting to impale the rampaging ogre.")
    print("the weapon embeds itself firmly between the ogres eyes! However the weight of the beast slams into you as it cries in pain.")
    print("with these injuries you likely won't be going anywhere. It  will be a long wait while the ogre recovers.")
    dead("...or maybe not. The commotion seems to have attracted the attention of the worshippers..")
else:
    dead("The ogre grips you with great force and squeeze til your eyes pop out as you {}.".format(ogre_choice))

def treasure_room():
    print("You lay your eyes upon a valuable looking gem..you made it!")
    print("Congratulations!")
    exit(0)




#starts the game
start()
