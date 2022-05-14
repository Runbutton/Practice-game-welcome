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

def temple_room():
    print("You walk down a long passageway that appears to split in 2 directions.")
    print("A set of stairs descending down is to your right. To your left You see a large room.")
    print("What would you like to do? 1. Take the stairs. 2. Explore the room.")

    temple_choice = input("Enter a choice>")

    if temple_choice == 1:
        print("You descend the stairs into the worship chamber.")
        worship_room()
    elif temple_choice == 2:
        guards_sleep = 0
        print("You enter the guard quarters.")
        print("The guards appear to be sleeping. It would be wise not to spend too much time here..")
        print("You notice a key on a guards belt.")
        print("There is a sturdy looking shield on the far wall.")

        while guards_sleep < 3:
            guards_choice = input("What would you like to do? >")
            guards_sleep += 1
            if "key" in guards_choice:
                print("You quietly take the key.")
            elif "sword" in guards_choice:
                print("You take the sword..it's a little heavy for you.")
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

def worship_room():





#starts the game
start()
