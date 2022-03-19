## DAY 1 - AFTER

label day1_transition:

    call screen day_change(443, "Day 1 - After") with Dissolve(2.0)
    pause(3.0)

    jump masami_kitchen1

# Masami is waiting in the kitchen for his parents to come home
label masami_kitchen1:

    scene bg kitchen
    show masami neutral at mc_pos
    with Dissolve(2.0)
    play music emotional fadein 1.0
    pause(2.0)
    play sound "audio/sound/door_open.mp3"
    show msprite at left
    show wsprite at right
    with Dissolve(1.5)
    pause(1.5)

    # Masami's parents come in
    voice "audio/voice/masami/masami_oh.mp3"
    m "Hey. You're finally back from the damn hospital."
    m "I was beginning to wonder what was taking you so long."
    mm "…"
    m sad "You don't need to tell me. {i}Jie{/i} is gone, isn't she?"
    n "Masami's mother dabs her eyes with the tissue she's holding, then stares wordlessly at it."
    n "Masami's father shifts beside her. Neither of them attempt to close the door, nor do they move away from it."
    md "We made the choice to let her go."

    stop music fadeout 2.0

    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "...I see."

    play music chaos fadein 1.0

    m neutral "Can't say I'm surprised about that."
    m "I already gave the leftover {i}tangyuan{/i} to Sabie. She’s still around so she might as well take it, anyways."
    mm "…"
    md "Masami."
    m sad "What? I'm just being honest."
    mm "…She would want you to be there when she go. Have her baby brother there one last time."
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "Sure. Like she even meant to stick around in the first place."
    mm "That is not true! I am her mother. I know her."
    m sad "Then you knew why she went and graffitied every illegal surface she could find."
    m "Why her bank account always had monthly cash withdrawals."
    m "Why she bought a noise machine to put outside her room."
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "You knew about all that, right?"
    show wsprite at shake, right
    n "Masami's mother gasps softly, clutching tightly at the tissue."
    show msprite at shake, left
    md "Masami. That is enough for today."
    m sad "…"
    voice "audio/voice/masami/masami_thatsbullshit.mp3"
    m exasperated "That's bullshit."
    show wsprite at shake, right
    md "Masami! You apologize to your mother - "
    show bg kitchen at hpunch
    show masami at hpunch, mc_pos
    m angry "I said, that's bullshit!"
    show bg kitchen at hpunch
    show masami at hpunch, mc_pos
    m "And I am not apologizing!"
    show bg kitchen at hpunch
    show masami exasperated at hpunch, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "I'm fucking sick of apologies that don't fix any fucking problems."
    m "{i}Jie{/i} was basically dead to everyone the moment she left the house three years ago."
    m "No one said a word about her."
    show bg kitchen at hpunch
    show masami angry at hpunch, mc_pos
    m "Not a single fucking word."
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m "Not even yesterday before we got the fucking phone call at dinner when we were supposed to be talking about the importance of \"family togetherness\" and shit."
    m "Now - "
    show masami sad
    n "Masami swallows."
    m "Now, she's actually dead."
    show bg kitchen at hpunch
    show masami angry at hpunch, mc_pos
    m "And everyone still wants to keep dancing around the whole thing like it didn't happen."
    m "Is it a crime that I want to actually talk about how fucked up it is that we are erasing a whole member of our family’s existence because she wouldn’t be the fucking doll you wanted her to?"

    stop music fadeout 3.0

    mm "…"
    md "…"

    play music reflective fadein 3.0

    show masami exasperated
    voice "audio/voice/masami/masami_quietsigh.mp3"
    n "Masami sighs."
    m "I - I don't know what else I expected."
    mm "…"
    mm "You changed Masami."
    mm "Why? Why you change?"
    m sad "…"
    show bg kitchen at shake
    show masami at shake, mc_pos
    n "Masami abruptly stands from his spot at the dinner table. His chair shakes from where he pushed it aside."
    voice "audio/voice/masami/masami_whatever.mp3"
    m "I'm done with this."
    show bg kitchen at hpunch
    show masami at hpunch, mc_pos
    play sound "audio/sound/door_slam.mp3"
    n "He turns for the stairs and stalks off to his room, slamming the door behind him."

    jump masami_room1

label masami_room1:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg bedroomnight
    show masami sad at mc_pos
    with Dissolve(1.0)

    n "Once inside, he leans against the wooden frame behind him."
    n "He can make out his parents' low voices in the kitchen, but he doesn't try to listen in further."
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "(I…didn't mean to take it out on them like this.)"
    m exasperated "(But I'm just so tired of everything. So fucking tired.)"
    m neutral "(Maybe you're right, Mom. Maybe I really have changed.)"
    n "His gaze drifts across the room to the keychain on his desk."
    voice "audio/voice/masami/masami_hm.mp3"
    m sad "(How is it that you still want to cling to me so long after you left?)"
    m "(Couldn't you have picked someone else to bother, {i}jie{/i}?)"
    m "(Someone a little less perfect? Someone who didn’t belong? Someone who wasn’t too comfortable where they were at and was willing to vanish away with you?)"
    m "(Maybe you’d have come out of this alive, then.)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    n "Masami sighs and stares out the window."
    show masami exasperated at shake, mc_pos
    m "(Who am I even kidding anymore?)"
    m sad "(On nights like this, you never pressured me into going with you. But I still went.)"
    m "(I helped you buy the cans. Disabled the cameras. Watched for the police.)"
    m neutral "(I guess we are on the same on the inside, after all.)"
    m sad "(But on the outside…)"
    voice "audio/voice/masami/masami_jie.mp3"
    m "(There was a reason you took the fall.)"
    m exasperated "(It was so easy for others to point a finger at you, because you never seemed to be \"enough.\")"
    m "(Your grades were good, but not \"good enough\". You spoke, but not \"enough\" to be whatever the hell normal was.)"
    m sad "(The only thing you did \"enough\" of was smile. But even then, it was to pretend nothing was wrong.)"
    m "(Back then…I did nothing for you. Because it was easier. And I benefited from it.)"
    m "(I was succeeding, so why did I need to change?)"
    n "Masami tilts back his head towards the ceiling and shuts his eyes."
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "(You knew this, too. Didn't you?)"
    m sad "(That's why you came back to us with the answer you did.)"
    m "(And my answer in return?)"
    m "(I...)"

    stop music fadeout 2.0

    m exasperated "..."

    play music emotional fadein 3.0

    show masami sad
    voice "audio/voice/masami/masami_quietsigh.mp3"
    n "Masami's eyes flutter open and he draws in a deep breath."
    m neutral "(Maybe I do have something in mind.)"
    n "He strides over to the window and pushes it open, letting the night air flutter in as he stares into the backyard."
    n "After a moment of hesitation, he eases himself onto the sill and over the edge."
    play sound "audio/sound/thud.mp3"
    n "Masami twists around in midair, grabbing the sill with his hands. He hangs there for a moment before lowering himself on the grass with a muffled thump."
    n "He brushes himself off, staring up at the small, dark hole he'd fallen out of."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "(Heh. Just like the old days.)"
    m sad "…"
    m "(I should get going. I don't have much time left.)"

    jump store

# Masami goes to buy some spray paint at the store
label store:

    scene bg black
    hide masami
    with Dissolve(2.0)
    pause(1.0)

    play sound "audio/sound/footsteps_walk2.mp3"
    pause(3.0)

    m "I'd like to check these out, please."
    play sound "audio/sound/set_down.mp3"
    queue sound "audio/sound/slide.mp3"
    ca "That's a lot of cans and markers, kid. You trying to make a mural or something?"
    voice "audio/voice/masami/masami_hm.mp3"
    m "Something like that, I guess."
    play sound "audio/sound/cash_register.mp3"
    ca "Well, good luck."
    m "…Thanks."
    m "But I don't think I want it."

    jump wall

# Masami goes to spray paint the wall
label wall:

    pause(2.0)
    scene bg wall
    with Dissolve(2.0)
    pause(0.7)
    play sound "audio/sound/footsteps_walk1.mp3"
    show masami at mc_pos
    with Dissolve(1.5)
    pause(1.5)
    m "(Well. I guess I'm really am going to do it this time.)"
    m "(With the security cameras rolling.)"
    m sad "…"
    voice "audio/voice/masami/masami_whatever.mp3"
    m exasperated "(To hell with it. They can watch me all they want.)"
    m angry "(Let's see who the problem child is now.)"

    scene bg black
    hide masami
    with Dissolve(2.0)
    pause(1.0)

    play sound "audio/sound/spray_shake.mp3"
    pause(1.5)
    queue sound "audio/sound/spray_long.mp3"
    queue sound "audio/sound/spray_long.mp3"
    queue sound "audio/sound/spray_short.mp3"
    queue sound "audio/sound/spray_short.mp3"
    queue sound "audio/sound/spray_long.mp3"
    queue sound "audio/sound/marker_shake.mp3"
    queue sound "audio/sound/marker_long.mp3" volume 0.1
    queue sound "audio/sound/marker_normal.mp3" volume 0.1
    queue sound "audio/sound/marker_quick.mp3" volume 0.1
    queue sound "audio/sound/marker_quick.mp3" volume 0.1
    queue sound "audio/sound/marker_long.mp3" volume 0.1

    pause

    scene bg graffitizoom with Dissolve(2.0)
    pause
    scene bg graffiti
    show masami at mc_pos
    with Dissolve(2.0)

    # Scene cut to the wonderful graffiti
    m "(There.)"
    m sad "(I - )"
    m neutral "(I did it.)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "…"
    m neutral "(I wish I'd listened when you tried to teach me, {i}jie{/i}. Maybe it would have turned out a little nicer.)"
    m "(But I decided to do this my own way.)"
    m "(Because this is my answer to you.)"
    m sad "..."
    m "(I just hope it’s enough for me.)"

    # Probably have some sort of "glitching" visual effect after this to imply it might be a dream.
    # This effect will pop up throughout the next section as well with "Glitch ON/OFF" comments
    # TODO - Add Xinyi laughter at end as well!

    stop music fadeout 2.0
    scene bg black
    hide masami
    with Dissolve(3.0)

    jump day_1_transition
