## DAY 1 - AFTER
# Masami is waiting in the kitchen for his parents to come home
label masami_kitchen1:

    scene bg kitchen with Dissolve(1.0)
    play music emotional fadein 1.0
    show msprite at left
    show wsprite at right
    with Dissolve(1.0)
    pause(0.5)

    # Masami's parents come in
    m "Hey. You're finally back from the damn hospital."
    m "I was beginning to wonder what was taking you so long."
    mm "…"
    m "You don't need to tell me. {i}Jie{/i} is gone, isn't she?"
    n "Masami's mother dabs her eyes with the tissue she's holding, then stares wordlessly at it."
    n "Masami's father shifts beside her. Neither of them attempt to close the door, nor do they move away from it."
    md "We made the choice to let her go."

    stop music fadeout 2.0

    m "..."
    m "I see."

    play music chaos fadein 1.0

    m "Can't say I'm surprised about that."
    m "I already gave the leftover {i}tangyuan{/i} to Sabie. She’s still around so she might as well take it, anyways."
    mm "…"
    md "Masami."
    m "What? I'm just being honest."
    mm "…She would want you to be there when she go. Have her baby brother there one last time."
    m "Sure. Like she even meant to stick around in the first place."
    show wsprite at shake, right
    mm "That is not true! I am her mother. I know her."
    m "Then you knew why she went and graffitied every illegal surface she could find."
    m "Why her bank account always had monthly cash withdrawals."
    m "Why she bought a noise machine to put outside her room."
    m "You knew about all that, right?"
    show wsprite at shake, right
    n "Masami's mother gasps softly, clutching tightly at the tissue."
    show msprite at shake, left
    md "Masami. That is enough for today."
    m "…"
    m "That's bullshit."
    show wsprite at shake, right
    md "Masami! You apologize to your mother - "
    show bg kitchen at hpunch
    m "I said, that's bullshit!"
    show bg kitchen at hpunch
    m "And I am not apologizing!"
    show bg kitchen at hpunch
    m "I'm fucking sick of apologies that don't fix any fucking problems."
    show bg kitchen at hpunch
    m "{i}Jie{/i} was basically dead to everyone the moment she left the house three years ago."
    show bg kitchen at hpunch
    m "No one said a word about her. Not a single fucking word."
    show bg kitchen at hpunch
    m "Not even yesterday before we got the fucking phone call at dinner when we were supposed to be talking about the importance of \"family togetherness\" and shit."
    m "Now - "
    n "Masami swallows."
    show bg kitchen at hpunch
    m "Now, she's actually dead."
    show bg kitchen at hpunch
    m "And everyone still wants to keep dancing around the whole thing like it didn't happen."
    show bg kitchen at hpunch
    m "Is it a crime that I want to actually talk about how fucked up it is that we are erasing a whole member of our family’s existence because she wouldn’t be the fucking doll you wanted her to?"

    stop music fadeout 3.0

    mm "…"
    md "…"

    play music reflective fadein 2.0

    n "Masami sighs."
    m "I - I don't know what else I expected."
    mm "…"
    mm "You changed Masami."
    mm "Why? Why you change?"
    m "…"
    show bg kitchen at shake
    n "Masami abruptly stands from his spot at the dinner table. His chair shakes from where he pushed it aside."
    m "I'm done with this."
    show bg kitchen at hpunch
    n "He turns for the stairs and stalks off to his room, slamming the door behind him."

    jump masami_room1

label masami_room1:

    scene bg black with Dissolve(1.0)
    scene bg bedroom with Dissolve(1.0)

    n "Once inside, he leans against the wooden frame behind him and shuts his eyes."
    n "He can make out his parents' low voices in the kitchen, but he doesn't try to listen in further."
    m "(I…didn't mean to take it out on them like this.)"
    m "(But I'm just so tired of everything. So fucking tired.)"
    m "(Guess you're right, Mom. I really have changed.)"
    n "His gaze drifts across the room to the keychain on his desk."
    m "(How is it that you still want to cling to me so long after you left?)"
    m "(Couldn't you have picked someone else to bother, {i}jie{/i}?)"
    m "(Someone a little less perfect? Someone who didn’t belong? Someone who wasn’t too comfortable where they were at and was willing to vanish away with you?)"
    m "(Maybe you’d have come out of this alive, then.)"
    n "Masami sighs and stares out the window."
    m "(Who am I even kidding anymore?)"
    m "(On nights like this, you never pressured me into going with you. But I still went.)"
    m "(I helped you buy the cans. Disabled the cameras. Watched for the police.)"
    m "(I guess we are on the same on the inside, after all.)"
    m "(But on the outside…)"
    m "(There was a reason you took the fall.)"
    m "(It was so easy for others to point a finger at you, because you never seemed to be \"enough.\")"
    m "(Your grades were good, but not \"good enough\". You spoke, but not \"enough\" to be whatever the hell normal was.)"
    m "(The only thing you did \"enough\" of was smile. But even then, it was to pretend nothing was wrong.)"
    m "(Back then…I did nothing for you. Because it was easier. And I benefited from it.)"
    m "(I was succeeding, so why did I need to change?)"
    n "Masami tilts back his head towards the ceiling and shuts his eyes."
    m "(You knew this, too. Didn't you?)"
    m "(That's why you came back to us with the answer you did.)"
    m "(And my answer in return?)"
    m "(I...)"

    stop music fadeout 2.0

    m "..."

    play music emotional fadein 1.0

    n "Masami's eyes flutter open and he draws in a deep breath."
    m "(Maybe I do have something in mind.)"
    n "He strides over to the window and pushes it open, letting the night air flutter in as he stares into the backyard."
    n "After a moment of hesitation, he eases himself onto the sill and over the edge."
    n "Masami twists around in midair, grabbing the sill with his hands. He hangs there for a moment before lowering himself on the grass with a muffled thump."
    n "He brushes himself off, staring up at the small, dark hole he'd fallen out of."
    m "(Heh. Just like the old days.)"
    m "…"
    m "(I should get going. I don't have much time left.)"

    jump store

# Masami goes to buy some spray paint at the store
label store:

    scene bg black with Dissolve(1.0)
    # TODO: Adjust timing here!

    m "I'd like to check these out, please."
    ca "That's a lot of spray cans and tape, kid. You trying to make a mural or something?"
    m "Something like that, I guess."
    ca "Well, good luck."
    m "…Thanks."
    m "But I don't think I want it."

    jump wall

# Masami goes to spray paint the wall
label wall:

    # SEFF - Probably more driving, but definitely footstep noises
    m "(Well. I guess I'm really am going to do it this time.)"
    m "(With the security cameras rolling.)"
    m "…"
    m "(To hell with it. They can watch me all they want.)"
    m "(Let's see who the problem child is now.)"
    # SEFF - Spray can noises for a bit

    # Scene cut to the wonderful graffiti
    m "(There.)"
    m "(I - )"
    m "(I did it.)"
    m "…"
    m "(I wish I'd listened when you tried to teach me, {i}jie{/i}. Maybe it would have turned out a little nicer.)"
    m "(But I decided to do this my own way.)"
    m "(Because this is my answer to you.)"
    m "..."
    m "(I just hope it’s enough for me.)"

    # Probably have some sort of "glitching" visual effect after this to imply it might be a dream.
    # This effect will pop up throughout the next section as well with "Glitch ON/OFF" comments
    # TODO - Add Xinyi laughter at end as well!

    stop music fadeout 2.0
    scene bg black with Dissolve(2.0)

    jump class_1
