while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()
def jump_hurdle():
    turn_left()
while wall_on_right():
    move()
    turn_right()
    move()
    turn_right()
while not wall_in_front():
    move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()
