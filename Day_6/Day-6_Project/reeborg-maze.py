#Paste this Code into the Reeborg Terminal and Observe how The Robot solves The Maze from Different Starting Positions.

def turn_right():
    for i in range(3):
     turn_left() # type: ignore

while front_is_clear(): # type: ignore
    move() # type: ignore
    
turn_left() # type: ignore

while not at_goal(): # type: ignore
    if right_is_clear(): # type: ignore
        turn_right()
        move() # type: ignore
    elif front_is_clear(): # type: ignore
        move() # type: ignore
    else:
        turn_left() # type: ignore
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
