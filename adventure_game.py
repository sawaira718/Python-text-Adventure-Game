import random
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def displayIntro():
    print_pause("You are on the way to your house in a rainy night. ")
    print_pause("You come to a crossroad 2 paths one path leads home.")
    print_pause("Roumor has that there is an evil near the house.")
    print_pause("What would you like to do?")
    print_pause("Enter 1 to choose path 1")
    print_pause("Enter 2 to choose path 2")


def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("what path will you choose? (1 or 2):")
    return int(path)


def check_path(choosePath):
    if choosePath == 1:
        print_pause("You are on your way!")
    else:
        print_pause("You chosed second path. Good Luck!")
    print_pause("Oops! You are infornt of an evil")
    print_pause("You are searching for somthing to fight")


def fight():
    weapon = random.choice(["dagger", "Gun", "Pike", "sabre"])
    print_pause("You have found " + weapon)
    fight = random.randint(1, 2)
    if fight == 1:
        print_pause("You try your best! but you lose")
    else:
        print_pause("Brave, you fight well. Welcome Home! You Win!")


def play_again():
    response = input("Would you like to play again? "
                     "Please enter 'y' or 'n'.\n")
    if "n" in response:
        print_pause("OK, goodbye!")
    elif "y" in response:
        print_pause("Very good.")
        again()


def again():
    path = choosePath()
    check_path(path)
    fight()
    play_again()


def adventure_game():
    displayIntro()
    path = choosePath()
    check_path(path)
    fight()
    play_again()


adventure_game()
