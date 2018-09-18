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

print("You can travel: ", north)

while True:
    d = input("Direction: ")
    if d == "n" or d == "N":
        print("You can travel: ", north,"or", east, "or", south)
    else:
        print("Not a valid direction!")
        if d == "n" or d == "N":
            print("You can travel: ", south, "or", east)
            if d == "e" or d == "E":
                print("You can travel: ", east, "or", west)
            elif d == "s" or d == "S":
                print("You can travel: ", north, "or", east, "or", south)
            else:
                print("Not a valid direction!")
        elif d == "e" or d == "E":
            print("You can travel: ", west, "or", south)
            if d == "w" or d == "W":
                print("You can travel: ", north, "or", east, "or", south)
            elif d == "s" or d == "S":
                print("You can travel: ", north)
        elif d == "s" or d == "S":
            print("You can travel:", north)
        else:
            print("Not a valid direction!")

    