# Defining choice being read variables
define rohan_unread = True
define sabie_unread = True
define tyree_unread = True
define kitchen_check = True
define upstairs_check = True
define graffiti_check = True
define car_check = True
define tracks_check = True

# Defining variables that matter for future decisions
define support = "None"
define sabie_trust = False
define rohan_respond = False
define sabie_respond = False
define tyree_respond = False
define alyssa_visit_first = True
define take_cookie = True
define kiss = True

# Defining Shake

init python:
    define.move_transitions("shake", 1.7)

transform shake (rate=0.090):
    xalign 0.5
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -15 yoffset 3
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -10 yoffset 2
    linear rate xoffset 0 yoffset 0
