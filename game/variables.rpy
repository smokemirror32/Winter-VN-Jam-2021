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

# Defining Phone Messaging System

init python:
    define.move_transitions("shake", 1.7)
transform shake (rate=0.090):
    xalign 0.5
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -15 yoffset 3
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -10 yoffset 2
    linear rate xoffset 0 yoffset 0

init python:
    import re
    yadjValue = float("inf")
    yadj = ui.adjustment()

    class phonemessage:
        def __init__(self, name, message):
            self.name = name
            self.message = message

    class phonelog:
        def __init__(self):
            self.history = []

        def addmessage(self, name, message):
            self.history.append(phonemessage(name,message))
            renpy.pause()

        def delphone(self):
            self.history = []

# Open Phone Messaging System
label phone_open(clear_screen, glide = True):

    if clear_screen == True:
        $ phone = phonelog()

    window hide
    if glide:
        show phonebg:
            ypos 1100
            xalign 0.5
        show phonebg:
            ease 0.7 ypos 0
            xalign 0.5
        $ renpy.pause (0.7,hard=True)
    show phonebg
    show screen nphone()
    $ renpy.pause (0.3,hard=True)

    return

# Close Phone Messaging System
label phone_close:

    hide screen nphone
    show phonebg:
        ypos 0
        xalign 0.5
    show phonebg:
        ease 0.7 ypos 1100
        xalign 0.5
    hide phonebg
    window show

    return

# Phone Messages
label message(name, word):

    if name == m:
        $ phone.addmessage("Masami", word)
    elif name == s:
        $ phone.addmessage("Sabie", word)
    elif name == r:
        $ phone.addmessage("Rohan", word)
    elif name == t:
        $ phone.addmessage("Tyree", word)
    else:
        $ phone.addmessage("???", word)
    return
