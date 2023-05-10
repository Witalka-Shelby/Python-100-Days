def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear() and wall_in_front():
        turn_right()
        if is_facing_north() == True:
            move()
    while wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()

    else:
        move()