# Player starts at 1,1 and can only move north
# We tell the player what directions he can move to
# If he enters a direction which is not available we print not a valid direction and let him try again
# Player wins when he gets to the tile 3,1, and we print out Victory!
# Directions the player can move to in each tile:
# 1,1 -> N
# 1,2 -> N, E, S
# 1,3 -> E, S
# 2,1 -> N
# 2,2 -> W, S
# 2,3 -> E, W
# 3,1 -> Victory!
# 3,2 -> N, S
# 3,3 -> W, S

north = "(N)orth"
east = "(E)ast"
west = "(W)est"
south = "(S)outh"

i = 1
j = 1
# (i,j)
while True:
    if j == 1 and i == 1:
        print("You can travel: ", north)
        d = input("Direction: ")
        if d == "n" or d == "N": #1,1
            j += 1
        else:
            print("Not a valid direction!")
    elif j == 2 and i == 1: #1,2
        print("You can travel: ", north, "or", east, "or", south)
        d = input("Direction: ")
        if d == "n" or d == "N":
            j += 1 #1,3
        elif d == "e" or d == "E":
            i += 1 #2,2
        elif d == "s" or d == "S":
            j -= 1 #1,1
        else:
            print("Not a valid direction!")
    elif j == 3 and i ==1: #1,3 
        print("You can travel: ", east, "or", south)
        d = input("Direction: ")
        if d == "e" or d == "E":
            i += 1 #2,3
        elif d == "s" or d == "S":
            j -= 1 #1,2
        else: 
            print("Not a valid direction!")
    elif j == 1 and i == 2: #2,1
        print("You can travel: ", north)
        d = input("Direction: ")
        if d == "n" or d == "N":
            j += 1 #2,2
        else: 
            print("Not a valid direction!")
    elif j == 2 and i == 2: #2,2
        print("You can travel: ", west, "or", south)
        d = input("Direction: ")
        if d == "w" or d == "W":
            i -= 1 #1,2
        elif d == "s" or d == "S":
            j -= 1 #2,1
        else: 
            print("Not a valid direction!")
    elif j == 3 and i == 2: #2,3
        print("You can travel: ", east, "or", west)
        d = input("Direction: ")
        if d == "e" or d == "E":
            i += 1 #3,3
        elif d == "w" or d == "W":
            i -= 1 #1,3
        else: 
            print("Not a valid direction!")
    elif j == 1 and i == 3: #3,1
        print("Victory!")
        break
    elif j == 2 and i == 3: #3,2
        print("You can travel: ", north, "or", south)
        d = input("Direction: ")
        if d == "n" or d == "N":
            j += 1 #3,3
        elif d == "s" or d == "S":
            j -= 1 #3,1
    elif j == 3 and i == 3: #3,3
        print("You can travel: ", west, "or", south)
        d = input("Direction: ")
        if d == "w" or d == "W":
            i -= 1 #2,3
        elif d == "s" or d == "S":
            j -= 1 #3,2
    else:
        print("not a valid direction!")
