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
    print("Stepping onto the temple grounds you're in awe of the sight before you.")
    print("What would you like to do first? \n 1.Throw a rock. Check for traps and circle the temple. \n 2.Charge forward!")

    choice = int(input("Enter a choice(number)> "))

    if choice == 1:
        print("You throw a rock, setting off some nearby traps that might've skewered you.")
        gremlin_enc()
    elif choice == 2:
        dead("You charge towards the temple with reckless abandon and are ripped apart by elaborate contraptions.")
    else:
        print("I don't know what that means.")

#gremlin event.
def gremlin_enc():
    print("Bypassing the traps you climb toward a secret entrance. It's guarded by a gremlin eating lunch.")
    print("The gremlin hasn't seen you.")
    print("What would you like to do? \n 1. Sneak on by. \n 2. Attack unawares.")

    enc_choice_1 = int(input("Enter a choice (number)> "))

    if enc_choice_1 == 1:
        print("You toss a noisemaker into a nearby bush. The gremlin drops his sandwich, annoyed and climbs down to investigate.")
        print("You sneak inside.")
        temple_room()
    elif enc_choice_1 == 2:
        print("You attack the goblin..unfortunately you weren't close enough to catch it off guard completely.")
        print("Your sword splits its sandwich as it scurries for its equipment and engages you in combat!")
        enc_1()
    else:
        print("I don't know what that means.")
#combat event
def enc_1():
    print("The gremlin charges you. It's wielding a short blade and a small shield.")
    print("What would you like to do? \n 1. Counterattack. \n 2. Dodge \n 3.Raise your shield.")

    enc_choice_2 = int(input("Enter a choice (number)> "")"))

    if enc_choice_2 == 1:
        #let the player choose their weapon for fun.
        weapon = input("What will you attack with? > ")

        #using the format method to add a placeholder inside the string. User input will be the weapon.
        print("You attempt to catch the gremlin off guard again with a quick strike of your {}.".format(weapon))
        print("The gremlin lets out a growl and deftly dodges your strike!")
        print("Surprised by your {} catching air you hesitate.".format(weapon))
        dead("The gremlin takes the opportunity to bury its blade in your stomach.")

    elif enc_choice_2 == 2:
        print("Readying yourself for the gremlins assault you watch its movements closely.")
        print("Feinting as if to attack, you bait the creature into striking at you.")
        print("Sidestepping the creatures strike you smirk before kicking it off the edge. Good job!")
        print("It's death scream probably alerted the rest though..")
        temple_room()
    elif enc_choice_2 == 3:
        print("You shield bash the gremlin into the wall following its charge, knocking it unconscious instantly.")
        print("Your shield was severely damaged in the process. You loot the gremlins remains and make do before proceeding into the temple.")
        temple_room()
    else:
        print("I don't know what that means.")
           

#starts the game
start()
