## DAY 2 - AFTER

label day2_transition:

    call screen day_change(550, 5, "Day 2 - After") with Dissolve(2.0)
    pause(3.0)

    jump masami_room2a

label masami_room2a:

    play music reflective fadein 2.0
    scene bg black with Dissolve(2.0)

    play sound "audio/sound/knock_pound.mp3"
    mm "Masami!"
    mm "{i}Cepetan{/i}! Breakfast is getting cold."
    n "Masami groans. He curls up into a fetal position and shoves the pillow over his head."
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "…"
    m "No."
    n "He swallows thickly, his voice dropping to a hoarse whisper."
    m "Fuck breakfast."
    mm "Masami."
    mm "Watch your - "
    m "I said, fuck breakfast!"
    mm "…"
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "I'm not hungry."
    mm "If you do not eat, you will not be able to study  - "
    m "My grades can go burn in fucking hell."
    mm "Masami - "
    m "For fuck's sake, it's winter break."
    m "Leave me the fuck alone."
    mm "…"
    n "There's silence on the other end of the door for a full minute. Then, there's a soft patter of footsteps as his mom heads off down the hall."
    voice "audio/voice/masami/masami_quietsigh.mp3"
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
    play sound "audio/sound/bed_bounce.mp3" volume 0.3
    n "He feels around the bed for a moment, before sitting up with a sigh."
    voice "audio/voice/masami/masami_huh.mp3"
    m "(Where? I still don't - )"
    show bg bedroom at shake
    play sound "audio/sound/bed_bounce.mp3" volume 0.3
    n "His hand hits something fluffy right behind him."
    m sad "(Oh. Well. Guess today is just one of those days.)"
    n "Masami props the pillow behind his head, where it's supposed to go."
    $ masami_glasses = True
    n "Then, he puts on his glasses and picks up his phone."
    m "(It's almost twelve. Half the day is gone.)"
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "(To think that I expected the world to end or something after what I did yesterday...)"
    m sad "..."
    m "(It feels…kinda weird.)"
    m neutral "(But also kinda nice, actually.)"
    n "He hums a little to himself as he unlocks his phone."
    voice "audio/voice/masami/masami_oh.mp3"
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
        play sound "audio/sound/phone_vibrate.mp3"
        queue sound "audio/sound/phone_vibrate.mp3"
        n "Just then, Masami's phone starts buzzing again."
        voice "audio/voice/masami/masami_quietsigh.mp3"
        m exasperated "(Dammit. It's the group chat.)"
        m sad "(Wonder what they're up to now.)"

        jump phone2a_gc

# Masami chose to check Rohan's message - on phone
label phone2a_rohan:

    call phone_open(True,"Rohan") from _call_phone_open

    call message(r, "Hey", True) from _call_message
    call message(r, "About the mall pics from a couple days ago") from _call_message_1
    call message(r, "I think I found one thats not bad if u want to look") from _call_message_2
    call message(r, "Not ready to post in gc yet") from _call_message_3

    call phone_close() from _call_phone_close

    menu:

        "Respond":
            $ rohan_respond = True
            jump phone2a_rohan_respond

        "Ignore":
            $ rohan_respond = False
            jump phone2a_rohan_ignore

# Reply to Rohan's message
label phone2a_rohan_respond:

    call phone_open(False, "Rohan", False) from _call_phone_open_1

    # On phone portion
    call message(m, "Yeah sure", True) from _call_message_4
    call message(r, "Kk give me one sec", True) from _call_message_5
    call message("Image", "cg/Rohan_Mall.webp") from _call_message_6
    show cg Rohan_Mall:
        alpha 0.0
    pause(0.01)
    hide cg Rohan_Mall
    call message(r, "Sabie helped me pick") from _call_message_7
    call message(r, "Makeup isnt very good since I did it myself this time") from _call_message_8
    call message(r, "It isnt too bad is it") from _call_message_9
    call message(m, "You look great", True) from _call_message_10
    call message(r, "...", True) from _call_message_11
    call message(m, "You don't believe me?", True) from _call_message_12
    call message(r, "Uh", True) from _call_message_13
    call message(r, "You always say stuff like that so I cant tell if youre just trying to make me feel better") from _call_message_14
    call message(m, "...", True) from _call_message_15
    call message(r, "Sabie does that too", True) from _call_message_16
    call message(m, "Well, we are being honest", True) from _call_message_17
    call message(r, "Maybe", True) from _call_message_18
    call message(r, "Sometimes I wonder if that would change if she knew") from _call_message_19
    call message(m, "Knew what?", True) from _call_message_20
    call message(r, "Like what I told you about before", True) from _call_message_21
    call message(m, "Oh, that.", True) from _call_message_22
    call message(m, "Nah, I don't think she'd treat you any differently if she knew you felt that way about her") from _call_message_23
    call message(r, "I hope so", True) from _call_message_24
    call message(m, "Why ask?", True) from _call_message_25
    call message(r, "Dunno just thinking", True) from _call_message_26
    call message(m, "Ah", True) from _call_message_27
    call message(r, "Wanna coop", True) from _call_message_28
    call message(r, "I can carry you") from _call_message_29
    call message(m, "I'll think about it", True) from _call_message_30
    call message(r, "Kk", True) from _call_message_31
    call message(r, "Oh") from _call_message_32
    call message(r, "I almost forgot") from _call_message_33
    call message(r, "I have leftover gingerbread cookies if u want extra") from _call_message_34
    call message(m, "I'm good, thanks.", True) from _call_message_35
    call message(r, "U sure", True) from _call_message_36
    call message(m, "Yeah. I'll let you know if I want any.", True) from _call_message_37
    call message(r, "Kk", True) from _call_message_38

    call phone_close() from _call_phone_close_1

    # Off phone portion
    show masami at mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m neutral "(Ahh, I'd actually kill for one of those cookies right now. Or anything he'd make.)"
    m sad "(But I also don't feel like seeing anyone today.)"
    m "…"
    m "(Guess I'll have to ask him later when I'm feeling up to it.)"

    jump phone2a

# Ignore Rohan's message - off phone
label phone2a_rohan_ignore:

    show masami at mc_pos
    voice "audio/voice/masami/masami_hm.mp3"
    m sad "(I wouldn't mind seeing it, but…)"
    m neutral "(It wouldn't hurt if I delayed replying by a day or two.)"

    jump phone2a

# Masami chose to check Sabie's message - on phone
label phone2a_sabie:

    call phone_open(True) from _call_phone_open_2

    call message(s, "{b}This message was deleted.{/b}", True) from _call_message_39
    call message(s, "sry {i}ge{/i} my bad") from _call_message_40
    call message(s, "ignore me") from _call_message_41

    call phone_close() from _call_phone_close_2

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

    call phone_open(False, "Sabie", False) from _call_phone_open_3

    call message(m, "Okay.", True) from _call_message_42
    call message(s, "bruh", True) from _call_message_43
    call message(s, "you didnt listen >:(") from _call_message_44
    call message(m, "What else did you expect me to do?", True) from _call_message_45
    call message(s, "idk", True) from _call_message_46
    call message(s, "just not respond ig") from _call_message_47
    call message(m, "Okay.", True) from _call_message_48
    call message(m, "But what was it?") from _call_message_49
    call message(s, "...", True) from _call_message_50
    call message(m, "Are you actually embarrassed?", True) from _call_message_51
    call message(s, "no ofc not", True) from _call_message_52
    call message(m, "Why no show?", True) from _call_message_53
    call message(s, "do u wanna see drunk pics again", True) from _call_message_54
    call message(m, "No?", True) from _call_message_55
    call message(s, "there u go", True) from _call_message_56
    call message(m, "...", True) from _call_message_57
    call message(s, "what", True) from _call_message_58
    call message(m, "Nothing.", True) from _call_message_59
    call message(m, "Nothing at all. (:") from _call_message_60
    call message(s, "...", True) from _call_message_61
    call message(s, "are u trying to blackmail me again") from _call_message_62
    call message(m, "Blackmail? When have I blackmailed you?", True) from _call_message_63
    call message(s, "uh all the time", True) from _call_message_64
    call message(m, "Like what", True) from _call_message_65
    call message(s, "is threatening to tell my parents about me going out to have fun not blackmail", True) from _call_message_66
    call message(m, "No, that's me looking out for you", True) from _call_message_67
    call message(m, "I don't like seeing you getting wasted every weekend") from _call_message_68
    call message(s, "but you keep your mouth shut about rohan doing theatre in front of his parents", True) from _call_message_69
    call message(s, "thats very fair") from _call_message_70
    call message(s, "no problems at all") from _call_message_71
    call message(m, "That's different. His parents are worse than yours and you know it.", True) from _call_message_72
    call message(s, ":P", True) from _call_message_73
    call message(s, "whatevs") from _call_message_74
    call message(s, "anyways") from _call_message_75
    call message(s, "how are quizbowl qs going") from _call_message_76
    call message(s, "i need my steady supply of nerd qs to torture the kiddos with") from _call_message_77
    call message(m, "Nerd qs", True) from _call_message_78
    call message(s, "yes nerd qs", True) from _call_message_79
    call message(s, "you need something to keep you busy") from _call_message_80
    call message(s, "and i don’t want to touch any of your gross sciencey math shit") from _call_message_81
    call message(m, "You know, if you keep insulting me, I won't help you.", True) from _call_message_82
    call message(s, "see theres the blackmail right there", True) from _call_message_83
    call message(m, "(:", True) from _call_message_84
    call message(s, "ugh ur hopeless", True) from _call_message_85
    call message(s, "bye") from _call_message_86
    call message(m, "Okay, bye.", True) from _call_message_87

    call phone_close() from _call_phone_close_3

    # Off phone portion
    show masami at mc_pos
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m neutral "(Well, at least things seem normal with her.)"
    m sad "…"
    m "(It's nice that she's not bringing up {i}jie{/i}, but I kind of wish she would.)"

    jump phone2a

# Ignore Sabie's Message - off phone
label phone2a_sabie_ignore:

    show masami at mc_pos
    voice "audio/voice/masami/masami_whatever.mp3"
    m neutral "(Well, she said to ignore it, so that's what I'm gonna do.)"

    jump phone2a

# Masami chose to check Tyree's message - on phone
label phone2a_tyree:

    call phone_open(True, "Tyree") from _call_phone_open_4

    call message(t, "Let me know if you want me to take over anything for you.", True) from _call_message_88
    call message(t, "You do not need to reply, but I am here if you need me.") from _call_message_89

    call phone_close() from _call_phone_close_4

    menu:

        "Respond":
            $ tyree_respond = True
            jump phone2a_tyree_respond

        "Ignore":
            $ tyree_respond = False
            jump phone2a_tyree_ignore

# Masami responds to Tyree
label phone2a_tyree_respond:

    call phone_open(False, "Tyree", False) from _call_phone_open_5

    # On-phone portion
    call message(m, "Hey thanks for reaching out", True) from _call_message_90
    call message(m, "I think I'm good for now, but I'll let you know") from _call_message_91
    call message(t, "Alright.", True) from _call_message_92
    call message(m, "Oh yeah, I forgot to ask", True) from _call_message_93
    call message(m, "Are there any more sponsors I need to reach out to or grants I should apply for before the season starts?") from _call_message_94
    call message(m, "Our budget is looking a bit tight right now") from _call_message_95
    call message(t, "There are a few, but I can manage them.", True) from _call_message_96
    call message(m, "You sure?", True) from _call_message_97
    call message(m, "You're not too busy with swim captaining and recruiting?") from _call_message_98
    call message(m, "Or helping Sabie with Quizbowl?") from _call_message_99
    call message(t, "Don't worry, I can do it.", True) from _call_message_100
    call message(m, "You sure?", True) from _call_message_101
    call message(t, "I'm sure.", True) from _call_message_102
    call message(t, ":)") from _call_message_103
    call message(m, "Alright, I'll take your word for it.", True) from _call_message_104
    call message(m, "Let me know if you need me to look over anything!") from _call_message_105
    call message(t, "Okay!", True) from _call_message_106

    call phone_close() from _call_phone_close_5

    # Off-phone portion
    show masami at mc_pos
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "(That was nice.)"
    m sad "…"
    m "(I know he can handle it, but I still feel bad about giving him so much to do.)"

    jump phone2a

# Masami chooses to ignore the message
label phone2a_tyree_ignore:

    show masami at mc_pos
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m neutral "(I appreciate that.)"
    m "(I'll just leave the message as is. Tyree understands.)"
    m sad "(Besides, he'll probably have his hands full enough once the school realizes what I've done.)"
    m "…"
    m exasperated "(Whatever. It's too late to change anything.)"

    jump phone2a

# Masami responds to the group chat - on phone
label phone2a_gc:

    hide masami

    call phone_open(True,"Group") from _call_phone_open_6

    call message(s, "yo", True) from _call_message_107
    call message(s, "did yall see that") from _call_message_108
    call message(r, "See what", True) from _call_message_109
    call message(s, "the vandalism thing", True) from _call_message_110
    call message(s, "someone absolutely lost their shit") from _call_message_111
    call message(r, "Uh...", True) from _call_message_112
    call message(r, "But hasnt everyone lost their shit") from _call_message_113
    call message(s, "well yeah", True) from _call_message_114
    call message(r, "Except for like tyree", True) from _call_message_115
    call message(s, "also yeah", True) from _call_message_116
    call message(s, "bc hes just special like that") from _call_message_117
    call message(r, "Truee", True) from _call_message_118
    call message(t, "Okay.", True) from _call_message_119
    call message(s, "anyways somebody really snapped this time", True) from _call_message_120
    call message(s, "went savagely poetic spitting them facts") from _call_message_121
    call message(s, "it was beautiful <3") from _call_message_122
    call message(r, "Uh...", True) from _call_message_123
    call message(s, "what", True) from _call_message_124
    call message(s, "ik art when i see it") from _call_message_125
    call message(r, "Im not questioning that", True) from _call_message_126
    call message(r, "You just sound suspiciously like the one who did it") from _call_message_127
    call message(s, "lmaoo i wish", True) from _call_message_128
    call message(s, "i don’t have the balls to do that") from _call_message_129
    call message(s, "i just drink and drive :3") from _call_message_130
    call message(r, "...", True) from _call_message_131
    call message(s, "ur judging me arent u -_-", True) from _call_message_132
    call message(r, "No, ofc not!", True) from _call_message_133
    call message(t, "Lol.", True) from _call_message_134
    call message(s, "i agree rohan is very sus", True) from _call_message_135
    call message(r, "Hey!", True) from _call_message_136
    call message(t, ":)", True) from _call_message_137
    call message(s, "anyways, im not crazy enough to risk my perfect school record with a suspension ^.^", True) from _call_message_138
    call message(r, "Yeah I feel kinda bad for whoever did it", True) from _call_message_139
    call message(r, "Its like academic suicide") from _call_message_140
    call message(s, "psh now you sound like masami", True) from _call_message_141
    call message(r, "Lol for real though, I scared myself channeling that energy", True) from _call_message_142
    call message(t, "I just hope whoever it is finds the help they need.", True) from _call_message_143
    call message(s, "ykw ur right", True) from _call_message_144
    call message(s, "we should all be nice people like tyree") from _call_message_145
    call message(s, "right {i}ge{/i}") from _call_message_146
    call message(s, "...") from _call_message_147
    call message(s, "......") from _call_message_148
    call message(t, ".........", True) from _call_message_149
    call message(r, "Uh...", True) from _call_message_150
    call message(s, "guess hell see this later", True) from _call_message_151
    call message(r, "*he'll", True) from _call_message_152
    call message(s, "**hell", True) from _call_message_153
    call message(t, "He's probably taking some time off.", True) from _call_message_154
    call message(r, "or just watching us", True) from _call_message_155
    call message(s, "truu he really likes lurking", True) from _call_message_156
    call message(r, "Lol", True) from _call_message_157
    call message(s, "heyo {i}gegeee{/i}", True) from _call_message_158
    call message(s, "if youre reading this i just wanna say that you gotta let go like vandal dude") from _call_message_159
    call message(s, "but not too much like vandal dude") from _call_message_160
    call message(s, "u will feel better i promiseee") from _call_message_161

    call phone_close() from _call_phone_close_6

    jump masami_room2c

    # You're done responding
label masami_room2c:

    show masami at mc_pos

    play sound "audio/sound/phone_vibrate.mp3" volume 0.6 loop
    n "Masami casually lets his phone drop onto his stomach. It keeps buzzing, but he doesn't bother to pick it up."
    stop sound
    m "(If only you knew, Sabie.)"
    m "(If only you knew how temporary that relief was.)"
    voice "audio/voice/masami/masami_whatever.mp3"
    m sad "…"
    n "His stomach rumbles."
    m neutral "(Right. Mom's probably making lunch right now.)"
    m sad "(...I probably owe her an apology since I didn't give her one last night either.)"
    m "(Not sure if I even want to say anything.)"
    m "(No matter what I say, she still wouldn't really understand. She never has.)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "…"
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
    play sound "audio/sound/boil.mp3" volume 0.1 fadein 3.0
    n "He walks in to find his mother with her apron on and back turned, having just finished cooking."
    stop sound fadeout 10.0
    n "She turns off the heat on the bok choi she was stir-frying in a wok. A clay pot sits on low heat on the back burner."
    voice "audio/voice/masami/masami_oh.mp3"
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
    voice "audio/voice/masami/masami_nevermind.mp3"
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
    voice "audio/voice/masami/masami_hm.mp3"
    m "Okay. Thanks."
    play sound "audio/sound/plates.mp3"
    n "He grabs a plate and spoon from the cupboard, helping himself to some food."

    jump masami_room2d

# Masami choses to ignore his mom
label masami_kitchen2_ignore:

    play sound "audio/sound/plates.mp3"
    n "Masami grabs a plate and spoon from the cupboard. His mom watches in silence as he helps himself to the food."
    voice "audio/voice/masami/masami_quietsigh.mp3"
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

    play sound "audio/sound/door_open.mp3"
    queue sound "audio/sound/door_close.mp3"
    n "Masami heads back to his room, where he eats in silence."
    m neutral "(This is really good. I actually feel better now.)"
    m sad "(Sort of.)"
    n "Despite himself, he instinctively turns to look out the window."
    voice "audio/voice/masami/masami_whatever.mp3"
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
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "(Heh. Younger me definitely had the patience for that.)"
    m "(But now? For some reason, I can't get myself to read for fun anymore.)"
    jump masami_room2_explore

# If the backpack option is selected
label masami_room2_study:

    $ room_study = False
    voice "audio/voice/masami/masami_hm.mp3"
    m "(Right. I still need to do that.)"
    m "…"
    m "(I don't really think I can focus on that now.)"
    jump masami_room2_explore

# If the computer option is selected
label masami_room2_games:

    voice "audio/voice/masami/masami_oh.mp3"
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

    play sound "<from 0 to 2.6>audio/sound/phone_ring.mp3"
    queue sound "audio/sound/footsteps_walk2.mp3"
    queue sound "audio/sound/phone_ring.mp3"
    n "A few hours later, he is faintly aware of the ringing of the telephone and the soft clack of his mom's slippers as she goes to pick it up."

    stop sound
    play music reflective fadein 2.0

    mm "Hello?"
    mm "Yes."
    mm "Yes..."
    mm "Oh."
    n "His mom goes silent, not saying a word as she hangs up the phone."
    n "Masami hears his father, who must have come home some time ago, say something indiscernible to her and the two of them speak in hushed whispers."
    n "A moment later, he hears his mother's muffled sobbing."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "(...The school called them about the vandalism, didn't they?)"
    n "A lump forms in Masami's throat. He swallows hard and stares at his hands."
    n "They're shaking."
    m "(Is this what {i}jie{/i} felt like whenever she disappointed someone?)"
    m exasperated "(How did she learn to stop caring?)"
    n "He squeezes his fists tight, only vaguely noticing the way his nails dig into his palms."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "(I…)"
    show masami sad
    n "His eyes snap back open, roaming around in every direction besides the window and the door."
    n "They settle on the phone face down on his desk."
    m "(Rohan, Sabie, Tyree...none of them know, do they?)"
    m exasperated "(...With what they thought about the vandalism, do I even want them to know?)"
    show masami sad
    n "His fingers gingerly trace the shell of the case before flipping it over, screen side up."
    show masami surprised
    voice "audio/voice/masami/masami_huh.mp3"
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

    call phone_open(True, "???") from _call_phone_open_7

    call message("???", "You're really a brave one, aren't you, magpie?", True) from _call_message_162
    call message("???", "Your sister must be proud of you. :)") from _call_message_163

    call phone_close() from _call_phone_close_7

    jump masami_dayend

# Masami reflects on it, scene cut
label masami_dayend:

    show masami at mc_pos

    n "Masami feels his chest warm."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "(Ah, so it was you.)"
    n "He delicately traces the outline of the text bubbles with his thumb."
    m happy "(You think she's proud of me, huh?)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "..."
    m "(Is that what I even want anymore?)"

    scene bg black
    hide masami
    with Dissolve(3.0)
    stop music fadeout 2.0

    jump day_2_transition
