# Defining Phone Messaging System

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

        def addmessage(self, name, message, pausing=True):
            self.history.append(phonemessage(name,message))
            if pausing:
                renpy.pause()

        def delphone(self):
            self.history = []

# A dictionary of phone images
define who_chat = "Sabie"


image phonebg  = ConditionSwitch(

    "who_chat == 'Sabie'","phone/phone_sabie.png",
    "who_chat == 'Rohan'","phone/phone_rohan.png",
    "who_chat == 'Tyree'", "phone/phone_tyree.png",
    "who_chat == 'Group'", "phone/phone_gc.png",
    "who_chat == '???'", "phone/phone_un.png",
    )


# Open Phone Messaging System
label phone_open(clear_screen, name="Sabie", glide = True):

    $ who_chat = name

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
label message(name, word="", icon=False):

    # Sending the appropriate message
    if name == m:
        if icon == True:
            $ phone.addmessage("Image", "phone/P_Masami.png", False) # TODO: Change to Masami's Profile Pic!
        $ phone.addmessage("Masami", word)
    elif name == s:
        if icon == True:
            $ phone.addmessage("Image", "phone/P_Sabie.png", False) # TODO: Change to Sabie's Profile Pic!
        $ phone.addmessage("Sabie", word)
    elif name == r:
        if icon == True:
            $ phone.addmessage("Image", "phone/P_Rohan.png", False) # TODO: Change To Rohan's Profile Pic!
        $ phone.addmessage("Rohan", word)
    elif name == t:
        if icon == True:
            $ phone.addmessage("Image", "phone/P_Tyree.png", False) # TODO: Change To Tyree's Profile Pic!
        $ phone.addmessage("Tyree", word)
    elif name == "Image":
        # "word" is the image file name in this case
        $ phone.addmessage("Image", word)
    else:
        if icon == True:
            $ phone.addmessage("Image", "phone/P_un.png", False) # TODO: Change To ???'s Profile Pic!
        $ phone.addmessage("???", word)
    return
