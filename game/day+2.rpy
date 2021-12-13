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

    r "Hey"
    r "About the mall pics from a couple days ago"
    r "I think I found one thats not bad if u want to look"
    r "Not ready to post in gc yet"

    menu:

        "Respond":
            $ rohan_respond = True
            jump phone2a_rohan_respond

        "Ignore":
            jump phone2a_rohan_ignore

# Reply to Rohan's message
label phone2a_rohan_respond:

    # On phone portion
    m "Yeah sure"
    r "Kk give me one sec"
    # Rohan picture here
    r "Sabie helped me pick"
    r "Makeup isnt very good since I did it myself this time"
    r "It isnt too bad is it"
    m "You look great"
    r "…"
    m "You don't believe me?"
    r "Uh"
    r "You always say stuff like that so I cant tell if youre just trying to make me feel better"
    m "…"
    r "Sabie does that too"
    m "Well, we are being honest"
    r "Maybe"
    r "Sometimes I wonder if that would change if she knew"
    m "Knew what?"
    r "Like what I told you about before"
    m "Oh, that."
    m "Nah, I don't think she'd treat you any differently if she knew you felt that way about her"
    r "I hope so"
    m "Why ask?"
    r "Dunno just thinking"
    m "Ah"
    r "Wanna coop"
    r "I can carry you"
    m "I'll think about it"
    r "Kk"
    r "Oh"
    r "I almost forgot"
    r "I have leftover gingerbread cookies if u want extra"
    m "I'm good, thanks."
    r "U sure"
    m "Yeah. I'll let you know if I want any."
    r "Kk"

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

    s "{i}This message was deleted.{/i}"
    s "sry ge my bad"
    s "ignore me"

    menu:

        "Respond":
            $ sabie_respond = True
            jump phone2a_sabie_respond

        "Ignore":
            jump phone2a_sabie_ignore

# Reply to Sabie's Message
label phone2a_sabie_respond:

    # On phone portion
    m "Okay."
    s "bruh"
    s "you didnt listen >:("
    m "What else did you expect me to do?"
    s "idk"
    s "just not respond ig"
    m "Okay."
    m "But what was it?"
    s "…"
    m "Are you actually embarrassed?"
    s "no ofc not"
    m "Why no show?"
    s "do u wanna see drunk pics again"
    m "No?"
    s "there u go"
    m "…"
    s "what"
    m "Nothing."
    m "Nothing at all. (:"
    s "…"
    s "are u trying to blackmail me again"
    m "Blackmail? When have I blackmailed you?"
    s "uh all the time"
    m "Like what"
    s "is threatening to tell my parents about me going out to have fun not blackmail"
    m "No, that's me looking out for you"
    m "I don't like seeing you getting wasted every weekend"
    s "but you keep your mouth shut about rohan doing theatre in front of his parents"
    s "thats very fair"
    s "no problems at all"
    m "That's different. His parents are worse than yours and you know it."
    s ":P"
    s "whatevs"
    s "anyways"
    s "how are quizbowl qs going"
    s "i need my steady supply of nerd qs to torture the kiddos with"
    m "Nerd qs"
    s "yes nerd qs"
    s "you need something to keep you busy"
    s "and i don’t want to touch any of your gross sciencey math shit"
    m "You know, if you keep insulting me, I won't help you."
    s "see theres the blackmail right there"
    m "(:"
    s "ugh ur hopeless"
    s "bye"
    m "Okay, bye."

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

    t "Let me know if you want me to take over anything for you."
    t "You do not need to reply, but I am here if you need me."

    menu:

        "Respond":
            $ tyree_respond = True
            jump phone2a_tyree_respond

        "Ignore":
            jump phone2a_tyree_ignore

# Masami responds to Tyree
label phone2a_tyree_respond:

    # On-phone portion
    m "Hey thanks for reaching out"
    m "I think I'm good for now, but I'll let you know"
    t "Alright."
    m "Oh yeah, I forgot to ask"
    m "Are there any more sponsors I need to reach out or grants I should apply to before the season starts?"
    m "Our budget is looking a bit tight right now"
    t "There are a few, but I can manage them."
    m "You sure?"
    m "You're not too busy with swim captaining and recruiting?"
    m "Or helping Sabie with Quizbowl?"
    t "Don't worry, I can do it."
    m "You sure?"
    t "I'm sure."
    t ":)"
    m "Alright, I'll take your word for it."
    m "Let me know if you need me to look over anything!"
    t "Okay!"

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

    s "yo"
    s "did yall see that"
    r "See what"
    s "the vandalism thing"
    s "someone absolutely lost their shit"
    r "uh no"
    r "But hasnt everyone lost their shit"
    s "well yeah"
    r "Except for like tyree"
    s "also yeah"
    s "bc hes just special like that"
    r "Truee"
    t "Okay."
    s "anyways somebody really snapped this time"
    s "went savagely poetic spitting them facts"
    s "it was beautiful <3"
    r "Uh…"
    s "what"
    s "ik art when I see it"
    r "Im not questioning that"
    r "You just sound suspiciously like the one who did it"
    s "lmaoo i wish"
    s "i don’t have the balls to do that"
    s "i just drink and drive"
    r "…"
    s "ur judging me arent u -_-"
    r "No, ofc not!"
    t "Lol."
    s "i agree rohan is very sus"
    r "Hey!"
    t ":)"
    s "anyways, im not crazy enough to risk my perfect school record with a suspension"
    r "Yeah I feel kinda bad for whoever did it"
    r "Its like academic suicide"
    s "psh now you sound like masami"
    r "Lol for real though, I scared myself channeling that energy"
    t "I just hope whoever it is finds the help they need."
    s "ykw ur right"
    s "we should all be nice people like tyree"
    s "right ge"
    s "…"
    s "……"
    t "………"
    r "Uh…"
    s "guess hell see this later"
    r "*he'll"
    s "**hell"
    t "He's probably taking some time off."
    r "or just watching us"
    s "truu he really likes lurking"
    r "Lol"
    s "heyo gegeee"
    s "if youre reading this i just wanna say that you gotta let go like vandal dude"
    s "but not too much like vandal dude"
    s "u will feel better i promiseee"

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

    na "You're really a brave one, aren't you, magpie?"
    na "Your sister must be proud of you. :)"

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
