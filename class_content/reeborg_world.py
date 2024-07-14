#**********************  Understanding concept with Reeborg's World ****************
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# Do this :
# move()
# move()
# turn_left()
# turn_left()
# move()
# move()
# turn_left()
# turn_left()
# * Do this using functions
# def turn_around():
#     turn_left()
#     turn_left()

# move()
# # move()
# turn_around()
# # move()
# # move()
# turn_around()

# Create a spearate program to turn the robot right
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# Create a program to draw the square
# def turn square
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()

# Challenge -- hurdle 1
# def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(6):
#     jump()

#************** Hurdle race 1 ---- reeborg's world ***************************************
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for step in range(6):
#     jump()

#************** Hurdle race 3 ---- reeborg's world ***************************************
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#************** Hurdle race 4 ---- reeborg's world ***************************************
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#************** Maze ---- reeborg's world ***************************************
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()