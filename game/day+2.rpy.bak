## DAY 2 - AFTER

label day2_transition:

    pause(2.0)
    show text "{size=+50}Day 2 - After{/size}" at trans_text with Dissolve(2.0)
    pause(4.0)
    hide text with Dissolve(2.0)
    pause(2.0)

    jump masami_room2a

label masami_room2a:

    play music reflective fadein 2.0
    scene bg black with Dissolve(2.0)

    mm "Masami!"
    mm "{i}Cepetan{/i}! Breakfast is getting cold."
    n "Masami groans. He curls up into a fetal position and shoves the pillow over his head."
    m "…"
    m "No."
    n "He swallows thickly, his voice dropping to a hoarse whisper."
    m "Fuck breakfast."
    mm "Masami."
    mm "Watch your - "
    m "I said, fuck breakfast!"
    mm "…"
    m "I'm not hungry."
    mm "If you do not eat, you will not be able to study  - "
    m "My grades can go burn in fucking hell."
    mm "Masami - "
    m "For fuck's sake, it's winter break."
    m "Leave me the fuck alone."
    mm "…"
    n "There's silence on the other end of the door for a full minute. Then, there's a soft patter of footsteps as his mom heads off down the hall."
    n "Masami exhales quietly and flops onto his back, the pillow still plastered onto his face."
    m "(Fuck.)"
    m "(I…shouldn't have unloaded on her like that. Again.)"
    m "(But I'm just so tired. Of all of this.)"
    m "…"

    menu:

        "Go back to sleep":
            m "(Guess I'll just go back to sleep then.)"

            stop music fadeout 2.0
            scene bg black with Dissolve(1.0)

            jump masami_room2b

# A few hours later
label masami_room2b:

    $ masami_glasses = False
    play music emotional fadein 1.0
    scene bg bedroom
    show masami sad at mc_pos
    with Dissolve(1.0)

    n "Masami is rudely awakened by the sunlight glaring down at him."
    show masami at shake, mc_pos
    m exasperated "(Ugh. My eyes. Where's…pillow?)"
    show bg bedroom at shake
    n "He feels around the bed for a moment, before sitting up with a sigh."
    m "(Where? I still don't - )"
    show bg bedroom at shake
    n "His hand hits something fluffy right behind him."
    m sad "(Oh. Well. Guess today is just one of those days.)"
    n "Masami props the pillow behind his head, where it's supposed to go."
    $ masami_glasses = True
    n "Then, he puts on his glasses and picks up his phone."
    m "(It's almost twelve. Half the day is gone.)"
    m happy "(To think that I expected the world to end or something after what I did yesterday...)"
    m sad "..."
    m "(It feels…kinda weird.)"
    m neutral "(But also kinda nice, actually.)"
    n "He hums a little to himself as he unlocks his phone."
    m "(Hm. New messages.)"

    jump phone2a

# Pick who you want to respond to…or no one
label phone2a:


    if (rohan_unread or sabie_unread or tyree_unread):

        hide masami

        menu:

            "Check Rohan's Message" if rohan_unread:
                $ rohan_unread = False
                jump phone2a_rohan

            "Check Sabie's Message" if sabie_unread:
                $ sabie_unread = False
                jump phone2a_sabie

            "Check Tyree's Message" if tyree_unread:
                $ tyree_unread = False
                jump phone2a_tyree

    else:
        show masami neutral at mc_pos
        m "(Well, looks like I've finished responding to all the messages.)"
        n "Just then, Masami's phone starts buzzing again."
        m exasperated "(Dammit. It's the group chat.)"
        m sad "(Wonder what they're up to now.)"

        jump phone2a_gc

# Masami chose to check Rohan's message - on phone
label phone2a_rohan:

    call phone_open(True,"Rohan")

    call message(r, "Hey", True)
    call message(r, "About the mall pics from a couple days ago")
    call message(r, "I think I found one thats not bad if u want to look")
    call message(r, "Not ready to post in gc yet")

    call phone_close()

    menu:

        "Respond":
            $ rohan_respond = True
            jump phone2a_rohan_respond

        "Ignore":
            $ rohan_respond = False
            jump phone2a_rohan_ignore

# Reply to Rohan's message
label phone2a_rohan_respond:

    call phone_open(False, "Rohan", False)

    # On phone portion
    call message(m, "Yeah sure", True)
    call message(r, "Kk give me one sec", True)
    call message("Image", "cg/Rohan_Mall.png") # TODO: Rohan picture here
    call message(r, "Sabie helped me pick")
    call message(r, "Makeup isnt very good since I did it myself this time")
    call message(r, "It isnt too bad is it")
    call message(m, "You look great", True)
    call message(r, "...", True)
    call message(m, "You don't believe me?", True)
    call message(r, "Uh", True)
    call message(r, "You always say stuff like that so I cant tell if youre just trying to make me feel better")
    call message(m, "...", True)
    call message(r, "Sabie does that too", True)
    call message(m, "Well, we are being honest", True)
    call message(r, "Maybe", True)
    call message(r, "Sometimes I wonder if that would change if she knew")
    call message(m, "Knew what?", True)
    call message(r, "Like what I told you about before", True)
    call message(m, "Oh, that.", True)
    call message(m, "Nah, I don't think she'd treat you any differently if she knew you felt that way about her")
    call message(r, "I hope so", True)
    call message(m, "Why ask?", True)
    call message(r, "Dunno just thinking", True)
    call message(m, "Ah", True)
    call message(r, "Wanna coop", True)
    call message(r, "I can carry you")
    call message(m, "I'll think about it", True)
    call message(r, "Kk", True)
    call message(r, "Oh")
    call message(r, "I almost forgot")
    call message(r, "I have leftover gingerbread cookies if u want extra")
    call message(m, "I'm good, thanks.", True)
    call message(r, "U sure", True)
    call message(m, "Yeah. I'll let you know if I want any.", True)
    call message(r, "Kk", True)

    call phone_close()

    # Off phone portion
    show masami at mc_pos
    m neutral "(Ahh, I'd actually kill for one of those cookies right now. Or anything he'd make.)"
    m sad "(But I also don't feel like seeing anyone today.)"
    m "…"
    m "(Guess I'll have to ask him later when I'm feeling up to it.)"

    jump phone2a

# Ignore Rohan's message - off phone
label phone2a_rohan_ignore:

    show masami at mc_pos
    m sad "(I wouldn't mind seeing it, but…)"
    m neutral "(It wouldn't hurt if I delayed replying by a day or two.)"

    jump phone2a

# Masami chose to check Sabie's message - on phone
label phone2a_sabie:

    call phone_open(True)

    call message(s, "{b}This message was deleted.{/b}", True)
    call message(s, "sry {i}ge{/i} my bad")
    call message(s, "ignore me")

    call phone_close()

    menu:

        "Respond":
            $ sabie_respond = True
            jump phone2a_sabie_respond

        "Ignore":
            $ sabie_respond = True
            jump phone2a_sabie_ignore

# Reply to Sabie's Message
label phone2a_sabie_respond:

    # On phone portion

    call phone_open(False, "Sabie", False)

    call message(m, "Okay.", True)
    call message(s, "bruh", True)
    call message(s, "you didnt listen >:(")
    call message(m, "What else did you expect me to do?", True)
    call message(s, "idk", True)
    call message(s, "just not respond ig")
    call message(m, "Okay.", True)
    call message(m, "But what was it?")
    call message(s, "...", True)
    call message(m, "Are you actually embarrassed?", True)
    call message(s, "no ofc not", True)
    call message(m, "Why no show?", True)
    call message(s, "do u wanna see drunk pics again", True)
    call message(m, "No?", True)
    call message(s, "there u go", True)
    call message(m, "...", True)
    call message(s, "what", True)
    call message(m, "Nothing.", True)
    call message(m, "Nothing at all. (:")
    call message(s, "...", True)
    call message(s, "are u trying to blackmail me again")
    call message(m, "Blackmail? When have I blackmailed you?", True)
    call message(s, "uh all the time", True)
    call message(m, "Like what", True)
    call message(s, "is threatening to tell my parents about me going out to have fun not blackmail", True)
    call message(m, "No, that's me looking out for you", True)
    call message(m, "I don't like seeing you getting wasted every weekend")
    call message(s, "but you keep your mouth shut about rohan doing theatre in front of his parents", True)
    call message(s, "thats very fair")
    call message(s, "no problems at all")
    call message(m, "That's different. His parents are worse than yours and you know it.", True)
    call message(s, ":P", True)
    call message(s, "whatevs")
    call message(s, "anyways")
    call message(s, "how are quizbowl qs going")
    call message(s, "i need my steady supply of nerd qs to torture the kiddos with")
    call message(m, "Nerd qs", True)
    call message(s, "yes nerd qs", True)
    call message(s, "you need something to keep you busy")
    call message(s, "and i don’t want to touch any of your gross sciencey math shit")
    call message(m, "You know, if you keep insulting me, I won't help you.", True)
    call message(s, "see theres the blackmail right there", True)
    call message(m, "(:", True)
    call message(s, "ugh ur hopeless", True)
    call message(s, "bye")
    call message(m, "Okay, bye.", True)

    call phone_close()

    # Off phone portion
    show masami at mc_pos
    m neutral "(Well, at least things seem normal with her.)"
    m sad "…"
    m "(It's nice that she's not bringing up {i}jie{/i}, but I kind of wish she did.)"

    jump phone2a

# Ignore Sabie's Message - off phone
label phone2a_sabie_ignore:

    show masami at mc_pos
    m neutral "(Well, she said to ignore it, so that's what I'm gonna do.)"

    jump phone2a

# Masami chose to check Tyree's message - on phone
label phone2a_tyree:

    call phone_open(True, "Tyree")

    call message(t, "Let me know if you want me to take over anything for you.", True)
    call message(t, "You do not need to reply, but I am here if you need me.")

    call phone_close()

    menu:

        "Respond":
            $ tyree_respond = True
            jump phone2a_tyree_respond

        "Ignore":
            $ tyree_respond = False
            jump phone2a_tyree_ignore

# Masami responds to Tyree
label phone2a_tyree_respond:

    call phone_open(False, "Tyree", False)

    # On-phone portion
    call message(m, "Hey thanks for reaching out", True)
    call message(m, "I think I'm good for now, but I'll let you know")
    call message(t, "Alright.", True)
    call message(m, "Oh yeah, I forgot to ask", True)
    call message(m, "Are there any more sponsors I need to reach out or grants I should apply to before the season starts?")
    call message(m, "Our budget is looking a bit tight right now")
    call message(t, "There are a few, but I can manage them.", True)
    call message(m, "You sure?", True)
    call message(m, "You're not too busy with swim captaining and recruiting?")
    call message(m, "Or helping Sabie with Quizbowl?")
    call message(t, "Don't worry, I can do it.", True)
    call message(m, "You sure?", True)
    call message(t, "I'm sure.", True)
    call message(t, ":)")
    call message(m, "Alright, I'll take your word for it.", True)
    call message(m, "Let me know if you need me to look over anything!")
    call message(t, "Okay!", True)

    call phone_close()

    # Off-phone portion
    show masami at mc_pos
    m neutral "(That was nice.)"
    m sad "…"
    m "(I know he can handle it, but I still feel bad about giving him so much to do.)"

    jump phone2a

# Masami chooses to ignore the message
label phone2a_tyree_ignore:

    show masami at mc_pos
    m neutral "(I appreciate that.)"
    m "(I'll just leave the message as is. Tyree understands.)"
    m sad "(Besides, he'll probably have his hands full enough once the school realizes what I've done.)"
    m "…"
    m exasperated "(Whatever. It's too late to change anything.)"

    jump phone2a

# Masami responds to the group chat - on phone
label phone2a_gc:

    hide masami

    call phone_open(True,"Group")

    call message(s, "yo", True)
    call message(s, "did yall see that")
    call message(r, "See what", True)
    call message(s, "the vandalism thing", True)
    call message(s, "someone absolutely lost their shit")
    call message(r, "Uh...", True)
    call message(r, "But hasnt everyone lost their shit")
    call message(s, "well yeah", True)
    call message(r, "Except for like tyree", True)
    call message(s, "also yeah", True)
    call message(s, "bc hes just special like that")
    call message(r, "Truee", True)
    call message(t, "Okay.", True)
    call message(s, "anyways somebody really snapped this time", True)
    call message(s, "went savagely poetic spitting them facts")
    call message(s, "it was beautiful <3")
    call message(r, "Uh...", True)
    call message(s, "what", True)
    call message(s, "ik art when i see it")
    call message(r, "Im not questioning that", True)
    call message(r, "You just sound suspiciously like the one who did it")
    call message(s, "lmaoo i wish", True)
    call message(s, "i don’t have the balls to do that")
    call message(s, "i just drink and drive :3")
    call message(r, "...", True)
    call message(s, "ur judging me arent u -_-", True)
    call message(r, "No, ofc not!", True)
    call message(t, "Lol.", True)
    call message(s, "i agree rohan is very sus", True)
    call message(r, "Hey!", True)
    call message(t, ":)", True)
    call message(s, "anyways, im not crazy enough to risk my perfect school record with a suspension ^.^", True)
    call message(r, "Yeah I feel kinda bad for whoever did it", True)
    call message(r, "Its like academic suicide")
    call message(s, "psh now you sound like masami", True)
    call message(r, "Lol for real though, I scared myself channeling that energy", True)
    call message(t, "I just hope whoever it is finds the help they need.", True)
    call message(s, "ykw ur right", True)
    call message(s, "we should all be nice people like tyree")
    call message(s, "right {i}ge{/i}")
    call message(s, "...")
    call message(s, "......")
    call message(t, ".........", True)
    call message(r, "Uh...", True)
    call message(s, "guess hell see this later", True)
    call message(r, "*he'll", True)
    call message(s, "**hell", True)
    call message(t, "He's probably taking some time off.", True)
    call message(r, "or just watching us", True)
    call message(s, "truu he really likes lurking", True)
    call message(r, "Lol", True)
    call message(s, "heyo {i}gegeee{/i}", True)
    call message(s, "if youre reading this i just wanna say that you gotta let go like vandal dude")
    call message(s, "but not too much like vandal dude")
    call message(s, "u will feel better i promiseee")

    call phone_close()

    jump masami_room2c

    # You're done responding
label masami_room2c:

    show masami at mc_pos

    n "Masami casually lets his phone drop onto his stomach. It keeps buzzing, but he doesn't bother to pick it up."
    m "(If only you knew, Sabie.)"
    m "(If only you knew how temporary that relief was.)"
    m sad "…"
    n "His stomach rumbles."
    m neutral "(Right. Mom's probably making lunch right now.)"
    m sad "(...I probably owe her an apology since I haven't given her one last night either.)"
    m "(Not sure if I even want to say anything.)"
    m "(No matter what I say, she still wouldn't really understand. She never has.)"
    m "…"
    n "Masami sighs."
    m "(Well. Might as well head on over since I need food anyways.)"

    jump masami_kitchen2

# Masami heads to the kitchen
label masami_kitchen2:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg kitchen
    show masami sad at mc_pos
    with Dissolve(1.0)

    n "Masami can smell the fragrant aroma of sesame oil long before he reaches the kitchen."
    show wsprite with Dissolve(0.2)
    n "He walks in to find his mother with her apron on and back turned, having just finished cooking."
    n "She turns off the heat on the bok choi she was stir-frying in a wok. A clay pot sits on low heat on the back burner."
    m "(Looks like it's a Hainanese chicken rice day.)"
    m neutral "(Kind of need that.)"
    m sad "…"
    m "(Should I say something to her?)"

    # Pick whether or not you plan on talking to Masami's mom
    menu:

        "Try to talk her":
            jump masami_kitchen2_talk

        "Ignore her":
            jump masami_kitchen2_ignore

# Masami choses to talk to his mom
label masami_kitchen2_talk:

    n "Masami gingerly taps his mother's shoulder."
    m neutral "Uh…Mom?"
    show wsprite at shake, center
    n "Masami's mother stops stirring the pot and turns around."
    mm "Yes?"
    m "I…"
    m sad "…"
    n "Masami's eyes drop to the floor, his hand retracting back to his side."
    show masami exasperated at shake, mc_pos
    m "(Damn it. I still don't know what to say.)"
    show masami sad
    n "Masami feels his mother wrapping her arms around him. She kisses him softly on the forehead."
    show wsprite at bounce, center
    mm "{i}Makan.{/i} Have some food. You feel better, okay?"
    show masami neutral
    n "Masami nods."
    m "Okay. Thanks."
    n "He grabs a plate and spoon from the cupboard, helping himself to some food."

    jump masami_room2d

# Masami choses to ignore his mom
label masami_kitchen2_ignore:

    n "Masami grabs a plate and spoon from the cupboard. His mom watches in silence as he helps himself to the food."
    m "…"
    m exasperated "(This is awkward. I thought she'd say something by now.)"
    m sad "(Guess she's just deciding to give me some space.)"

    jump masami_room2d

# Masami returns to his room
label masami_room2d:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg bedroom
    show masami sad at mc_pos
    with Dissolve(1.0)

    n "Masami heads back to his room, where he eats in silence."
    m neutral "(This is really good. I actually feel better now.)"
    m sad "(Sort of.)"
    n "Despite himself, instinctively turns to look out the window."
    m "…"
    m exasperated "(I wonder why I still bother when she's gone.)"
    show masami sad
    n "He looks around his room."
    m "(It'll be several hours before Dad comes home. Might as well find something to do.)"

    jump masami_room2_explore

# Open up a screen to explore things, disappear on click after each option is looked at
label masami_room2_explore:

    hide masami
    call screen bedroom

# If the bookcase option is selected
label masami_room2_read:

    $ room_read = False
    m "(Heh. Younger me definitely had the patience for that.)"
    m "(But now? For some reason, I can't get myself to read for fun anymore.)"
    jump masami_room2_explore

# If the backpack option is selected
label masami_room2_study:

    $ room_study = False
    m "(Right. I still need to do that.)"
    m "…"
    m "(I don't really think I can focus on that now.)"
    jump masami_room2_explore

# If the computer option is selected
label masami_room2_games:

    m "(Hm, looks like Sabie is online playing Genshin.)"
    m "(And Rohan, too, with League of Legends as always.)"
    m "..."
    m "(Not really in the mood for multiplayer right now, so I might as well continue where I left off with Herlock Sholmes.)"
    jump masami_news

# Masami indulges himself for a couple hours, before it's time for dinner
label masami_news:

    scene bg black
    with Dissolve(1.0)
    stop music fadeout 2.0

    n "Masami sets his phone to silent and puts on his headset."

    scene bg bedroomnight
    show masami sad at mc_pos
    with Dissolve(1.0)

    n "A few hours later, he is faintly aware of the ringing of the telephone and the soft clack of his mom's slippers as she goes to pick it up."

    play music reflective fadein 2.0

    mm "Hello?"
    mm "Yes."
    mm "Yes..."
    mm "Oh."
    n "His mom goes silent, not saying a word as she hangs up the phone."
    n "Masami hears his father, who must have come home some time ago, say something indiscernible to her and the two of them speak in hushed whispers."
    n "A moment later, he hears his mother's muffled sobbing."
    m "(...The school called them about the vandalism, didn't they?)"
    n "A lump forms in Masami's throat. He swallows hard and stares at his hands."
    n "They're shaking."
    m "(Is this what {i}jie{/i} felt like whenever she disappointed someone?)"
    m exasperated "(How did she learn to stop caring?)"
    n "He squeezes his fists tight, only vaguely noticing the way his nails dig into his palms."
    show masami at shake, mc_pos
    m "(I…)"
    show masami sad
    n "His eyes snap back open, roaming around in every direction beside the window and the door."
    n "They settle on the phone face down on his desk."
    m "(Rohan, Sabie, Tyree...none of them know, do they?)"
    m exasperated "(...With how they thought about the vandalism, do I even want them to know?)"
    show masami sad
    n "His fingers gingerly trace the shell of the case before flipping it over, screen side belly-up."
    show masami surprised
    n "When the home screen flicks on, his breath catches."
    m "(New messages from an unknown number.)"
    m "(No way. I thought…)"
    show masami at shake, mc_pos
    m exasperated "(No, it can't be.)"
    m sad "(Can it?)"
    n "Holding his breath, he opens the message up."

    jump phone2b

# Text from the unknown number - should not show it's from Nasir
label phone2b:

    hide masami

    call phone_open(True, "???")

    call message("???", "You're really a brave one, aren't you, magpie?", True)
    call message("???", "Your sister must be proud of you. :)")

    call phone_close()

    jump masami_dayend

# Masami reflects on it, scene cut
label masami_dayend:

    show masami at mc_pos

    n "Masami feels his chest warm."
    m "(Ah, so it was you.)"
    n "He delicately traces the outline of the text bubbles with his thumb."
    m happy "(You think she's proud of me, huh?)"
    m sad "..."
    m "(Is that what I even want anymore?)"

    scene bg black
    hide masami
    with Dissolve(3.0)
    stop music fadeout 2.0

    jump day_2_transition
