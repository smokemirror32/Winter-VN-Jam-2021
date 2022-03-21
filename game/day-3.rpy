﻿## DAY 3 - BEFORE

label day_3_transition:

    call screen day_change(5, 5, "Day 3 - Before") with Dissolve(2.0)
    pause(3.0)

    jump class_3

label class_3:

    play music lighthearted fadein 1.0
    scene bg hallway with Dissolve(2.0)
    show masami at mc_pos with Dissolve(1.0)

    m "Thanks, Mr. Friedman! Happy holidays to you, too!"
    n "Masami steps out of the classroom, joining the sea of students heading to lunch."
    voice "audio/voice/masami/masami_hm.mp3"
    m sad "(Phew. That last bit on LR circuits was rough. I'll probably have to review over break.)"
    m neutral "(At least the material is kinda interesting.)"
    m "(Unlike chemistry, which is just watered down physics.)"
    m "(Math with memorization.)"
    m "(The only thing it's good for is making reactions pretty enough for you to forget how boring it is.)"
    show masami sad
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m neutral "(Still got two more classes of it to go. Two more days. I can make it.)"
    m sad "(...Probably.)"
    m neutral "(Heh. Times like this make it really easy for me to understand why {i}jie{/i} - )"
    show masami exasperated at shake, mc_pos
    n "He freezes suddenly mid-thought and gives his head a quick shake."
    voice "audio/voice/masami/masami_jie.mp3"
    m sad "…"
    m "(After three years, I should be better with this.)"
    m exasperated "(Focus, Masami. Focus.)"
    n "He rubs his temples."
    m sad "(What was I supposed to be doing again?)"
    m neutral "(...Oh, right. Lunch. I'm headed to lunch.)"
    play sound "audio/sound/phone_vibrate.mp3"
    n "Just then, Masami's phone buzzes in his pocket."
    voice "audio/voice/masami/masami_oh.mp3"
    m "(Ah, that's probably Sabie.)"
    n "He pulls it out and unlocks it."
    m "(Yup, it's her.)"
    m "(...Wonder what she wants this time.)"

    jump phone_3a

# This is a series of text messages between Sabie and Masami
label phone_3a:

    hide masami with Dissolve(0.5)

    call phone_open(True) from _call_phone_open_10

    call message(s, "yo", True) from _call_message_168
    call message(s, "yo") from _call_message_169
    call message(s, "yooo") from _call_message_170
    call message(s,"{i}ge{/i}") from _call_message_171
    call message(s, "r u there") from _call_message_172
    call message(s, "...") from _call_message_173
    call message(s, "{i}ge geeeeeee{/i}") from _call_message_174
    call message(s, "u r not ignoring me right") from _call_message_175
    call message(s, ":(((((") from _call_message_176
    call message(m, "Hey", True) from _call_message_177
    call message(s, ":o", True) from _call_message_178
    call message(s, "ur here") from _call_message_179
    call message(s, ":D") from _call_message_180
    call message(m, "Ye", True) from _call_message_181
    call message(m, "Sorry, just got out of class") from _call_message_182
    call message(s, "tis ok ^.^", True) from _call_message_183
    call message(s, "we r outside at usual spot") from _call_message_184
    call message(s, "dont take too long or rohan will niwnag;awngawn") from _call_message_185
    call message(s, "nae;iwngliane;li;ngial") from _call_message_186
    call message(s, "I;eangioaen;oein;ioeanwi") from _call_message_187
    call message(s, "ianewgilnewa") from _call_message_188
    call message(m, "?", True) from _call_message_189
    call message(s, "naigneianeiawne;", True) from _call_message_190
    call message(s, "wia;eiai") from _call_message_191
    call message(s, "eaaijeianwl") from _call_message_192
    call message(m, "...", True) from _call_message_193
    call message(s, "sry he took my phone again :(", True) from _call_message_194
    call message(m, "Okay. You deserved it.", True) from _call_message_195
    call message(s, "hey >:(", True) from _call_message_196
    call message(s, "rude") from _call_message_197
    call message(m, ":)", True) from _call_message_198
    call message(s, "fine then dont come", True) from _call_message_199
    call message(s, "i dont need u to bully me") from _call_message_200
    call message(m, "Someone needs to bully you", True) from _call_message_201
    call message(s, ">:(", True) from _call_message_202
    call message(m, ":)", True) from _call_message_203
    call message(s, "meanie", True) from _call_message_204
    call message(s, "i hate u") from _call_message_205
    call message(s, "leave me alone") from _call_message_206
    call message(m, "Okay bye", True) from _call_message_207

    call phone_close() from _call_phone_close_10

    jump hallway_3

# Return back to the hallway scene
label hallway_3:

    show masami at mc_pos with Dissolve(0.5)

    n "Masami slips the phone back into his pocket."
    play sound "audio/sound/phone_vibrate.mp3"
    queue sound "audio/sound/phone_vibrate.mp3"
    n "It vibrates plaintively against his hip."
    n "He just shakes his head and smiles a little to himself."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "(Heh. Idiots.)"
    n "He continues down the hallway at his usual leisurely pace."
    m neutral "(They'll manage.)"
    m "(...Probably.)"

    jump lunch_chaos

# Scene change to the lunch spot
label lunch_chaos:

    hide masami
    scene bg black
    with Dissolve(1.0)
    scene bg courtyard
    show masami at mc_pos
    with Dissolve(1.0)
    play music uptempo fadein 1.0 fadeout 1.0


    n "As per usual, Masami hears the chaos long before he sees it."
    voice "audio/voice/rohan/rohan_seriously.mp3"
    r "Hey, let go of my phone!"
    s "But you gotta share those pictures we took in the group chat."
    r "Uh, those were supposed to be private. Just for me!"
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "That's not what you said yesterday."
    r "I-I take what I said back!"
    s "Too late, buddy. You gotta learn to - ah!"
    play sound "audio/sound/phone_vibrate.mp3" loop
    n "As if on cue, Masami's own phone, which had been silent for some time, starts buzzing again."
    m "(I should probably hurry up.)"
    stop sound fadeout 3.0
    n "Masami quickens his pace to a light jog as he heads down the courtyard path."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "(Of all the places they could sit, they still chose the spot farthest from the door.)"

    show rohan annoyed at right
    show sabie mischievous at left
    with Dissolve(0.5)

    n "As he gets closer, he can see Rohan and Sabie kneeling on top of the only occupied table in the yard, fighting for possession over what is apparently Rohan's phone."

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    n "From the seat at a nearby bench, Tyree watches with mild amusement as he eats his kale salad."
    n "He gives Masami a slight nod."
    voice "audio/voice/tyree/tyree_ah.mp3"
    t "Hey."
    m "Hey, Tyree."

    hide tyree
    show rohan annoyed at right
    show sabie mischievous at left
    with Dissolve(0.1)

    n "At the sound of Masami's voice, Rohan's head whips around."
    r "What?"
    voice "audio/voice/rohan/rohan_oh.mp3"
    r neutral "Oh! Hi!"

    show rohan at shake, right

    n "He gives the phone a tug. Sabie doesn't budge."
    r happy "I, uh. Need a little help here?"
    n "Sabie swats at his hand. Rohan yelps."

    show rohan annoyed at bounce

    r "Hey, what was that for?"
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s happy "That. Would be cheating."
    s innocent "Besties only help besties."
    s mischievous "Right, {i}ge{/i}?"
    n "Sabie winks at Masami."
    voice "audio/voice/rohan/rohan_w-what.mp3"
    r sad "Hey! I thought we were besties."

    show sabie annoyed at shake, left

    s "Well, not after you sent those drunk karaoke clips of me in the chat."

    show rohan annoyed at shake, right

    r "But that was because you posted those shots you took of me in the mall!"

    show sabie neutral

    n "Sabie shrugs."
    voice "audio/voice/sabie/sabie_imean.mp3"
    s happy "It's not a big deal. You looked good. And they already knew all about your little schtick."
    r embarrassed "…"
    s mischievous "Besides…weren't you the one who said you wanted everyone to get more comfy with {i}that{/i} side of yourself?"
    r "I - "
    voice "audio/voice/rohan/rohan_defeatedsigh.mp3"
    r sad "…"

    show sabie innocent at bounce

    s "Don’t be shy. I know you, theater butterfly."
    r embarrassed "I-I never said - "
    voice "audio/voice/sabie/sabie_suckstosuck.mp3"
    s mischievous "Sucks to suck ‘cuz you know I'm right."
    r "I - "
    r sad "Ugh. Fine."

    show rohan annoyed at shake, right

    r "But that doesn't give you the right to send the rest of the - "
    s surprised "Wait. You've got more pictures?"
    voice "audio/voice/rohan/rohan_n-no.mp3"
    r embarrassed "What? No, I didn't mean - "

    show sabie mischievous at center with move
    show sabie at bounce

    voice "audio/voice/sabie/sabie_heh.mp3"
    s "Ooh, now this is something I have to see!"
    r "Sabie, no!"

    show sabie at left
    show rohan at center
    with move
    show sabie at shake,left

    n "Sabie makes another desperate, backwards yank at Rohan's phone."

    hide sabie
    hide rohan
    with easeoutleft
    show bg courtyard behind rohan, sabie at hpunch

    play sound "audio/sound/crash.mp3"
    n "Rohan holds on for dear life as the momentum sends them both flying onto the ground, where they continue to wrestle for control."
    n "Or at least, Rohan is struggling, while Sabie bats lightly at his limbs, clearly toying with him."
    n "Masami takes a cautious step forward."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Um - "

    show rohan embarrassed at center, shake with Dissolve(0.1)

    voice "audio/voice/rohan/rohan_um.mp3"
    r "Masami, do something! Don't let her - ah!"

    show rohan at right with move
    show sabie mischievous at shake, center with Dissolve(0.1)

    n "Rohan yelps again as Sabie's elbow brushes roughly against his cheek."
    voice "audio/voice/sabie/sabie_well.mp3"
    s happy "Oh, please. You know you're going to be thanking me later."

    show sabie mischievous at shake

    s mischievous "And, {i}ge{/i}? If anything, you should be helping - me!"

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    voice "audio/voice/tyree/tyree_heh.mp3"
    t "Or you could just watch them."

    show rohan annoyed at shake, right
    show sabie annoyed at center
    hide tyree

    voice "audio/voice/rohan/rohan_seriously.mp3"
    r "What?"

    show sabie at shake, center

    s "Hey!"

    hide rohan
    hide sabie
    show tyree happy at center, bounce
    with Dissolve(0.1)

    voice "audio/voice/tyree/tyree_quietchuckle.mp3"
    t "It's free entertainment."

    show rohan annoyed at shake, right
    show sabie annoyed at shake, center
    hide tyree

    n "Sabie sticks her tongue out at Tyree."
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s "Ugh. So rude."
    r sad "For once, I agree with her."

    show rohan neutral

    s happy "Aw thanks, Rohan. I appreciate it."
    s annoyed "But also. Rude."
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "(Hm…)"

# Masami decides what to do
menu:

    "Side with Sabie":
        $ support = "Sabie"
        jump lunch_chaos_sabie
    "Side with Rohan":
        $ support = "Rohan"
        jump lunch_chaos_rohan
    "Join Tyree in watching them both suffer":
        $ support = "Tyree"
        jump lunch_chaos_tyree

# If Masami decides to help Sabie
label lunch_chaos_sabie:

    m "I'm actually with Sabie for once."

    show rohan sad

    voice "audio/voice/rohan/rohan_hmph.mp3"
    n "Rohan's expression instantly deflates."

    show sabie happy at bounce

    n "In the meantime, Sabie does a fist pump."
    voice "audio/voice/sabie/sabie_gotcha.mp3"
    s "Aha, yes! Someone understands where I'm coming from."
    show masami exasperated
    n "Masami gives her a pointed look."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "I'm not finished."
    s surprised "Oop."
    m "And I'm not letting you have control over Rohan's phone."
    m sad "(Not going to make that mistake again after the flood of deep fried memes last time.)"
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s annoyed "Aw, dammit."
    voice "audio/voice/masami/masami_sorryaboutthat.mp3"
    m neutral "Anyways, as I was saying, it helps to open up to people about stuff like this."
    m happy "Helps you accept yourself, too."
    m neutral "I'm not going to force you to share, but I still think it would be good to."

    show rohan neutral
    show sabie neutral

    n "Rohan's shoulders relax the slightest bit."
    voice "audio/voice/rohan/rohan_um.mp3"
    r sad "Yeah. I get that. But…"

    show sabie worried

    n "His voice trails off as he looks away."
    m "If you're worried about rejection, we already promised we wouldn't judge you for it, didn't we?"

    hide sabie
    hide rohan
    show tyree

    voice "audio/voice/tyree/tyree_yes.mp3"
    t "Agreed."

    show sabie at center
    show rohan at right
    hide tyree

    n "After a moment of hesitation, Rohan nods."
    voice "audio/voice/rohan/rohan_iguess.mp3"
    r "Okay. I'll think about it."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Cool. Er, Sabie?"
    s "Yeah?"
    m neutral "Could you let go of his phone?"
    n "Sabie blinks at him uncomprehendingly for a moment before she realizes her hands are still clamped down tight around it."

    show sabie surprised at shake, center

    s "Oh."

    show sabie at left with move

    voice "audio/voice/sabie/sabie_fine.mp3"
    n "She obediently lets go. The moment she does, Rohan quickly tucks it away, eyeing her with a healthy amount of distrust."
    n "Masami sighs in relief."
    m "(That was easier to take care of than usual.)"

    jump lunch_stable

# If Masami decides to help Rohan
label lunch_chaos_rohan:

    m exasperated "Sabie. Let go of his phone."
    s surprised "But - "
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "Now. Or I'll make you do it myself."

    show sabie annoyed at shake, center

    voice "audio/voice/sabie/sabie_fine.mp3"
    s annoyed "Ugh. Fine. Spoilsport."

    show sabie at left with move

    n "Sabie sticks out her tongue at him, but grudgingly complies."
    n "The moment she lets go, Rohan snatches up his phone and stuffs it hastily into his pocket."
    voice "audio/voice/rohan/rohan_oh.mp3"
    r happy "Phew. Thanks."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m neutral "Don't mention it."
    m sad "(It would be good for Rohan to get some confidence from sharing those photos, but I don't want to force him to do anything he's not comfortable with.)"

    jump lunch_stable

# If Masami decides to watch them both suffer
label lunch_chaos_tyree:

    m happy "I wash my hands of this."

    show rohan at shake, right

    voice "audio/voice/rohan/rohan_w-what.mp3"
    r embarrassed "What? You can't just - "
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s mischievous "Ohoho, you heard him. This one's between you and me, string bean."

    show rohan at shake, right

    r annoyed "Urgh…"
    r "If that's what it's going to be, I am not going to let you have my phone."

    show sabie at bounce, center

    s innocent "Bet!"

    hide rohan
    hide sabie
    show tyree

    n "Tyree catches Masami's eye."

    t "Who do you think is going to win?"
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "Hm, tough one, but I'm going with Sabie."
    m "(After all, there's only so much you can do against someone on the wrestling team. Even if they're only on JV.)"

    show tyree happy at bounce

    voice "audio/voice/tyree/tyree_ah.mp3"
    t "Same."

    show sabie at center
    show rohan sad at right
    hide tyree

    voice "audio/voice/rohan/rohan_seriously.mp3"
    r "Thanks for the vote of confidence."
    m happy "Sorry, Rohan, but I'm afraid I have to take into account prior experience."
    voice "audio/voice/sabie/sabie_heh.mp3"
    s mischievous "As you should. Those noodle arms got nothing on these guns."


    show rohan annoyed at shake, right

    r "H-Hey! This time will be different."
    s happy "Sure. That's what you said last time."

    hide rohan
    hide sabie
    show tyree

    voice "audio/voice/tyree/tyree_hm.mp3"
    t "Change your mind, Masami?"
    m neutral "Nope."
    t "Good."

    hide tyree
    show sabie mischievous
    show rohan annoyed at right

    s "Hehe. Good choice."

    show rohan at shake, right
    show sabie at shake, center
    show bg courtyard behind rohan, sabie at hpunch
    pause(0.5)
    show rohan sad
    show sabie at left with move

    n "As expected, it isn't even a minute before Sabie wrests control of the device away from him."
    voice "audio/voice/rohan/rohan_igiveup.mp3"
    n "Rohan lies spread eagle on the ground in defeat."

    show sabie happy at bounce, left

    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Ehe."
    s mischievous "Now, let's see…"
    play sound "audio/sound/phone_vibrate.mp3"
    s surprised "Dammit. You changed the passcode again."

    show rohan happy

    n "Rohan's eyes glint back at her in triumph."
    voice "audio/voice/rohan/rohan_nervouslaughter.mp3"
    r happy "Heh."
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s annoyed "Ugh. Maybe it’s the one from last week? Nope. Or the week before that? Nope again…"
    play sound "audio/sound/phone_vibrate.mp3"
    queue sound "audio/sound/phone_vibrate.mp3"
    queue sound "audio/sound/phone_vibrate.mp3"
    n "Sabie proceeds to check a flurry of combinations. After a couple of minutes, she stops."

    show sabie innocent at bounce, left

    s "Rohan, bestie, can you please - "
    r neutral "Nope."
    s worried "But - "

    show rohan happy at bounce, right

    voice "audio/voice/rohan/rohan_hey.mp3"
    r "Sucks to suck."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Well. Why am I not surprised?"

    show sabie annoyed at shake, left

    voice "audio/voice/sabie/sabie_hmmmm.mp3"
    s annoyed "Hey! What did I do to deserve that attitude from you?"

    hide rohan
    hide sabie
    show tyree

    voice "audio/voice/tyree/tyree_yes.mp3"
    t "Everything."

    show sabie annoyed at left
    show rohan at right
    hide tyree

    s "Rude. I was not asking for your opinion."
    m neutral "I mean, he does have a point. This is a weekly occurrence."
    voice "audio/voice/rohan/rohan_um.mp3"
    r happy "Yeah. And now we're at the part where you give me my phone back?"
    n "Sabie purses her lips as her gaze bounces between Masami, Tyree, and Rohan."

    show sabie at shake, left

    voice "audio/voice/sabie/sabie_fine.mp3"
    s "Ugh. Fine. Thought I'd get lucky for once, but whatever."
    s "Guess I have no choice when everyone decides to gang up on me like that."

    show rohan neutral

    n "She grudgingly hands Rohan's phone back to him."
    n "For his part, Rohan tucks the phone quickly into his pocket, eyeing Sabie with a healthy amount of distrust."
    n "Masami smiles quietly to himself."
    m happy "(Some things never get old, do they?)"

    jump lunch_stable

# Return to civil discussion
label lunch_stable:

    show masami neutral
    show sabie neutral at center
    show rohan neutral at right behind sabie
    with move

    n "Rohan and Sabie move back to sit at the table like proper civilized human beings."

    show tyree at left behind sabie with moveinleft

    play sound "audio/sound/set_down.mp3"
    n "Tyree picks up his things to join them and Masami follows suit."
    n "Once they've all gathered, Sabie rubs her hands together."

    show sabie happy at bounce

    s happy "So. How's everyone doing?"
    voice "audio/voice/rohan/rohan_um.mp3"
    r sad "Why this question all of a sudden? Can we, you know, talk about the usual stuff? Like gaming?"

    show sabie neutral

    n "Sabie shrugs."
    voice "audio/voice/sabie/sabie_well.mp3"
    s "We could."
    s mischievous "But I also kind of want to check in since {i}some{/i} people don't share their feelings unless they're asked to."

    show sabie happy at bounce

    s "So. How about it?"
    r embarrassed "Uh…"

    show tyree at bounce, left

    voice "audio/voice/tyree/tyree_ah.mp3"
    t "I'm doing fine."
    show masami happy at bounce, mc_pos
    m "Same."

    show rohan at bounce, right

    r neutral "What they said."

    show sabie annoyed at shake

    voice "audio/voice/sabie/sabie_uh.mp3"
    s "That's not what I meant. And you know that."
    n "Tyree shrugs."
    t "I answered your question."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m neutral "He's not wrong."
    n "Sabie rolls her eyes dramatically."
    s innocent "Oh, my bad. It seems that I did. Let me specify."
    show sabie at bounce
    s "Are your classes less sucky than usual?"
    show sabie at bounce
    s "Are you saying your prayers so that your sad grades will get you into the Ivy League of your dreams?"
    show sabie at bounce
    s "Are your extracurricular overcommitments getting you down?"
    show sabie at bounce
    s "Are you counting down the days to Christmas carousing?"
    show sabie at bounce
    s "Are you holding on to the promise {i}Dongzhi{/i} binge-eating with the fam like it's a lifeline from above?"
    show sabie at bounce
    s "Are you - "
    n "She stops when she sees Rohan raising his hand."
    s neutral "Yeah?"
    voice "audio/voice/rohan/rohan_um.mp3"
    r "Question. What's {i}Dongzhi{/i}?"
    t "It's an East Asian holiday held on the winter solstice that comprises of reuniting with family and eating {i}tangyuan{/i}."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "(...And the assumption that you have a complete family to spend it with.)"
    show sabie at bounce
    s "Basically Thanksgiving with a better menu. Fun stuff!"
    voice "audio/voice/sabie/sabie_hmmmm.mp3"
    s worried "Anyways, let's see, what else do I need to ask you emotionally constipated children to help you open up properly?"
    show sabie innocent at bounce
    s "Oh yeah! Are you - "
    voice "audio/voice/rohan/rohan_hmph.mp3"
    r sad "Um, I think we get the point."
    s mischievous "Great!"
    n "She puts her elbows on the table, hands resting in her open palms as she leans forward."
    show sabie at bounce
    s "So. Got an answer?"
    show rohan at shake, right
    r embarrassed "Uh - "

    show rohan neutral

    voice "audio/voice/tyree/tyree_hm.mp3"
    t "I can go."
    s happy "Okay, let's hear it."

    jump lunch_stable_tyree

# Tyree's turn
label lunch_stable_tyree:

    show tyree at bounce, left
    t happy "My classes and grades are fine. My extracurriculars are going well. I am looking forward to going on break."
    s annoyed "..."
    m neutral "..."
    show rohan at bounce, right
    voice "audio/voice/rohan/rohan_pft.mp3"
    r happy "Pft."
    voice "audio/voice/sabie/sabie_well.mp3"
    s worried "That was kind of vague."
    t worried "I'm not sure what else you want me to say."
    s "Uh, anything on recruiting for swimming, robotics co-captaining for build season? Stuff like that?"
    voice "audio/voice/tyree/tyree_oh.mp3"
    t neutral "Several schools seem interested in having me. Build season is going well."
    voice "audio/voice/rohan/rohan_defeatedsigh.mp3"
    r sad "He means that MIT and Stanford have already talked about wanting to sign him on and that the robotics team is on track to go to Worlds again this year."
    r "And that he's passed his HSK 3 exam for Chinese last month."

    show sabie surprised at shake
    n "Sabie stands up from her seat and plants her hands on the table."
    s "Wait, what the hell? That's a shit ton. Why didn't you say anything?"
    voice "audio/voice/tyree/tyree_hm.mp3"
    t worried "I thought it wasn't necessary to bring up."
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s annoyed "Well, that's exactly what I wanted you to bring up! Friends always celebrate each other's wins right?"
    t neutral "Um. Sure."
    s neutral "Now that's the spirit!"
    n "Sabie then whirls on Rohan."

    show sabie annoyed at shake

    s "And you, how did you know about this anyways when this kid over here won't open his mouth?"
    show rohan happy at bounce, right
    voice "audio/voice/rohan/rohan_hey.mp3"
    r happy "Uh, my parents?"
    show sabie happy at bounce
    s happy "Oh, right. Sorry I asked."
    voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
    s "Your parents are crazy. I don't know how they find the stuff they do."
    show rohan happy at bounce, right
    r "To be honest, me neither."
    voice "audio/voice/rohan/rohan_igiveup.mp3"
    r "It's okay though. I'm kinda numb to it at this point."

    jump lunch_stable_rohan

label lunch_stable_rohan:

    show sabie happy at bounce
    s "I felt that."
    s mischievous "Anyways, how are you? Wanna tell us about your life?"
    show rohan embarrassed at shake, right
    r "Dammit. I was hoping you'd forget."
    voice "audio/voice/sabie/sabie_heh.mp3"
    s "Not a chance. So, what do you have to say for yourself?"
    voice "audio/voice/rohan/rohan_um.mp3"
    r neutral "Uh, my grades are probably good enough for me to go to the state university for medical school and my classes are kinda interesting?"
    r sad "...All of them except for the STEM ones at least. I hate bio."
    r neutral "Most of my clubs have wound down for the year. We had a full house for our productions all last week, so that was nice."
    r sad "I still haven't done anything for Science Olympiad, though. Or HOSA. Or the Intel Research competition. I need to get on that."
    r neutral "Anyways, I am definitely very tired and looking forward to break."
    n "Rohan gives Sabie a nervous look."
    voice "audio/voice/rohan/rohan_nervouslaughter.mp3"
    r "That was it, right? I didn't miss anything, did I?"
    show sabie neutral at bounce
    s "That. Was perfect. Exactly what I was looking for."
    n "Sabie points in Tyree's direction."
    show sabie mischievous at bounce
    s "You. Take note when I ask you next time."
    voice "audio/voice/tyree/tyree_yes.mp3"
    t "Okay."

    jump lunch_stable_masami

label lunch_stable_masami:

    s happy "Now, last one."
    voice "audio/voice/sabie/sabie_uh.mp3"
    s worried "..."
    show sabie at bounce
    s "Hey, Masami? You still there?"
    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "Huh?"
    n "Masami blinks and looks up. Everyone at the table is now staring at him."
    m exasperated "(Shit. How long have I zoned out for?)"
    show sabie at bounce
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s neutral "It's your turn for a group progress update."
    voice "audio/voice/masami/masami_oh.mp3"
    m sad "Oh."
    n "Masami stares at his hands, a lump forming in his throat."
    m exasperated "(Dammit.)"
    voice "audio/voice/masami/masami_hm.mp3"
    m sad "(Usually I wouldn't struggle with this sort of thing.)"
    m "(But these past few days all I can think about is {i}jie{/i} and what she promised - )"
    m exasperated "(No. I have to focus. I can't think about that now.)"
    show masami neutral
    n "Masami looks up again and forces himself to smile, easing his shoulders into a more natural position."
    n "His fingers instinctively fish for a small object in his pocket, latching on tight when they find it."
    show masami happy at bounce, mc_pos
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "Well, you guys have already heard most of it before. Robotics pre-season is going well. So is theatre. And badminton, though I’m not getting recruited for that."
    show masami happy at bounce, mc_pos
    m "Grades and classes are pretty good, though break is also nice."
    m "I…don't really have anything to complain about."
    voice "audio/voice/masami/masami_whatever.mp3"
    m sad "(At least, anything that's acceptable for me to say, that is.)"
    show masami neutral
    show rohan at bounce, right
    voice "audio/voice/rohan/rohan_hey.mp3"
    r "Sounds like things are going as well as always for you then."
    show tyree at bounce, left
    voice "audio/voice/tyree/tyree_ah.mp3"
    t "That's good."
    voice "audio/voice/sabie/sabie_uh.mp3"
    s worried "Yeah, I suppose."
    n "Sabie stares at Masami for a moment longer, as she usually does when she's trying to fish the hesitancy out of him."
    show masami sad
    n "Masami's grip tightens on the object in his pocket."
    m exasperated "(Shit. She noticed. What now?)"
    s "What about - "
    play sound "audio/sound/bell_normal.mp3"
    n "Just then the bell rings, cutting her off."
    m neutral "(Phew.)"
    m "Looks like that's our cue to leave for class."
    r sad "Yeah, unfortunately."
    voice "audio/voice/rohan/rohan_um.mp3"
    r neutral "Are we coming here again tomorrow?"
    show sabie neutral at bounce
    s "Yep!"
    voice "audio/voice/sabie/sabie_heh.mp3"
    s mischievous "Next time, I {i}will{/i} get my hands on those pictures. Just you wait."
    r "Sure, as long as you remember."

    show sabie surprised
    show masami happy
    show tyree at bounce, left


    t happy "You won't."
    voice "audio/voice/rohan/rohan_nervouslaughter.mp3"
    r happy "Oop."
    show sabie annoyed at shake, center
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s annoyed "Hey!"
    m "He's not wrong."
    m neutral "Anyways, I've really got to run. You know how chemistry is. See you all!"

    show tyree neutral
    show sabie neutral
    show rohan neutral

    r "See you!"
    voice "audio/voice/tyree/tyree_takecare.mp3"
    t "Take care."

    jump lunch_end

# Sabie approaches Masami at the end of lunch in the hallway on the way to class
label lunch_end:

    hide masami
    scene bg black
    with Dissolve(1.0)
    scene hallway
    show masami at mc_pos
    with Dissolve(1.0)
    play music lighthearted fadein 1.0

    n "Masami heads quickly into the building and down the hallway to chemistry."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "(Thank God for the indoor heating. I don't know why we sit outside.)"
    m exasperated "(Actually, I do know. Sabie is a masochist and we're too dead inside to contradict her.)"
    show masami neutral
    n "His hand twitches and he realizes his fingers are still tightly wrapped around the object in his pocket."
    n "After a moment of hesitation, he lets go."
    m sad "(After all this time, I still cling to an old relic like this. Even though I know it's not going to help me with the situation at hand.)"
    voice "audio/voice/masami/masami_jie.mp3"
    m "(Even knowing it's not going to bring {i}jie{/i} any closer to home.)"
    m neutral "(I'm really some desperate fool, aren't I?)"
    m sad "…"
    m neutral "(At least the only person who'd bother me for it isn't - )"
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "{i}Ge{/i}!"
    show masami exasperated at shake, mc_pos
    m "(Well. Just when I thought she'd let up on me.)"
    show masami neutral
    n "Just to spite her, Masami picks up his pace."
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s "Oi! Halt, dumbass!"
    s "Don't make me run after you!"
    m "Hm?"

    play sound "audio/sound/footsteps_run.mp3"
    show sabie annoyed with moveinleft
    show sabie at shake, center

    n "Masami glances over his shoulder as if he's just noticed Sabie tearing down the sidewalk at full speed. He dramatically slows to a stop to let her catch up to him."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Heh. Did you really think I wasn't going to wait?"

    show sabie neutral

    n "Sabie shrugs."
    voice "audio/voice/sabie/sabie_well.mp3"
    s "Who knows."
    n "She goes up on her tiptoes and sticks out her right index finger to boop him on the forehead."
    show sabie innocent at bounce
    s "There's still a lot of things going on in there that you aren't telling me, {i}ge{/i}."
    s neutral "Not even after these sixteen {i}long{/i} years of knowing each other."
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "...And despite that, you're not going to stop calling me {i}ge{/i}, are you?"
    s mischievous "Nah. You being hung up over the fact that it’s \"culturally incorrect\" isn't gonna to stop me from making you my big bro."

    show sabie neutral

    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Heh. I’m not complaining anymore."
    m neutral "Just thinking about how it’s sort of become \"our thing.\" Kind of like…"
    voice "audio/voice/masami/masami_nevermind.mp3"
    m sad "Never mind."

    # The more serious part of the conversation
    voice "audio/voice/sabie/sabie_uh.mp3"
    s worried "Is everything alright? You've been kind of stuck in that head of yours for days now."
    s "Like {i}stuck{/i}, stuck. The {i}not-just-a-mood{/i} kind of stuck. You know what I mean?"
    s neutral "Wanna talk about it?"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "…"

    # Choose how to respond to her
    menu:

        "Be completely honest with Sabie":
            $ sabie_trust = True
            jump lunch_end_honest

        "Vaguely admit something is up":
            $ sabie_trust = False
            jump lunch_end_vague

        "Pretend nothing is wrong":
            $ sabie_trust = False
            jump lunch_end_deny

# Masami chooses to be honest with Sabie
label lunch_end_honest:

    m "Yeah. Kinda."
    voice "audio/voice/sabie/sabie_hmmmm.mp3"
    s worried "It's about Xinyi, right?"
    m "...Yeah."
    s neutral "Don't worry so much. She'll be back, I'm sure of it."
    s "You know that better than anyone. Don't you?"
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "I suppose."
    n "Sabie pats him reassuringly on the shoulder."
    show sabie at bounce
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "Then, take it easy. That's what she'd want for you."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Yeah. I'll try."
    m neutral "(I know that you're just saying these things to make me feel better, but I'll take it.)"
    m sad "(For now, I guess.)"

    jump lunch_end_invite

# Masami chooses to be vague about the issue
label lunch_end_vague:

    m happy "Was it that obvious?"
    show sabie innocent at bounce
    voice "audio/voice/sabie/sabie_well.mp3"
    s "Nah. I don't think anyone else noticed."
    s neutral "Mm, now that I think about it, maybe Tyree did."
    s innocent "Then again, who knows what he does or doesn't notice, because he won't say anything."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m neutral "True."
    s happy "But, that's besides the point!"
    s mischievous "You need someone to talk to."
    m "And that person {i}has{/i} to be you. Right."
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s worried "Oh, come on! Who else is qualified enough?"
    show masami exasperated at shake, mc_pos
    m "Well - "
    voice "audio/voice/sabie/sabie_heh.mp3"
    s neutral "Don't get me wrong, your guy friends are great and all."
    s mischievous "But do you really think that you're going to bring up any of your {i}feelings{/i} with any of them?"
    show masami at shake, mc_pos
    m "That's - "
    show sabie at bounce
    s "And!"
    s "If the problem is what I think it is, if you're not going to be telling me about it, you're not going to be telling anyone at all."
    m "That's..."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "That's true."
    m exasperated "(Damn. Why is it that she's always right about the most annoying things?)"

    show sabie neutral
    show masami neutral

    n "Sabie puts a hand on his shoulder, tilting her head a little as she looks him in the eyes."
    voice "audio/voice/sabie/sabie_well.mp3"
    s "Hey."
    s "I just don’t wanna see you holding things in until you explode."
    s "Let me know when you're ready to talk, alright?"
    voice "audio/voice/masami/masami_hm.mp3"
    m sad "..."
    m neutral "Alright."
    m "Thanks, Sabie."

    show sabie innocent at bounce

    s "You got it!"
    m "(It's nice being reminded that someone has my back, but…)"
    voice "audio/voice/masami/masami_whatever.mp3"
    m sad "(Well, it's probably too selfish of me to wish that there was someone who gets me a little better that I could talk to.)"

    jump lunch_end_invite

# Masami denies anything is wrong
label lunch_end_deny:

    n "Masami shrugs."
    show masami happy at bounce, mc_pos
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "I guess the schoolwork is getting to me."
    m neutral "And all those extracurriculars, you know?"
    voice "audio/voice/sabie/sabie_well.mp3"
    s worried "…If you say so."
    s neutral "Just tell me if you need anything, alright?"
    m sad "Uh…"
    m neutral "Sure."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "(I hate keeping things from her, but she's still…)"
    m "(She's still Sabie.)"
    m "(There's only so much about this that she gets.)"

    jump lunch_end_invite

# Sabie invites Masami to the party
label lunch_end_invite:

    show masami sad
    show sabie worried

    n "Sabie stares at him for a moment and blinks a couple of times."

    show sabie mischievous

    n "Then she snaps her fingers."
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Oh, I almost forgot! The head of the student council is hosting a Christmas party at his bougie house tomorrow."
    show sabie innocent at bounce
    s "You should come!"
    s neutral "I'm even dragging Tyree and Rohan along."
    s neutral "Well, Rohan was going anyways, but you get the point."
    voice "audio/voice/masami/masami_im...fine.mp3"
    m exasperated "I've already told you that I don't go to parties. Especially not Christmas parties."
    show sabie innocent at bounce
    voice "audio/voice/sabie/sabie_imean.mp3"
    s "I know. But you need a distraction."
    n "She waggles a finger mischievously in his face."
    s mischievous "And if someone doesn't give you a good one, you're never going to learn about how nice it is to just live in the moment instead of brooding all the time."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "I do not brood."
    s "You do brood. You're doing it right now."
    voice "audio/voice/masami/masami_whatever.mp3"
    m sad "This isn't brooding. This is exasperation."
    n "Sabie waves her hand dismissively."
    s "Same difference."
    s neutral "Anyways. It doesn't hurt to start the weekend a little early, now does it?"
    m "We'll still have class the next day."
    voice "audio/voice/sabie/sabie_well.mp3"
    s mischievous "Psh. Teachers know that break starts next week."
    s "They can't give us {i}that{/i} much more grief when finals are in January, can they?"
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "That's not how - "
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s neutral "Come on. It's just one day."
    s "One singular day."
    s "You can relax, chat up some girls - "
    m sad "I can't chat up girls - "
    s mischievous "Please, I've seen you in your glory days."
    show sabie innocent at bounce
    s "You had the stagehands swooning from second hand exposure. And that wasn't even the kiss scene!"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m exasperated "That was in middle school. I run audio now."
    voice "audio/voice/sabie/sabie_heh.mp3"
    s neutral "Psh, whatever. What I {i}mean{/i} is that you have experience."
    s "Besides, what's the difference between flirting in improv and flirting in reality?"
    show masami at shake, mc_pos
    m "There is a difference! None of them were - "

    stop music

    show sabie happy at shake, center
    s "ALYSSA!"

    jump lunch_end_alyssa

# Alyssa walks on scene
label lunch_end_alyssa:

    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m surprised "Wha - "

    play music uptempo fadein 1.0

    n "Masami whirls around to see Sabie waving wildly to an approaching figure at the other end of the hall."
    n "A very familiar figure."
    show masami at shake, mc_pos
    m "(Shit.)"
    m "(Shit. Shit. Shit.)"
    m "Sabie. What are you - "
    play sound ["audio/sound/thud.mp3","<silence 1.0>"] loop volume 0.5
    n "Sabie ignores him and starts jumping up and down."
    stop sound
    show sabie at shake, center
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "HEY ALYSSA, BESTIE - "

    show masami exasperated at shake, mc_pos
    show sabie at shake, center
    pause(0.1)
    show sabie at left with move
    show bg hallway behind sabie at hpunch
    show sabie surprised
    play sound "audio/sound/crash.mp3" volume 0.2

    n "Sabie lets out a muffled cry of protest as Masami puts a hand lightly over her mouth and yanks them behind a corner."
    show sabie annoyed
    n "As soon as they're safely behind the wall, Sabie bats his hand away."
    show sabie at shake, left
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s "What the hell was that for? I'm doing you - "
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "Please. Just."
    m sad "Why is it that you two have to be friends?"
    voice "audio/voice/sabie/sabie_uh.mp3"
    s worried "Are you jealous of my bestie status with Alyssa?"
    m surprised "No! Of course not - "
    show masami exasperated at shake, mc_pos
    m "Ugh, that's not what I meant, but whatever."
    voice "audio/voice/masami/masami_whatever.mp3"
    m sad "I've already told you that I've stopped trying to \"get to know her better.\""
    voice "audio/voice/sabie/sabie_well.mp3"
    s mischievous "Uh, you did not tell me that you've stopped trying. You told me it was complicated."
    show sabie happy at bounce, left
    s "Which means you should be trying harder!"
    s innocent "If someone like me can get on her good side, so can you."
    show masami exasperated at shake, mc_pos
    m "That's…not what I meant by \"complicated.\""
    show sabie worried at shake, left
    s "Wait, did you already talk to her, piss her off, and not tell me anything because you were embarrassed?"
    voice "audio/voice/masami/masami_huh.mp3"
    m surprised "What? No! I - "

    # Alyssa actually arrives on scene with Nasir in tow
    n "Masami freezes as Alyssa's voice drifts into earshot."
    show masami sad
    n "He presses himself further against the wall and motions for Sabie to do the same."

    hide sabie with Dissolve(0.4)

    n "For once, Sabie actually follows through, albeit with a questioning look."
    voice "audio/voice/sabie/sabie_uh.mp3"
    s "Hey. Wouldn't now be a good - "
    show masami exasperated at shake, mc_pos
    m "Shhh."
    show masami neutral
    n "Remarkably, Sabie obediently purses her lips and falls silent."
    a "...That was weird. I thought I heard something."
    voice "audio/voice/nasir/nasir_oh.mp3"
    u "Really? What?"
    show masami surprised
    n "At the sound of the second voice, Masami's stomach drops."
    m "(Damnit. It's Nasir.)"
    m sad "(Of course he's with her.)"
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_nevermind.mp3"
    m "(I...I'm not {i}bothered{/i} that she's such close friends with one of the most…{i}academically{/i} perfect students at our school.)"
    m sad "(Well, I'm not jealous anymore, at least.)"
    m "(But...)"
    m exasperated "(This just makes the whole situation so much more awkward.)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "..."
    m "(Sabie, why?)"
    m exasperated "(Why do you do things like this?)"
    voice "audio/voice/sabie/sabie_nervouslaughter.mp3"
    n "As if on cue, Masami hears Sabie chuckle sheepishly."
    s "Sorry {i}ge{/i}. Guess I didn't account for that little detail."
    voice "audio/voice/masami/masami_whatever.mp3"
    m neutral "Mm. Whatever. It's…fine."
    m sad "(It's not fine.)"
    m neutral "(...I still kind of want to listen in, though.)"
    m sad "(But should I?)"

    menu:

        "Listen in":
            jump lunch_end_listen

        "Ignore them":
            jump lunch_end_ignore

# Masami decides to listen in
label lunch_end_listen:

    n "Despite his better judgement, Masami's curiosity gets the better of him and he peeks over his shoulder."

    jump lunch_end_nasir

# Masami tries to ignore them, to no avail
label lunch_end_ignore:

    show masami exasperated
    n "Masami shuts his eyes and tries to block out what's going on."
    show sabie at left with easeinleft
    n "Unfortunately, Sabie keeps nudging him."
    show sabie at bounce, left
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "Pst. Pay attention."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "No."
    show sabie at shake, left
    voice "audio/voice/sabie/sabie_uh.mp3"
    s worried "But aren't you the least bit curious?"
    m "No."
    show sabie at shake, left
    s "Don't you want to talk to Alyssa the slightest bit?"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "..."
    m "No."
    show sabie at bounce, left
    voice "audio/voice/sabie/sabie_gotcha.mp3"
    s mischievous "Aha, I see that hesitation! I know you. I know you want to hear her voice…"
    show masami at shake, mc_pos
    m exasperated "Will you shut up?"
    s innocent "Who do you think I am?"
    m sad "Please?"
    voice "audio/voice/sabie/sabie_heh.mp3"
    s neutral "Not until you put your eyes in the right place."
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_whatever.mp3"
    m "Ugh, fine."
    m sad "I'll pay attention."
    m exasperated "But only because I know you won't stop otherwise."

    show sabie mischievous

    n "Sabie rubs her hands together."
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Good choice. Good choice…"
    hide sabie with easeoutleft
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "(I'm going to regret this.)"
    n "He peeks over his shoulder as inconspicuously as he can, trying to ignore the blood pounding in his ears and Sabie's triumphant cackling."

    jump lunch_end_nasir

label lunch_end_nasir:

    show nasir at innerright
    show alyssa neutral at right
    with Dissolve(0.3)

    voice "audio/voice/nasir/nasir_hm.mp3"
    na "…Huh. Strange. I don't think I heard that."
    a nervous "Really? That's a first."
    na sad "What do you mean?"
    a happy "Well, usually you're the one who catches the things I miss."
    voice "audio/voice/nasir/nasir_itsnothing.mp3"
    na happy "Not really."
    a "Yes, you are."
    show alyssa at shake, right
    show nasir at shake, innerright
    a neutral "Come on, Mr. I-Got-Into-MIT-Early-Action. Have more confidence in yourself!"

    hide nasir
    hide alyssa
    show sabie surprised at left
    with Dissolve(0.3)
    show masami surprised

    n "Sabie exchanges glances with Masami before she leans over to stage whisper into his ear."
    voice "audio/voice/sabie/sabie_imean.mp3"
    m "I mean, I'm not surprised, but…"
    s "…how does the whole school not know about this yet when he's basically a celebrity?"
    voice "audio/voice/masami/masami_hm.mp3"
    m neutral "Yeah."
    show sabie neutral
    n "Sabie shrugs."
    s "Beats me."
    show sabie at bounce, left
    s innocent "Some people are just good at keeping things to themselves."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "Unlike you."
    show sabie at shake, left
    voice "audio/voice/sabie/sabie_ugh.mp3"
    s annoyed "Hey!"

    hide sabie
    show masami neutral
    show nasir happy at bounce, innerright
    show alyssa neutral at right

    voice "audio/voice/nasir/nasir_quietchuckle.mp3"
    n "In the meantime, Nasir chuckles, though it seems a little strained."
    na "That was luck. You know how college admissions are."
    show alyssa happy at bounce, right
    a "What about being principal cellist of the National Youth Orchestra?"
    show alyssa at bounce, right
    a "Or being on the International Physics Olympiad team?"
    show alyssa at bounce, right
    a "Or being a nationally ranked Scrabble player?"


    hide nasir
    hide alyssa
    show sabie mischievous at shake, left

    n "At the last one, Masami feels a nudge on his arm."
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Nationally ranked Scrabble player, huh?"
    s happy "Hey, {i}ge{/i}, maybe you finally have someone that could - "
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m exasperated "No."
    s worried "But - "
    show masami at shake, mc_pos
    m "Words with Friends is not Scrabble."
    voice "audio/voice/sabie/sabie_well.mp3"
    s "But you still beat me every time by at least 200 points!"
    m happy "I hate to say it, but you're just not very good."

    show sabie annoyed at shake, left

    n "Sabie sticks out her tongue at him."
    s "Meanie."

    # Nasir approaches
    n "Masami is about to make a retort when he feels a quick brush against his elbow."

    hide sabie
    show nasir at center
    show masami surprised at shake, mc_pos

    voice "audio/voice/masami/masami_huh.mp3"
    n "He whirls around to find himself inches away from Nasir's face."
    n "Nasir looks briefly at Sabie before his gaze settles on Masami."
    m "Uh. Hi?"
    voice "audio/voice/nasir/nasir_quietsigh.mp3"
    na sad "..."
    m "(Shit. He definitely heard everything we said.)"
    n "For a moment, the two of them just stand there looking at each other."

    show nasir happy at bounce, center

    n "Then, to his surprise, Nasir's mouth breaks into a warm, encouraging smile."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_oh.mp3"
    m "(???)"

    show alyssa nervous at bounce, right with Dissolve(0.3)

    a "Uh, Nasir?"
    show nasir at shake, center
    voice "audio/voice/nasir/nasir_huh.mp3"
    na surprised "Huh?"
    show alyssa at bounce, right
    a "You still there?"

    show nasir neutral at innerright with move

    n "Nasir turns sheepishly back to Alyssa, who seems thankfully oblivious to the fact that Masami and Sabie were standing right behind him."
    na "Yeah."
    show masami neutral
    n "Masami sighs in relief."
    voice "audio/voice/masami/masami_hm.mp3"
    m "(Thank God he's tall enough to block Alyssa's view of us.)"
    na "Sorry, I saw a magpie outside and got a little distracted."
    a neutral "A magpie? I thought they didn’t live around here."
    a "Or at least, I’ve never seen one that did."
    n "Nasir shrugs."
    show nasir happy at bounce, innerright
    voice "audio/voice/nasir/nasir_quietchuckle.mp3"
    na "They come by every once in a while."
    na neutral "You’ll find them. If you know where to look."
    show alyssa happy at bounce, right
    a "Ah. Well, I’ll take your word for it."
    na sad "..."
    a sad "What?"
    voice "audio/voice/nasir/nasir_itsnothing.mp3"
    na happy "It’s nothing."
    a neutral "Okay then."
    na neutral "Anyways, what was I saying before?"

    hide nasir
    hide alyssa
    with Dissolve(0.3)

    jump lunch_end_aftermath

label lunch_end_aftermath:

    n "And then, just like that they're gone, swept up in the flow of students meandering down the hall."
    show masami surprised
    n "Masami's hand flies forward after him in spite of itself."
    show masami at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "Wha - W-Wait!"
    m "(What the hell was that about?)"
    m "(Why did he - )"

    show sabie mischievous at center with Dissolve(0.2)

    show sabie at bounce, center
    voice "audio/voice/sabie/sabie_mischievousgiggle.mp3"
    s "Ooh, so somebody does want to play a little Scrabble after all."
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "I-I did not say that."
    show sabie neutral
    n "Sabie gives him a pat of mock consolation on the shoulder."
    show sabie innocent at bounce, center
    voice "audio/voice/sabie/sabie_imean.mp3"
    s "Aw, it's okay to defend your butthurt little male ego sometimes."
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "For the last time. I. Am. Not. Jealous. Of. Him."
    m sad "Okay?"

    show sabie neutral

    n "Sabie waves her hand dismissively."
    s innocent "Yeah, yeah. Whatever you say."
    s neutral "You really need to unwind that mind of yours."

    jump lunch_end_party

label lunch_end_party:

    # Back to the party
    s mischievous "Which brings me back to the Christmas party."
    show sabie happy at bounce
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s "You should come!"
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "Ugh. This again?"
    show sabie worried at shake, center
    voice "audio/voice/sabie/sabie_uh.mp3"
    s "What do you mean? Can't you appreciate a break when you see it?"
    s neutral "You'll have people you know there. Rohan. Tyree. Me."
    m sad "Well, yeah. But Rohan and Tyree are probably going to be playing Smash."
    m happy "And you're going to be - uh. Singing karaoke."
    voice "audio/voice/sabie/sabie_imean.mp3"
    s worried "Look, I understand if you don't want to get drunk with me."
    s "But what's wrong with Smash? I thought you liked playing it."
    m neutral "Uh…I don’t own a console."
    s "But you’ve played it before."
    m sad "Yeah, but..."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "Look, I’m not Rohan. I don’t have practice."
    s "Neither does Tyree."
    m neutral "Tyree is Tyree."
    s neutral "Eh, you’re not wrong. No Smash then."
    n "Sabie thinks for a moment."
    voice "audio/voice/sabie/sabie_heh.mp3"
    s mischievous "Okay. I've got it."
    m "What?"
    s happy "I'll just introduce you to some of my friends who also sit in the corner."
    show sabie innocent at bounce, center
    s "And then you guys can sit in awkward silence together!"
    voice "audio/voice/masami/masami_whatthehell.mp3"
    m exasperated "..."
    s neutral "Or play Scrabble or whatever else you nerds do."
    m "Aren't you also a nerd too?"
    s mischievous "Psh, you know what I mean."
    voice "audio/voice/sabie/sabie_cmon.mp3"
    s happy "Anyways, it'll be fun!"
    s neutral "Whaddya say?"
    m sad "..."
    m "(She's not going to let up, is she?)"
    n "Masami throws his hands up in surrender."
    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_whatever.mp3"
    m "Fine, I'll think about it, okay?"
    m sad "Satisfied?"

    show sabie happy at bounce, center

    voice "audio/voice/sabie/sabie_gotcha.mp3"
    n "Sabie does a fist pump."
    s innocent "Ayy! That's more like it. Glad you came around."
    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_huh.mp3"
    m "What? That's not what I - "
    play sound "audio/sound/bell_warning.mp3"
    n "Before he can finish his sentence, Masami is conveniently cut off by the blare of the warning bell."
    s surprised "Shit!"
    voice "audio/voice/sabie/sabie_heh.mp3"
    s mischievous "Gotta run. Text me later when your answer is yes!"

    hide sabie with easeoutright

    show masami at shake, mc_pos
    m "Wait, Sabie - "
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m exasperated "(And she's gone.)"
    m sad "..."
    m exasperated "(What have I gotten myself into?)"
    show masami sad
    n "He pulls out his phone, turning it over in his hands once. After a moment, he slips it back into his pocket."
    voice "audio/voice/masami/masami_nevermind.mp3"
    m "(I'll figure it out later.)"

    jump masami_home_3

# Scene cut to Masami's car
label masami_home_3:

    stop music fadeout 2.0
    hide masami
    scene bg black
    with Dissolve(1.0)
    show masami at mc_pos
    scene bg carday
    with Dissolve(1.0)
    play music emotional fadein 1.0 fadeout 1.0


    m "(I'm home.)"
    m sad "..."
    voice "audio/voice/masami/masami_hm.mp3"
    m "(It's been three whole hours and I still haven't figured out what I'm doing yet.)"
    m "(I usually wouldn't be too worried about something like this, but…)"
    play sound "audio/sound/phone_vibrate.mp3" loop
    n "As if on cue, Masami's phone starts buzzing again with new messages."
    m exasperated "(…and it's starting again.)"
    stop sound
    n "He sighs and sets his phone to silent."
    m neutral "(Finally. Peace and quiet for me to think. Should have done it earlier.)"
    m sad "..."
    voice "audio/voice/masami/masami_whatever.mp3"
    m "(Might as well head inside.)"

    jump masami_kitchen_3

# Scene cut to the kitchen
label masami_kitchen_3:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg kitchen
    show masami at mc_pos
    with Dissolve(1.0)

    n "A pungent aroma fills the air long before Masami reaches the kitchen."
    voice "audio/voice/masami/masami_oh.mp3"
    m "(Looks like we're having curry tonight.)"
    play sound "audio/sound/boil.mp3" volume 0.1 fadein 3.0 fadeout 3.0
    n "He hangs his coat on the rack near the door."
    m "{i}Ma{/i}. I'm home."

    show wsprite with Dissolve(0.1)
    show wsprite at bounce

    mm "Masami!"
    n "Masami's mother leaves her cooking in an instant to sweep her son up into a warm hug, her eyes twinkling."
    mm "{i}Bagaimana harimu?{/i} Learn a lot today?"
    m "Yeah."
    mm "Good, good. You keep working hard, you have good future."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m sad "…"
    m neutral "Yeah. I know."
    n "His mother doesn't notice his discomfort as she breaks away to give the pot a quick stir."
    n "Masami's gaze follows her, his expression a pleasant mask once more."
    mm "We have curry tonight. Warm for winter."
    show masami at bounce, mc_pos
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "It smells really good. Thanks for making it."
    n "His mother beams."
    mm "Of course!"
    n "She gestures towards the refrigerator."
    mm "If you not busy, you can help make {i}tangyuan{/i}. I buy ingredients today."
    voice "audio/voice/masami/masami_oh.mp3"
    m sad "{i}Tangyuan{/i}? Isn't it a little early to make that? {i}Dongzhi{/i} is in three days."
    n "His mother shifts quietly. Her lips purse briefly before they curve back into a bright smile."
    mm "Ah."
    show wsprite at bounce
    mm "Not bad to start early, right?"
    mm "You grow up, you eat more! Also, more to save for later."
    mm "I buy sesame. More variety. You ask for that, right?"
    voice "audio/voice/masami/masami_hm.mp3"
    m "..."
    m neutral "Yeah, I did."
    show masami happy at bounce, mc_pos
    m "Thanks for remembering."
    m neutral "I'll get started on making the peanut ones after dinner and freeze them. Probably should get warmed up with something familiar before I try anything new."
    mm "You're welcome."
    n "She leans forward to tuck a stray lock of hair behind his ear."
    mm "Stay focused, okay?"
    mm "And remember family. We are always here for you. We stick together."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "You've told me that before."
    n "She smiles and pats his shoulder."
    show wsprite at bounce
    mm "I know. I just don't want you to forget."
    m sad "..."
    m neutral "Right."
    voice "audio/voice/masami/masami_sorryaboutthat.mp3"
    m sad "I've...got some homework to do."
    m happy "I'll be back down in a bit!"
    mm "Okay, I call you down for dinner."
    mm "Remember, stay focused!"
    m neutral "...I will."
    stop sound

    jump masami_room_3a

# Scene cut to Masami's room
label masami_room_3a:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene bg bedroom
    show masami sad at mc_pos
    with Dissolve(1.0)
    play sound "audio/sound/door_open.mp3"
    queue sound "audio/sound/door_close.mp3"

    n "The moment that Masami sets foot in his room, he flops down face first on the bed with a groan."
    stop sound
    show bg bedroom at vpunch
    show masami exasperated at vpunch, mc_pos
    play sound "audio/sound/bed_bounce.mp3"
    m "(Ugh…)"
    m "(What a day…)"
    m sad "(I don't feel like functioning anymore.)"
    n "He rolls over onto his back to stare at the ceiling."
    voice "audio/voice/masami/masami_whatever.mp3"
    m exasperated "(I should be doing homework, but I can't focus.)"
    m sad "(Sorry, Mom.)"
    m "(Sorry, God.)"
    m "(Sorry, life expectations.)"
    m "(Looks like I'm going to be failing you all today.)"
    n "Masami gently removes a small keychain in the shape of a magpie from his pants pocket, turning it over in his hands."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m happy "(Heh. You never told me you'd be giving me so much trouble after you left.)"
    m sad "..."
    m "(Three days from now…)"
    m "(You said you'd be back to give me your answer then.)"
    m neutral "(And I'd promised to give you mine. Even if neither of us had quite figured things out yet.)"
    voice "audio/voice/masami/masami_jie.mp3"
    m sad "(...I don’t know if I’m more afraid of my answer or yours.)"
    m  "(And I...I don't think I'm ready to let go of everything.)"
    m neutral "(At least, not like you did, {i}jie{/i}. I'm not as brave as you.)"
    m sad "(But sometimes, I wonder…)"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    n "Masami sighs quietly to himself and leans over to set the keychain on his desk."
    m "(Maybe Sabie is right. I do need a distraction.)"
    n "He pulls out his phone, thumbing idly through the home screen before he decides to open the messaging app."

    jump phone_3b

# Brings up phone screen of Masami's phone
label phone_3b:

    hide masami
    call phone_open(True) from _call_phone_open_11

    call message(m, "Hey.", True) from _call_message_208
    call message(m, "I'm going.") from _call_message_209

    call phone_close() from _call_phone_close_11

    jump masami_room_3b

# Back to Masami's room
label masami_room_3b:

    show masami sad at mc_pos
    n "Masami puts down his phone and flops onto the bed beside it."
    n "He can see the lights on the screen seeping into the covers as Sabie’s replies roll in."
    voice "audio/voice/masami/masami_im...fine.mp3"
    m "..."
    m exasperated "(I'll read it later.)"
    show masami sad
    n "Masami rubs his eyes and turns to stare at the ceiling again."
    m "(What would you have thought of me if you'd known what I'd done, {i}jie{/i}?)"
    m neutral "(I…hope that you're proud.)"

    scene bg black
    hide masami
    with Dissolve(3.0)
    stop music fadeout 2.0

    jump day2_transition
