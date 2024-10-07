print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")
choice1 = input("You're at crossroad , where do you want to go ? Type left or right \n").lower()
if choice1 == "left" :
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type wait to wait for boat or type swim to swim across.\n").lower()
    if choice2 == "wait" :
        choice3 = input("You've arrived at the island unhamrmed. There is house with 3 doors. One is red , one is yellow and one is blue. Which door do you choose ? \n").lower()
        if choice3 == "red" :
            print("Room is full of fire.\nYou Lose.\nGame over.\n")
        elif choice3 == "yellow" :
            print("You found the treasure.\nYou Win.\nGame over.\n")
        elif choice3 == "blue" :
            print("You are eaten by beasts.\nYou Lose.\nGame Over.\n")
        else :
            print("Door does not exist.\nPlease choose valid door.\n")
    else :
        print("You are attacked by Sharks.\nYou Lose.\nGame Over.\n")
else :
    print("You fell into a hole.\nYou Lose.\nGame Over.\n")