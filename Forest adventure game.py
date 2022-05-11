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
    print("Bypassing the traps you move toward a secret entrance. It's guarded by a gremlin eating lunch.")
    print("The gremlin hasn't seen you.")
    print("What would you like to do? \n 1. Sneak on by. \n 2. Attack unawares.")

    enc_choice_1 = int(input("Enter a choice (number)> "))

    if enc_choice_1 == 1:
        print("You toss a noisemaker into a nearby bush. The gremlin drops his sandwich, annoyed and hobbles off to investigate.")
        print("You sneak inside.")
        temple_room()
    elif enc_choice_1 == 2:
        print("You attack the goblin..unfortunately you weren't close enough to catch it off guard completely.")
        print("Your sword splits its sandwich as it scurries for its equipment and engages you in combat!")
        enc_1()
    else:
        print("I don't know what that means.")

#starts the game
start()
