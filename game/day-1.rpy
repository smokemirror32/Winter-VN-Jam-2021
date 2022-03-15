## DAY 1 - BEFORE

label day_1_transition:

    pause(2.0)
    show text "{size=+50}Day 1 - Before{/size}" at trans_text with Dissolve(2.0)
    pause(1.0)
    show text "{size=+50}Day1-Before{/size}" at glitch, glitch_trans_text
    pause(0.5)
    show text "{size=+50}Day 1 - Before{/size}" at trans_text
    pause(1.5)
    hide text with Dissolve(2.0)
    pause(2.0)

    jump class_1

label class_1:

    scene bg hallway
    show masami at mc_pos
    with Dissolve(1.0)
    play music lighthearted fadein 1.0

    # SEFF: SCHOOL BELL RING
    m "Thanks, Mr. Friedman! Happy holidays to you, too!"
    n "Masami waves goodbye to his physics teacher before he steps out of the classroom, joining the sea of students heading to lunch."
    voice "audio/voice/masami/masami_hm.mp3"
    m happy "(Phew. I can't believe that - )"
    play sound "audio/sound/phone_vibrate.mp3"
    n "Suddenly, his phone buzzes in his pocket."
    m neutral "(Hm. It's probably Sabie again. I wonder what she's up to this time.)"

    jump phone_1a

# Glitch ON
label phone_1a:

    hide masami
    stop music fadeout 1.0

    call phone_open(True) from _call_phone_open_8
    show glitch_filter onlayer glitching with Dissolve(1.0)
    play music chaos
    call message(s, "Hey dumbass. I know who you really are. It'd be a shame if I told everyone, wouldn't it? ;)", True) from _call_message_164
    call phone_close() from _call_phone_close_8

    jump class_1_panik

# Glitch OFF, cuts back to Masami
label class_1_panik:

    hide glitch_filter onlayer glitching
    show masami surprised at mc_pos
    n "Masami nearly drops his phone."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "What the hell?"
    show masami sad
    n "He nervously picks up his phone again."

    jump phone_1b

# The previous message disappears from the screen revealing the actual message:
label phone_1b:

    stop music fadeout 1.0
    hide masami

    call phone_open(True) from _call_phone_open_9

    call message(s, "dude", True) from _call_message_165
    call message(s, "rohan is bullying me again") from _call_message_166
    call message(s, "send help :(") from _call_message_167

    call phone_close() from _call_phone_close_9

    jump class_1_kalm

# Cuts back to Masami
label class_1_kalm:

    play music lighthearted fadein 1.0
    show masami sad at mc_pos

    n "Masami exhales slowly and slides the phone back into his pocket."
    voice "audio/voice/masami/masami_oh.mp3"
    m neutral "(It's okay. I'm just seeing things.)"
    n "He rubs his temples."
    show masami exasperated at shake, mc_pos
    m "(Dammit. I should have gotten back earlier last night. Three hours is definitely not enough sleep.)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "..."
    m neutral "(I'll just reply to Sabie in person.)"

    jump lunch_1a

# Back to lunch
label lunch_1a:

    stop music fadeout 1.0
    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg courtyard
    show masami at mc_pos
    with Dissolve(1.0)
    play music uptempo fadein 1.0

    n "As per usual, Masami hears the chaos long before he sees it."
    m "Well. Here we go again. Might as well try to end this one before it starts."

    show rohan annoyed at right
    show sabie annoyed at left
    with Dissolve(0.1)

    n "He hurries in as quickly as he can to find Rohan and Sabie engaged in another one of their tabletop battles."
    show rohan at shake, right
    voice "audio/voice/rohan/rohan_seriously.mp3"
    r "Hey, let go of my phone!"
    show sabie at shake, left
    voice "audio/voice/sabie/sabie_hmmmm.mp3"
    s "But you gotta delete those videos you took of me last night."
    r "What? No! They were good videos."
    r sad "Besides I - I wasn't even planning on sharing them."
    s "I don't trust you. You sent those drunk karaoke videos last time without a second thought."
    show rohan annoyed at shake, right
    voice "audio/voice/rohan/rohan_um.mp3"
    r "But Smash videos are different!"
    s "No, they are not."
    r sad "Why?"
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s worried "Ugh, spare me, will you? The number of times I suicided with Kirby was - "

    show sabie surprised

    n "Suddenly she freezes when she catches sight of Masami."

    jump sabie_glitching

label sabie_glitching:

    stop music fadeout 1.0

    s mischievous "Oh. Hey. Look who it is."

    # Depending on if you supported Sabie on the third day
    # GLITCH ON

    show glitch_filter onlayer glitching with Dissolve(1.0)
    play music chaos fadein 1.0

    show rohan at glitch
    pause(0.05)
    show rohan
    pause(0.05)
    hide rohan with Dissolve(0.2)
    call sabie_glitch() from _call_sabie_glitch
    call sabie_spaz() from _call_sabie_spaz

    if support == "Sabie":

        call sabie_spaz()
        voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
        s "Feel like coming to help me again?"
        call sabie_spaz() from _call_sabie_spaz_2
        s "Or are you going to leave me out to dry like you did to Alyssa because you've got commitment issues?"
        call sabie_spaz() from _call_sabie_spaz_3
        s "I should hope that a good old family friend means something to you, {i}ge{/i}."
        call sabie_spaz()
        call sabie_spaz()
        voice "audio/voice/sabie/sabie_gotcha.mp3"
        s innocent "But then again, Xinyi did decide to leave her poor little brother behind."
        call sabie_spaz() from _call_sabie_spaz_6
        s happy "Who knows how much more you've learned from her? You two were close after all."

    else:

        call sabie_spaz()
        voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
        s "Are you going to help me this time?"
        call sabie_spaz() from _call_sabie_spaz_8
        s "Or are you going to leave me to suffer alone?"
        call sabie_spaz() from _call_sabie_spaz_9
        s "I wonder if it's worth it for me to care about someone who didn't care for me back."
        call sabie_spaz()
        voice "audio/voice/sabie/sabie_gotcha.mp3"
        s innocent "That's what Xinyi did to you, after all."
        call sabie_spaz() from _call_sabie_spaz_11
        call sabie_spaz() from _call_sabie_spaz_12
        s happy "It's only fair that you take it out on the rest of us, right {i}ge{/i}?"

    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "W-What? When did I ever think that?"

    # Glitch OFF
    stop music fadeout 2.0
    show sabie worried:
        ease 40 zoom 1.0
    show rohan sad at right with Dissolve(1.0)
    hide glitch_filter onlayer glitching with Dissolve(2.0)
    play music uptempo fadein 2.0

    voice "audio/voice/sabie/sabie_uh.mp3"
    s "Uh…I guess you could start thinking about helping me right about now. Kinda in a tough spot, as you can see."
    m sad "Ah."
    n "Masami swallows."
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "Rohan, maybe this time if you - "
    voice "audio/voice/rohan/rohan_defeatedsigh.mp3"
    r "Does it matter what I do?"
    stop music fadeout 1.0

    # Glitch ON

    show glitch_filter onlayer glitching with Dissolve(1.0)
    play music chaos fadein 1.0

    show sabie at glitch
    pause(0.05)
    show sabie
    pause(0.05)
    hide sabie with Dissolve(0.2)
    call rohan_glitch() from _call_rohan_glitch
    call rohan_spaz() from _call_rohan_spaz
    call rohan_spaz() from _call_rohan_spaz_1

    r annoyed "I’ll answer that question for you. No, it doesn't."
    call rohan_spaz() from _call_rohan_spaz_2
    r "You're the only one here that she'll even listen to and you know that."
    if support == "Rohan":

        call rohan_spaz() from _call_rohan_spaz_3
        r "Stand up for me like you did last time."
        call rohan_spaz()
        call rohan_spaz()
        voice "audio/voice/rohan/rohan_igiveup.mp3"
        r sad "Or do I not matter to you either?"

    else:

        call rohan_spaz() from _call_rohan_spaz_6
        r sad "But definitely, go ahead. Let her walk all over to me."
        call rohan_spaz()
        call rohan_spaz()
        voice "audio/voice/rohan/rohan_igiveup.mp3"
        r "I won't care."

    show masami surprised at shake, mc_pos
    m "N-No! It's not like that. I care about you guys, I promise."
    # Glitch OFF

    stop music fadeout 2.0
    show rohan:
        ease 40 zoom 1.0
    show sabie worried at left with Dissolve(1.0)
    hide glitch_filter onlayer glitching with Dissolve(2.0)
    play music uptempo fadein 2.0

    n "Sabie and Rohan exchange glances. The phone hangs between them in their limp grasps, forgotten. "
    voice "audio/voice/rohan/rohan_um.mp3"
    r neutral "Uh, we already knew that part, but thanks."
    s "Is there something that you're thinking too hard about, {i}ge{/i}?"
    show masami at shake, mc_pos
    m "I - "
    show masami neutral
    n "Masami runs his hand through his hair."
    voice "audio/voice/masami/masami_im...fine.mp3"
    m happy "It's nothing. Just tired. You know what happens when you don't get those eight hours."
    n "Sabie and Rohan just stare at him."
    m exasperated "(Shit. I should have known they wouldn't buy it. Not when they've got a worse sleep schedule than me.)"

    show tyree
    hide sabie
    hide rohan

    voice "audio/voice/tyree/tyree_ah.mp3"
    t "Ah."
    show masami surprised at shake, mc_pos
    m "Wait, when did you - "
    n "His eyes land on Tyree's usual spot where he is indeed sitting and eating his salad."
    t "Same time as always."
    m neutral "Oh."
    m happy "Sorry, I am really out of it today."

    stop music fadeout 1.0

    voice "audio/voice/tyree/tyree_hm.mp3"
    t "Hm."

    # Glitch ON

    show glitch_filter onlayer glitching with Dissolve(1.0)
    play music chaos fadein 1.0
    call tyree_glitch() from _call_tyree_glitch
    call tyree_spaz() from _call_tyree_spaz

    t happy "There is no use trying to destroy who you once were."
    if support == "Tyree":

        call tyree_spaz() from _call_tyree_spaz_1
        t "You may be able to ignore others for a short while, but you cannot ignore them forever."
        call tyree_spaz() from _call_tyree_spaz_2
        t "Not if you've expressed affection for them before. It will be too late then."
        call tyree_spaz()
        voice "audio/voice/tyree/tyree_quietchuckle.mp3"
        t neutral "They will always want the old you back. As they should."
        call tyree_spaz() from _call_tyree_spaz_4
        call tyree_spaz() from _call_tyree_spaz_5
        t worried "What will they say when you cannot return to them?"

    else:

        call tyree_spaz() from _call_tyree_spaz_6
        t "People will always expect the same good thing out of you once you've given it to them before."
        call tyree_spaz() from _call_tyree_spaz_7
        t "They will accept no less and we must follow through."
        call tyree_spaz()
        voice "audio/voice/tyree/tyree_quietchuckle.mp3"
        t neutral "This is how we become who we need to be."
        call tyree_spaz() from _call_tyree_spaz_9
        call tyree_spaz() from _call_tyree_spaz_10
        t worried "Is it too much to ask for, to make a wise decision more than once?"

    hide tyree

    show layer master at hpunch
    show masami surprised at hpunch, mc_pos
    n "Masami backs up quickly, colliding into a nearby tree. His hands reach backwards around the trunk."
    # Glitch OFF
    hide glitch_filter onlayer glitching with Dissolve(2.0)
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "I - I..."
    show masami exasperated at shake, mc_pos
    m "Look, I don't know what I should do anymore."
    m "If I help Rohan, Sabie complains. If I help Sabie, Rohan complains. If I leave you both alone, you both complain."
    m angry "I can't win. So, stop trying to make me play your fucking game, okay?"

    jump lunch_1b

label lunch_1b:

    show rohan sad at right
    show sabie worried at left

    r "..."
    s "..."

    show tyree worried
    hide rohan
    hide sabie

    t "..."

    hide tyree
    show rohan sad at right
    show sabie worried at left

    n "Sabie lets go of the phone and nudges it back to Rohan. Rohan quietly pockets it, eyes trained on Masami."
    voice "audio/voice/sabie/sabie_uh.mp3"
    s "{i}Ge{/i}. What happened last night?"
    m sad "Last night?"
    s "Something happened last night or you wouldn't be acting like this."
    n "Masami inhales slowly."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Nothing happened. I have no idea what you're talking about."

    show sabie annoyed at center with move
    show sabie:
        ease 1.5 zoom 1.05
    show rohan neutral

    play sound "audio/sound/footsteps_walk1.mp3"
    n "Sabie gets up and walks over to him very slowly, her fists balled."
    n "She stops when she's inches away and stares up at him, unflinching."
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s "Don't even try that on me, dumbass. I thought you knew better than that."

    show sabie at shake, center

    n "She pokes him hard on the forehead."
    show masami angry at shake, mc_pos
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "Ow! What was that for?"
    s "Your idiocy."
    s worried "Look, I really didn't want things to go this way, but you're not giving me a choice."
    s "I let you get away with holding those stupid thoughts in your head last time."

    # Glitch ON - will stay on until Masami enters house

    show glitch_filter onlayer glitching with Dissolve(1.0)
    call sabie_spaz() from _call_sabie_spaz_13
    s mischievous  "And what did you do?"

    show rohan at glitch
    pause(0.05)
    show rohan
    pause(0.05)
    hide rohan with Dissolve(0.2)
    call sabie_glitch() from _call_sabie_glitch_1
    call sabie_spaz() from _call_sabie_spaz_14

    # Depends if you visited Alyssa first or not
    if alyssa_visit_first:

        voice "audio/voice/sabie/sabie_gotcha.mp3"
        s innocent "You ditch the girl you've been pining over for years as if it were nothing."
        call sabie_spaz() from _call_sabie_spaz_15
        s happy "I'll give you credit for even having the balls to go straight to her in the first place."
        call sabie_spaz() from _call_sabie_spaz_16
        s "But still."

    else:

        voice "audio/voice/sabie/sabie_gotcha.mp3"
        s innocent "You waste so much time trying to decide whether or not you actually want to get the idiot you've been pining over for years."
        call sabie_spaz() from _call_sabie_spaz_17
        s happy "Then after you finally work up the fucking nerve, you just ditch her."

    call sabie_spaz() from _call_sabie_spaz_18
    call sabie_spaz() from _call_sabie_spaz_19
    s mischievous "Incredibly rude."
    call sabie_spaz() from _call_sabie_spaz_20
    call sabie_spaz() from _call_sabie_spaz_21
    s "Waste of my efforts."

    # Depends if you trusted Sabie with the Xinyi response earlier on Day 3 - Before
    if sabie_trust:

        call sabie_spaz()
        voice "audio/voice/sabie/sabie_imean.mp3"
        s happy "You told me something was wrong before and I supported you."
        call sabie_spaz() from _call_sabie_spaz_23
        s "What about that wasn't enough for you that you had to clam up like this again?"

    else:

        call sabie_spaz()
        voice "audio/voice/sabie/sabie_imean.mp3"
        s happy "Don't you care that there are people out here trying to help you at all?"
        call sabie_spaz() from _call_sabie_spaz_25
        s "Was it worth it being so damn selfish that you couldn't even bother to explain yourself? Not even to me when I fucking asked you what was wrong?"

    call sabie_spaz() from _call_sabie_spaz_26
    call sabie_spaz() from _call_sabie_spaz_27
    call sabie_spaz() from _call_sabie_spaz_28
    s "What on earth is going on in your head that's worth keeping from the rest of us?"
    call sabie_spaz() from _call_sabie_spaz_29
    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "I - "
    call sabie_spaz() from _call_sabie_spaz_30
    m "I don’t know."

    jump lunch_1c

label lunch_1c:

    call sabie_glitch_big()
    call sabie_spaz()
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s mischievous "Pft. Of course you know yourself, silly."

    # Depends on if you answered Sabie's message on Day 2 - After
    if sabie_respond:
        call sabie_spaz() from _call_sabie_spaz_32
        s "The day after you painted that wall with your word vomit, you had the audacity to text me like everything was perfectly normal."
        call sabie_spaz() from _call_sabie_spaz_33
        s "How sick of you think you could hide such a monster from yourself."
    else:
        call sabie_spaz() from _call_sabie_spaz_34
        s "You knew enough that you decided to leave me on read. On read!"
        call sabie_spaz() from _call_sabie_spaz_35
        s "On no circumstance do you ever leave some on read, even if they fucked up and sent a deleted message to you."
        call sabie_spaz() from _call_sabie_spaz_36
        s "You have to at least leave an emoji."

    call sabie_spaz()
    call sabie_spaz()
    voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
    s happy "Sometimes, I really can't believe you."

    show masami at shake, mc_pos
    m "But - "

    # Depends on if you answered Rohan's message

    show rohan annoyed at right behind sabie
    call rohan_spaz() from _call_rohan_spaz_9
    call sabie_spaz() from _call_sabie_spaz_39
    call rohan_glitch() from _call_rohan_glitch_1
    call rohan_spaz() from _call_rohan_spaz_10

    voice "audio/voice/rohan/rohan_seriously.mp3"
    r "Don't even try lying to yourself."
    call rohan_spaz() from _call_rohan_spaz_11
    call sabie_spaz() from _call_sabie_spaz_40
    r sad "Just look at how you've treated me!"

    if rohan_respond:
        call rohan_spaz() from _call_rohan_spaz_12
        call sabie_spaz() from _call_sabie_spaz_41
        r "You respond to my photos just to be nice. I know that you do."
        call rohan_spaz() from _call_rohan_spaz_13
        call sabie_spaz() from _call_sabie_spaz_42
        r "You wouldn't dare tell me otherwise or you think I'll go even further off the rails."
        call rohan_spaz()
        call sabie_spaz()
        call rohan_spaz()
        voice "audio/voice/rohan/rohan_defeatedsigh.mp3"
        r "Just like your sister."
        call rohan_spaz() from _call_rohan_spaz_16
        call sabie_spaz() from _call_sabie_spaz_44
        r "And you didn't want that happening, did you?"
    else:
        call rohan_spaz() from _call_rohan_spaz_17
        call sabie_spaz() from _call_sabie_spaz_45
        r "You couldn't even spend a moment to look at a single photo."
        call rohan_spaz()
        call sabie_spaz()
        call rohan_spaz()
        voice "audio/voice/rohan/rohan_defeatedsigh.mp3"
        r "It wasn't even much to ask for. Just a glance to say that you supported me when I needed it."

    show rohan happy
    call rohan_glitch_big() from _call_rohan_glitch_big
    call rohan_spaz() from _call_rohan_spaz_20
    call sabie_spaz() from _call_sabie_spaz_47
    r happy "But definitely, believe what you want. That you actually look good in the eyes of others."
    call sabie_spaz()
    call rohan_spaz()
    voice "audio/voice/rohan/rohan_nervouslaughter.mp3"
    r "Keep your pathetic little image of yourself as the golden boy."
    call sabie_spaz() from _call_sabie_spaz_49
    call rohan_spaz() from _call_rohan_spaz_22
    show masami angry at shake, mc_pos
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "What the hell are you talking about?"
    call rohan_spaz() from _call_rohan_spaz_23
    call sabie_spaz() from _call_sabie_spaz_50
    m sad "Of course I'm not perfect! Of all people, you'd think I know that by now."

    # Depends on if you answered Tyree's message

    show tyree at left behind sabie
    call tyree_spaz() from _call_tyree_spaz_11
    call rohan_spaz() from _call_rohan_spaz_24
    call tyree_glitch() from _call_tyree_glitch_1
    call tyree_spaz() from _call_tyree_spaz_12
    call sabie_spaz() from _call_sabie_spaz_51

    voice "audio/voice/tyree/tyree_no.mp3"
    t "We know you aren't."
    call sabie_spaz() from _call_sabie_spaz_52
    call tyree_spaz() from _call_tyree_spaz_13
    call rohan_spaz() from _call_rohan_spaz_25
    t worried "But that's the problem lies, I'm afraid."

    if tyree_respond:
        call tyree_glitch_big() from _call_tyree_glitch_big
        call rohan_spaz() from _call_rohan_spaz_26
        call sabie_spaz() from _call_sabie_spaz_53
        call tyree_spaz() from _call_tyree_spaz_14
        t "You always care too much about what others think."
        call tyree_spaz()
        call rohan_spaz()
        call sabie_spaz()
        voice "audio/voice/tyree/tyree_hm.mp3"
        t "What's more is that you take on more than what you can give."
    else:
        call tyree_spaz() from _call_tyree_spaz_16
        call rohan_spaz() from _call_rohan_spaz_28
        call sabie_spaz() from _call_sabie_spaz_55
        t "You don't think enough of others to offer gratitude for when they do offer to help."
        call rohan_spaz() from _call_rohan_spaz_29
        call sabie_spaz() from _call_sabie_spaz_56
        call tyree_spaz() from _call_tyree_spaz_17
        t "When the world gives you its favor, you wallow in self-pity. And when you do not succeed, you bury yourself even deeper."
        call sabie_spaz()
        call tyree_spaz()
        call rohan_spaz()
        voice "audio/voice/tyree/tyree_hm.mp3"
        t "Nothing is ever enough for you and in your cowardice, you will never be satisfied."

    # TODO: Change Tyree's expression to happy and add dialogue to adjust flow, address secrets kept, etc.

    call tyree_spaz() from _call_tyree_spaz_19
    call rohan_spaz() from _call_rohan_spaz_31
    call sabie_spaz() from _call_sabie_spaz_58
    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "Please, I - "
    call sabie_spaz() from _call_sabie_spaz_59
    call tyree_spaz() from _call_tyree_spaz_20
    call rohan_spaz() from _call_rohan_spaz_32
    n "Masami looks desperately around. His arms lock tighter around the trunk."
    call rohan_spaz()
    call tyree_spaz()
    call sabie_spaz()
    voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
    s innocent "If you don't trust us, just say so. At least you're being honest."
    call tyree_spaz() from _call_tyree_spaz_22
    call rohan_spaz() from _call_rohan_spaz_34
    call sabie_spaz() from _call_sabie_spaz_61
    s "Not like whatever shit you're trying to pull with yourself."
    call sabie_spaz() from _call_sabie_spaz_62
    call tyree_spaz() from _call_tyree_spaz_23
    call rohan_spaz() from _call_rohan_spaz_35
    show masami at shake, mc_pos
    m "I - "
    call rohan_spaz() from _call_rohan_spaz_36
    call tyree_spaz() from _call_tyree_spaz_24
    call sabie_spaz() from _call_sabie_spaz_63
    n "In the distance, the school bell rings."
    call sabie_spaz() from _call_sabie_spaz_64
    call tyree_spaz() from _call_tyree_spaz_25
    call rohan_spaz() from _call_rohan_spaz_37
    show masami at shake, mc_pos
    m "I gotta go."
    call tyree_spaz() from _call_tyree_spaz_26
    call rohan_spaz() from _call_rohan_spaz_38
    call sabie_spaz() from _call_sabie_spaz_65
    n "Before any of them can stop him, Masami makes a break for entrance inside."

    jump hallway_1

# Masami runs into Nasir
label hallway_1:

    scene bg black
    hide masami
    with Dissolve(0.5)
    scene bg hallway
    show masami surprised at mc_pos
    with Dissolve(0.5)

    show bg hallway with vpunch
    n "He pushes open the door and tries to lose himself in the crowd."
    n "Behind him, he can hear Sabie's footsteps hot on his heels."
    play sound "audio/sound/footsteps_pound.mp3"
    show bg hallway with vpunch
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Oi, dumbass!"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    s "You can't run from yourself forever!"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    voice "audio/voice/masami/masami_thatsbullshit.mp3"
    m exasperated "(I'm not running from myself. I'm not.)"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    m sad "(I'm just...)"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    m "..."
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m exasperated "(Damn it.)"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    n "Masami quickens his pace, weaving in between the molasses-slow current of people."
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    m sad "(Can't everyone just leave me alone?)"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    m "(Nothing happened, nothing changed.)"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    m exasperated "(So why can't I just - )"
    show bg hallway with vpunch
    play sound "audio/sound/footsteps_pound.mp3"
    n "He turns a corner and brushes a little too hard against an unsuspecting student."
    show bg hallway with vpunch
    show masami surprised at shake, mc_pos
    play sound "audio/sound/crash.mp3"
    m "Ah, sorry - "
    show bg hallway with vpunch

    show nasir surprised at innerright
    call nasir_spaz() from _call_nasir_spaz
    show alyssa nervous at right
    call alyssa_spaz()
    voice "audio/voice/masami/masami_oh.mp3"
    m "Oh."
    call alyssa_spaz() from _call_alyssa_spaz_1
    call nasir_spaz() from _call_nasir_spaz_1
    a sad "Ugh, you again? Got some nerve to show up, huh."
    call nasir_spaz() from _call_nasir_spaz_2
    call alyssa_spaz() from _call_alyssa_spaz_2
    show masami at shake, mc_pos
    m "Alyssa - "
    call alyssa_spaz() from _call_alyssa_spaz_3
    call nasir_spaz() from _call_nasir_spaz_3
    a happy "Oh, I know what you came for now."
    show alyssa at shake, right
    call nasir_spaz() from _call_nasir_spaz_4
    show nasir at center with move
    call alyssa_spaz() from _call_alyssa_spaz_4
    a "Go on, take your boyfriend and be happy. That's what you want, right?"
    call alyssa_spaz() from _call_alyssa_spaz_5
    call nasir_spaz() from _call_nasir_spaz_5
    show masami angry at shake, mc_pos
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "The hell? I never - "
    call nasir_spaz() from _call_nasir_spaz_6
    call alyssa_spaz() from _call_alyssa_spaz_6
    a sad "Spare me. I've had enough of you, cheating scum."
    call alyssa_spaz() from _call_alyssa_spaz_7
    hide alyssa
    call nasir_spaz() from _call_nasir_spaz_7
    show masami surprised at shake, mc_pos
    m "No, Alyssa, please - "
    call nasir_spaz() from _call_nasir_spaz_8
    m sad "I didn't mean - "
    call nasir_spaz()
    voice "audio/voice/nasir/nasir_dontworryaboutme.mp3"
    na sad "It's alright."
    show nasir at center with move
    call nasir_spaz() from _call_nasir_spaz_10
    n "Nasir looks away and also moves to leave, but Masami moves to grab his wrist."
    show bg hallway with vpunch
    show nasir surprised at vpunch, center
    show masami surprised at shake, mc_pos
    m "Wait!"
    call nasir_spaz() from _call_nasir_spaz_11
    na sad "What is it?"
    call nasir_spaz()
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "About last night. I - "
    call nasir_spaz()
    voice "audio/voice/nasir/nasir_quietchuckle.mp3"
    na happy "You don't need to explain. I understand."
    call nasir_spaz() from _call_nasir_spaz_14
    call nasir_spaz() from _call_nasir_spaz_15
    na sad "But perhaps you could have been more honest with yourself."

    if kiss:
        call nasir_spaz() from _call_nasir_spaz_16
        na "You should have pushed me away earlier if you didn't want me."
        call nasir_spaz()
        call nasir_spaz()
        voice "audio/voice/nasir/nasir_quietsigh.mp3"
        na "You shouldn't have kissed me back as if it meant something."

    else:
        # If a cookie was taken
        if take_cookie:
            call nasir_spaz() from _call_nasir_spaz_19
            na "Perhaps I should have known better than to judge from a simple gesture of taking a cookie."
        else:
            call nasir_spaz() from _call_nasir_spaz_20
            na "I should have known when you refused to take a cookie."
            call nasir_spaz()
            voice "audio/voice/nasir/nasir_quietsigh.mp3"
            na "But then, you led me on the whole night with the journey and conversation. And I thought, maybe, we did feel the same way about each other."
            call nasir_spaz() from _call_nasir_spaz_22
            call nasir_spaz() from _call_nasir_spaz_23
            na "Do you know how betrayed I felt when you couldn't do something so simple at the end?"
            call nasir_spaz() from _call_nasir_spaz_24
            na "Is a kiss really too much go give?"

    call nasir_spaz() from _call_nasir_spaz_25
    show masami exasperated at shake, mc_pos
    m "I - I wasn't thinking straight. Neither of us were."
    call nasir_spaz()
    voice "audio/voice/masami/masami_sorryaboutthat.mp3"
    m sad "I'm trying to tell you what I really want now. And that's - "

    if kiss:

        call nasir_spaz() from _call_nasir_spaz_27
        call nasir_spaz() from _call_nasir_spaz_28
        na "What?"
        call nasir_spaz() from _call_nasir_spaz_29
        m neutral "…I think I like you. The same way."
        m sad "I just didn't realize until last night."
        call nasir_spaz()
        call nasir_spaz()
        voice "audio/voice/nasir/nasir_hm.mp3"
        na "Ah."
        call nasir_spaz() from _call_nasir_spaz_32
        show masami angry at shake, mc_pos
        voice "audio/voice/masami/masami_whatthehell.mp3"
        m "That's it? Your only response? Isn't this suppose to be a mutual feeling where we're both supposed to be excited?"
        call nasir_spaz() from _call_nasir_spaz_33
        na "Perhaps."
        call nasir_spaz()
        voice "audio/voice/nasir/nasir_quietchuckle.mp3"
        na "But let me ask you this: if we start something, would you be ready to tell your friends and family about it?"
        call nasir_spaz() from _call_nasir_spaz_35
        call nasir_spaz() from _call_nasir_spaz_36
        na "Even if they would reject you?"
        call nasir_spaz() from _call_nasir_spaz_37
        call nasir_spaz() from _call_nasir_spaz_38
        call nasir_spaz() from _call_nasir_spaz_39
        na "Is that something you could truly ask of yourself when you don’t even have the courage to speak up for your own sister?"
        call nasir_spaz() from _call_nasir_spaz_40
        m sad "..."
        call nasir_spaz()
        call nasir_spaz()
        voice "audio/voice/nasir/nasir_iunderstand.mp3"
        na "That's what I was afraid of."

    else:
        call nasir_spaz()
        call nasir_spaz()
        call nasir_spaz()
        voice "audio/voice/nasir/nasir_iunderstand.mp3"
        na "You've already made yourself clear enough."

    stop music fadeout 1.5
    na "Goodbye Masami."

    call nasir_spaz() from _call_nasir_spaz_46
    hide nasir
    hide glitch_filter onlayer glitching with Dissolve(2.0)

    # GLITCH OFF - Fade out

    n "With that, Nasir twists his arm free and disappears into the outgoing stream of people."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "..."

    jump masami_kitchen_1

# Blackout scene change back to house
label masami_kitchen_1:

    scene bg black
    hide masami
    with Dissolve(1.5)
    pause(1.0)
    scene bg kitchen
    show masami sad at mc_pos
    show wsprite at center
    with Dissolve(1.5)
    play music emotional fadein 1.0

    mm "Hello Masami! Welcome home!"
    m "…"
    mm "Something wrong?"
    voice "audio/voice/masami/masami_im...fine.mp3"
    m neutral "Not really, no."
    n "Masami glances at the stovetop."
    m happy "Making the ginger duck so soon?"
    show wsprite at bounce, center
    n "Masami's mother laughs."
    mm "Well you made a lot of {i}tangyuan{/i}. So I think, why not start making other thing?"
    voice "audio/voice/masami/masami_oh.mp3"
    m neutral "Oh."
    show wsprite at bounce, center
    mm "We can always make more tomorrow {i}tangyuan{/i} to cook tomorrow, don't worry!"
    m "Of course."
    n "She pats him heartily on the back."
    show wsprite at bounce, center
    mm "You excited to eat? Have family time?"
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Yeah. I think so."
    m neutral "That would be nice. I couldn't wish for more than that."
    m sad "(I just such a wish was worth having to begin with.)"

    stop music fadeout 2.0
    scene bg black
    hide masami
    with Dissolve(3.0)

    jump day0_transition
