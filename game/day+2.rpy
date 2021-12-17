## DAY 2 - AFTER
label masami_room2a:

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
            jump masami_room2b

# A few hours later
label masami_room2b:

    n "Masami is rudely awakened by the sunlight glaring down at him."
    m "(Ugh. My eyes. Where's…pillow?)"
    n "He feels around the bed for a moment, before sitting up with a sigh."
    m "(Where? I still don't - )"
    n "His hand hits something fluffy right behind him."
    m "(Oh. Well. Guess today is just one of those days.)"
    n "Masami props the pillow behind his head, where it's supposed to go."
    n "Then, he reaches for his phone."
    m "(It's almost twelve. Half the day is gone.)"
    m "…"
    n "Masami chuckles to himself."
    m "(To think that I expected the world to end or something after what I did yesterday...)"
    m "…"
    m "(It feels…kinda weird.)"
    m "(But also kinda nice, actually.)"
    n "He hums a little to himself as he unlocks his phone."
    m "(Hm. New messages.)"

    jump phone2a

# Pick who you want to respond to…or no one
label phone2a:

    if (rohan_unread or sabie_unread or tyree_unread):

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
        m "(Well, looks like I've finished responding to all the messages.)"
        n "Just then, Masami's phone starts buzzing again."
        m "(Dammit. It's the group chat.)"
        m "(Wonder what they're up to now.)"

        jump phone2a_gc

# Masami chose to check Rohan's message - on phone
label phone2a_rohan:

    call phone_open(True)

    call message(r, "Hey")
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

    call phone_open(False, False)

    # On phone portion
    call message(m, "Yeah sure")
    call message(r, "Kk give me one sec")
    # Rohan picture here
    call message(r, "Sabie helped me pick")
    call message(r, "Makeup isnt very good since I did it myself this time")
    call message(r, "It isnt too bad is it")
    call message(m, "You look great")
    call message(r, "...")
    call message(m, "You don't believe me?")
    call message(r, "Uh")
    call message(r, "You always say stuff like that so I cant tell if youre just trying to make me feel better")
    call message(m, "...")
    call message(r, "Sabie does that too")
    call message(m, "Well, we are being honest")
    call message(r, "Maybe")
    call message(r, "Sometimes I wonder if that would change if she knew")
    call message(m, "Knew what?")
    call message(r, "Like what I told you about before")
    call message(m, "Oh, that.")
    call message(m, "Nah, I don't think she'd treat you any differently if she knew you felt that way about her")
    call message(r, "I hope so")
    call message(m, "Why ask?")
    call message(r, "Dunno just thinking")
    call message(m, "Ah")
    call message(r, "Wanna coop")
    call message(r, "I can carry you")
    call message(m, "I'll think about it")
    call message(r, "Kk")
    call message(r, "Oh")
    call message(r, "I almost forgot")
    call message(r, "I have leftover gingerbread cookies if u want extra")
    call message(m, "I'm good, thanks.")
    call message(r, "U sure")
    call message(m, "Yeah. I'll let you know if I want any.")
    call message(r, "Kk")

    call phone_close()

    # Off phone portion
    m "(Ahh, I'd actually kill for one of those cookies right now. Or anything he'd make.)"
    m "(But I also don't feel like seeing anyone today.)"
    m "…"
    m "(Guess I'll have to ask him later when I'm feeling up to it.)"

    jump phone2a

# Ignore Rohan's message - off phone
label phone2a_rohan_ignore:

    m "(I wouldn't mind seeing it, but…)"
    m "(It wouldn't hurt if I delayed replying by a day or two.)"

    jump phone2a

# Masami chose to check Sabie's message - on phone
label phone2a_sabie:

    call phone_open(True)

    call message(s, "{i}This message was deleted.{/i}")
    call message(s, "sry ge my bad")
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

    call phone_open(False, False)

    call message(m, "Okay.")
    call message(s, "bruh")
    call message(s, "you didnt listen >:(")
    call message(m, "What else did you expect me to do?")
    call message(s, "idk")
    call message(s, "just not respond ig")
    call message(m, "Okay.")
    call message(m, "But what was it?")
    call message(s, "...")
    call message(m, "Are you actually embarrassed?")
    call message(s, "no ofc not")
    call message(m, "Why no show?")
    call message(s, "do u wanna see drunk pics again")
    call message(m, "No?")
    call message(s, "there u go")
    call message(m, "...")
    call message(s, "what")
    call message(m, "Nothing.")
    call message(m, "Nothing at all. (:")
    call message(s, "...")
    call message(s, "are u trying to blackmail me again")
    call message(m, "Blackmail? When have I blackmailed you?")
    call message(s, "uh all the time")
    call message(m, "Like what")
    call message(s, "is threatening to tell my parents about me going out to have fun not blackmail")
    call message(m, "No, that's me looking out for you")
    call message(m, "I don't like seeing you getting wasted every weekend")
    call message(s, "but you keep your mouth shut about rohan doing theatre in front of his parents")
    call message(s, "thats very fair")
    call message(s, "no problems at all")
    call message(m, "That's different. His parents are worse than yours and you know it.")
    call message(s, ":P")
    call message(s, "whatevs")
    call message(s, "anyways")
    call message(s, "how are quizbowl qs going")
    call message(s, "i need my steady supply of nerd qs to torture the kiddos with")
    call message(m, "Nerd qs")
    call message(s, "yes nerd qs")
    call message(s, "you need something to keep you busy")
    call message(s, "and i don’t want to touch any of your gross sciencey math shit")
    call message(m, "You know, if you keep insulting me, I won't help you.")
    call message(s, "see theres the blackmail right there")
    call message(m, "(:")
    call message(s, "ugh ur hopeless")
    call message(s, "bye")
    call message(m, "Okay, bye.")

    call phone_close()

    # Off phone portion
    m "(Well, at least things seem normal with her.)"
    m "…"
    m "(It's nice that she's not bringing up {i}jie{/i}, but I kind of wish she did.)"

    jump phone2a

# Ignore Sabie's Message - off phone
label phone2a_sabie_ignore:

    m "(Well, she said to ignore it, so that's what I'm gonna do.)"

    jump phone2a

# Masami chose to check Tyree's message - on phone
label phone2a_tyree:

    call phone_open(True)

    call message(t, "Let me know if you want me to take over anything for you.")
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

    call phone_open(False, False)

    # On-phone portion
    call message(m, "Hey thanks for reaching out")
    call message(m, "I think I'm good for now, but I'll let you know")
    call message(t, "Alright.")
    call message(m, "Oh yeah, I forgot to ask")
    call message(m, "Are there any more sponsors I need to reach out or grants I should apply to before the season starts?")
    call message(m, "Our budget is looking a bit tight right now")
    call message(t, "There are a few, but I can manage them.")
    call message(m, "You sure?")
    call message(m, "You're not too busy with swim captaining and recruiting?")
    call message(m, "Or helping Sabie with Quizbowl?")
    call message(t, "Don't worry, I can do it.")
    call message(m, "You sure?")
    call message(t, "I'm sure.")
    call message(t, ":)")
    call message(m, "Alright, I'll take your word for it.")
    call message(m, "Let me know if you need me to look over anything!")
    call message(t, "Okay!")

    call phone_close()

    # Off-phone portion
    m "(That was nice.)"
    m "…"
    m "(I know he can handle it, but I still feel bad about giving him so much to do.)"

    jump phone2a

# Masami chooses to ignore the message
label phone2a_tyree_ignore:

    m "(I appreciate that.)"
    m "(I'll just leave the message as is. Tyree understands.)"
    m "(Besides, he'll probably have his hands full enough once the school realizes what I've done.)"
    m "…"
    m "(Whatever. It's too late to change anything.)"

    jump phone2a

# Masami responds to the group chat - on phone
label phone2a_gc:

    call phone_open(True)

    call message(s, "yo")
    call message(s, "did yall see that")
    call message(r, "See what")
    call message(s, "the vandalism thing")
    call message(s, "someone absolutely lost their shit")
    call message(r, "Uh...")
    call message(r, "But hasnt everyone lost their shit")
    call message(s, "well yeah")
    call message(r, "Except for like tyree")
    call message(s, "also yeah")
    call message(s, "bc hes just special like that")
    call message(r, "Truee")
    call message(t, "Okay.")
    call message(s, "anyways somebody really snapped this time")
    call message(s, "went savagely poetic spitting them facts")
    call message(s, "it was beautiful <3")
    call message(r, "Uh…")
    call message(s, "what")
    call message(s, "ik art when I see it")
    call message(r, "Im not questioning that")
    call message(r, "You just sound suspiciously like the one who did it")
    call message(s, "lmaoo i wish")
    call message(s, "i don’t have the balls to do that")
    call message(s, "i just drink and drive")
    call message(r, "...")
    call message(s, "ur judging me arent u -_-")
    call message(r, "No, ofc not!")
    call message(t, "Lol.")
    call message(s, "i agree rohan is very sus")
    call message(r, "Hey!")
    call message(t, ":)")
    call message(s, "anyways, im not crazy enough to risk my perfect school record with a suspension")
    call message(r, "Yeah I feel kinda bad for whoever did it")
    call message(r, "Its like academic suicide")
    call message(s, "psh now you sound like masami")
    call message(r, "Lol for real though, I scared myself channeling that energy")
    call message(t, "I just hope whoever it is finds the help they need.")
    call message(s, "ykw ur right")
    call message(s, "we should all be nice people like tyree")
    call message(s, "right ge")
    call message(s, "...")
    call message(s, "......")
    call message(t, ".........")
    call message(r, "Uh...")
    call message(s, "guess hell see this later")
    call message(r, "*he'll")
    call message(s, "**hell")
    call message(t, "He's probably taking some time off.")
    call message(r, "or just watching us")
    call message(s, "truu he really likes lurking")
    call message(r, "Lol")
    call message(s, "heyo gegeee")
    call message(s, "if youre reading this i just wanna say that you gotta let go like vandal dude")
    call message(s, "but not too much like vandal dude")
    call message(s, "u will feel better i promiseee")

    call phone_close()

    jump masami_room2c

    # You're done responding
label masami_room2c:

    n "Masami casually lets his phone drop onto his stomach. It keeps buzzing, but he doesn't bother to pick it up."
    m "(If only you knew, Sabie.)"
    m "(If only you knew how temporary that relief was.)"
    m "…"
    n "His stomach rumbles."
    m "(Right. Mom's probably making lunch right now.)"
    m "…"
    m "(I probably owe her an apology since I haven't given her one last night either.)"
    m "(Not sure if I even want to say anything.)"
    m "(No matter what I say, she still wouldn't really understand. She never has.)"
    m "…"
    n "Masami sighs."
    m "(Well. Might as well head over to the kitchen since I need food anyways.)"

    jump masami_kitchen2

# Masami heads to the kitchen
label masami_kitchen2:

    scene bg kitchen

    n "Masami can smell the fragrant aroma of sesame oil long before he reaches the kitchen."
    n "He walks in to find his mother with her apron on and back turned, having just finished cooking."
    n "She turns off the heat on the bok choi she was stir-frying in a wok. A clay pot sits on low heat on the back burner."
    m "(Looks like it's a Hainanese chicken rice day.)"
    m "(Kind of need that.)"
    m "…"
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
    m "Uh…Mom?"
    n "Masami's mother stops stirring the pot and turns around."
    mm "Yes?"
    m "I…"
    m "…"
    n "Masami's eyes drop to the floor, his hand retracting back to his side."
    m "(Damn it. I still don't know what to say.)"
    n "Masami feels his mother wrapping her arms around him. She kisses him softly on the forehead."
    mm "{i}Makan.{/i} Have some food. You feel better, okay?"
    n "Masami nods."
    m "Okay. Thanks."
    n "Masami grabs a plate and spoon from the cupboard, helping himself to some food."

    jump masami_room2d

# Masami choses to ignore his mom
label masami_kitchen2_ignore:

    n "Masami grabs a plate and spoon from the cupboard. His mom watches in silence as he helps himself to the food."
    m "…"
    m "(This is awkward. I thought she'd say something by now.)"
    m "(Guess she's just deciding to give me some space.)"

    jump masami_room2d

# Masami returns to his room
label masami_room2d:

    scene # TODO: Fix this!

    n "Masami heads back to his room, where he eats in silence."
    m "(This is really good. I actually feel better now.)"
    m "(Sort of.)"
    n "Despite himself, instinctively turns to look out the window."
    m "…"
    m "(I wonder why I still bother when she's gone.)"
    n "He looks around his room."
    m "(It'll be several hours before Dad comes home. Might as well find something to do.)"

    jump masami_room2_explore

# Open up a screen to explore things, disappear on click after each option is looked at
label masami_room2_explore:

    # TODO: Make this point and click!
    menu:

        "Study for upcoming final exams":
            m "(Right. I still need to do that.)"
            m "…"
            m "(I don't really think I can focus on that now.)"
            jump masami_room2_explore

        "Play some video games":
            m "(Hm, looks like Rohan is online.)"
            m "…"
            m "(Not really in the mood for multiplayer right now.)"
            m "(Might as well continue where I left off with Herlock Sholmes.)"
            jump masami_news

        "Read a book":
            m "(Heh. Younger me definitely had the patience for that.)"
            m "(But now? For some reason, I can't get myself to read for fun anymore.)"
            jump masami_room2_explore

# Masami indulges himself for a couple hours, before it's time for dinner
label masami_news:

    n "Masami sets his phone to silent and puts on his headset."
    n "A few hours later, he is faintly aware of the ringing of the telephone and the soft clack of his mom's slippers as she goes to pick it up."
    mm "Hello?"
    mm "Yes."
    mm "Yes..."
    mm "Oh."
    n "His mom goes silent, not saying a word as she hangs up the phone."
    n "Masami hears his father, who must have come home some time ago, say something indiscernible to her and the two of them speak in hushed whispers."
    n "A moment later, he hears his mother's muffled sobbing."
    m "…"
    m "(The school called them about the vandalism, didn't they?)"
    n "A lump forms in Masami's throat. He swallows hard and stares at his hands."
    n "They're shaking."
    m "(Is this what {i}jie{/i} felt like whenever she didn’t quite manage to do what people wanted out of her?)"
    m "(How did she learn to stop caring?)"
    n "He squeezes his eyes tight, only vaguely noticing the way his fists clench and his nails dig into his palms."
    m "(I…)"
    n "His eyes snap back open, roaming around in every direction beside the window and the door."
    n "They settle on the phone face down on his desk."
    m "(Rohan, Sabie, Tyree…none of them know, do they?)"
    m "…"
    m "(With how they thought about the vandalism, do I even want them to know?)"
    n "His fingers gingerly trace the shell of the case before flipping it over, screen side belly-up."
    n "When it lights up, his breath catches."
    m "(New messages from an unknown number.)"
    m "(No way. I thought…)"
    m "(No, it can't be. Can it?)"
    n "Holding his breath, he opens the message up."

    jump phone_2b

# Text from the unknown number - should not show it's from Nasir
label phone_2b:

    call phone_open(True)

    call message("???", "You're really a brave one, aren't you, magpie?")
    call message("???", "Your sister must be proud of you. :)")

    call phone_close()

    jump masami_dayend

# Masami reflects on it, scene cut
label masami_dayend:

    n "Masami feels his chest warm."
    m "(Ah, so it was you.)"
    n "He delicately traces the outline of the text bubbles with his thumb."
    m "(You think she's proud of me, huh?)"
    m "..."
    m "(Is that what I even want anymore?)"

    jump masami_room_2
