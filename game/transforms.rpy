# Defining Shake

init python:
    define.move_transitions("shake", 1.7)

transform shake (rate=0.090):
    xalign 0.5
    linear rate xoffset -15 yoffset 3
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -10 yoffset 2
    linear rate xoffset 0 yoffset 0

# Defining Bounce

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    #repeat

# Defining Innerright

transform innerright:
    xalign 0.6
