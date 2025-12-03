print("Welcome to teasure island.")
print("Your mission is to find the teasure.")
print("You're at a cross road. Where do you want to go?")
r_l=input(f"Type 'left' or 'right': ").lower()

if r_l == "right":
    print("You fell into a hole. Game Over.")
elif r_l == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    w_s=input(f"Type 'wait' to wait for a boat. Type 'swim' to swim across.: ").lower()
    if w_s== "swim":
        print("Game Over")
    elif w_s== "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        r_y_b=input(f"Which colour do you choose?: ").lower()
        if r_y_b == "red":
            print("It's a room full of fire. Game Over.")
        elif r_y_b == "blue":
            print("You enter a room of beasts. Game Over.")
        elif r_y_b == "yellow":
            print("You found the teasure! You Win!")    
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Game Over")
else:
    print("Pick a Valid Path.")
