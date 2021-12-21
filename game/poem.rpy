# Just a test block :)
label test_block:

    scene bg kitchen # REMOVE TEST BLOCK
    show masami # REMOVE TEST BLOCK

    m "I am a poem"

    show masami at bounce

    m party "At a party!"

    show masami at shake

    m surprised "What?"

    show masami at right with move
    show sabie happy at left with moveinleft
    show xinyi happy at center with Dissolve(0.2)

    m happy "Oh."

    scene bg black with Dissolve(2.0)

    jump intro_poem

# The actual starting point
label intro_poem:

    # This is currently in NVL mode, though we can change if needed!
    narrator "\n For every defining moment, there is a Before and an After."
    narrator "The Before is an open sea. Every turn of the rudder in water, every breath of the wind in the sail, holds equal promise of propelling a craft onward and dragging it under."
    narrator "The After is a rearview mirror. The rubble is already on the ground and growing ever smaller in the lens. The only control is the speed of onward acceleration."
    narrator "But what can be said of the moment itself, this impossibly thin waist in the hourglass of time? What can be said of this paradoxical well of space, where even the falling seconds dare to defy gravity?"
    narrator "What dare we make of it?"
    nvl clear

    jump office
