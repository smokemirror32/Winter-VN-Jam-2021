﻿## DAY 3 - BEFORE

label class_3:

    # SEFF: SCHOOL BELL RING
    m "Thanks, Mr. Friedman! Happy holidays to you, too!"
    n "Masami steps out of the classroom, joining the sea of students heading to lunch."
    m "(Phew. That last bit on LR circuits was rough. I'll probably have to review over break.)"
    m "(At least the material is kinda interesting.)"
    m "(Unlike chemistry, which is just watered down physics.)"
    m "(Math with memorization.)"
    m "(The only thing it's good for is making reactions pretty enough for you to forget how boring it is.)"
    n "Masami sighs."
    m "(Still got two more classes of it to go. Two more days. I can make it.)"
    m "(...Probably.)"
    m "(Heh. Times like this make it really easy for me to understand why {i}jie{/i} - )"
    n "He freezes suddenly mid-thought and gives his head a quick shake."
    m "…"
    m "(After three years, I should be better with this.)"
    m "(Focus, Masami. Focus.)"
    n "He rubs his temples."
    m "(What was I supposed to be doing again?)"
    m "(...Oh, right. Lunch. I'm headed to lunch.)"
    n "Just then, Masami's phone buzzes in his pocket."
    m "(Ah, that's probably Sabie.)"
    n "He pulls it out and unlocks it."
    m "(Yup, it's her.)"
    m "(...Wonder what she wants this time.)"

    jump phone_3a

# This is a series of text messages between Sabie and Masami
label phone_3a:

    s "yo"
    s "yooo"
    s "{i}ge{/i}"
    s "r u there"
    s "…"
    s "{i}ge geeeeeee{/i}"
    s "u r not ignoring me right"
    s ":((((("
    m "Hey"
    s ":o"
    s "ur here"
    s ":D"
    m "Ye"
    m "Sorry, just got out of class"
    s "tis ok ^.^"
    s "we r outside at usual spot"
    s "dont take too long or rohan will niwnag;awngawn"
    s "nae;iwngliane;li;ngial"
    s "I;eangioaen;oein;ioeanwi"
    s "ianewgilnewa"
    m "?"
    s "naigneianeiawne;"
    s "wia;eiai"
    s "eaaijeianwl"
    m "…"
    s "sry he took my phone again :("
    m "Okay. You deserved it."
    s "hey >:("
    s "rude"
    m ":)"
    s "fine then dont come"
    s "i dont need u to bully me"
    m "Someone needs to bully you"
    s ">:("
    m ":)"
    s "meanie"
    s "i hate u"
    s "leave me alone"
    m "Okay bye"

    jump hallway_3

# Return back to the hallway scene
label hallway_3:

    n "Masami slips the phone back into his pocket."
    n "It vibrates plaintively against his hip."
    n "He just shakes his head and smiles a little to himself."
    m "(Heh. Idiots.)"
    n "He continues down the hallway at his usual leisurely pace."
    m "(They'll manage.)"
    m "(...Probably.)"

    jump lunch_chaos

# Scene change to the lunch spot
label lunch_chaos:

    scene # TODO: Replace with courtyard!

    n "As per usual, Masami hears the chaos long before he sees it."
    r "Hey, let go of my phone!"
    s "But you gotta share those pictures we took in the group chat."
    r "Uh, those were supposed to be private. Just for me!"
    s "That's not what you said yesterday."
    r "I-I take what I said back!"
    s "Too late, buddy. You gotta learn to - ah!"
    n "As if on cue, Masami's own phone, which had been silent for some time, starts buzzing again."
    m "(I should probably hurry up.)"
    n "Masami quickens his pace to a light jog as he heads down the courtyard path."
    m "(Of all the places they could sit, they still chose the spot farthest from the door.)"

    show rohan annoyed at right
    show sabie mischievous at left
    with Dissolve(0.1)

    n "As he gets closer, he can see Rohan and Sabie kneeling on top of the only occupied table in the yard, fighting for possession over what is apparently Rohan's phone."

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    n "From the seat at a nearby bench, Tyree watches with mild amusement as he eats his kale salad."
    n "He gives Masami a slight nod."
    t "Hey."
    m "Hey, Tyree."

    hide tyree
    show rohan annoyed at right
    show sabie mischievous at left
    with Dissolve(0.1)

    n "At the sound of Masami's voice, Rohan's head whips around."
    r "What?"
    r neutral "Oh! Hi!"
    n "He gives the phone a tug. Sabie doesn't budge."
    r happy "I, uh. Need a little help here?"
    n "Sabie swats at his hand. Rohan yelps."
    r annoyed "Hey, what was that for?"
    s happy "That. Would be cheating."
    s neutral "Besties only help besties."
    s mischievous "Right, {i}ge{/i}?"
    n "Sabie winks at Masami."
    r sad "Hey! I thought we were besties."
    s annoyed "Well, not after you sent those drunk karaoke clips of me in the chat."
    r annoyed "But that was because you posted those shots you took of me in the mall!"

    show sabie neutral

    n "Sabie shrugs."
    s happy "It's not a big deal. You looked good. And they already knew all about your little schtick."
    r embarrassed "…"
    s mischievous "Besides…weren't you the one who said you wanted everyone to get more comfy with {i}that{/i} side of yourself?"
    r "I - "
    r sad "…"
    s happy "Don’t be shy. I know you, theater butterfly."
    r embarrassed "I-I never said - "
    s mischievous "Sucks to suck ‘cuz you know I'm right."
    r "I - "
    r sad "Ugh. Fine."
    r annoyed "But that doesn't give you the right to send the rest of the - "
    s surprised "Wait. You've got more pictures?"
    r embarrassed "What? No, I didn't mean - "
    s mischievous "Ooh, now this is something I have to see!"
    r "Sabie, no!"
    n "Sabie makes another desperate, backwards yank at Rohan's phone."

    # TODO - Make them go off-screen and have screen shake!
    hide sabie
    hide rohan
    with easeoutleft

    n "Rohan holds on for dear life as the momentum sends them both flying onto the ground, where they continue to wrestle for control."
    n "Masami takes a cautious step forward."
    m "Um - "

    show rohan embarrassed at right with Dissolve(0.1)

    r "Masami, do something! Don't let her - ah!"

    show sabie mischievous at left with Dissolve(0.1)

    n "Rohan yelps again as Sabie's elbow brushes roughly against his cheek."
    s happy "Oh, please. You know you're going to be thanking me later."
    s mischievous "And, {i}ge{/i}? If anything, you should be helping - me!"

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    t "Or you could just watch them."

    show rohan annoyed at right
    show sabie annoyed at left
    hide tyree

    r "What?"
    s "Hey!"

    hide rohan
    hide sabie
    show tyree happy
    with Dissolve(0.1)

    t "It's free entertainment."

    show rohan annoyed at right
    show sabie annoyed at left
    hide tyree

    n "Sabie sticks her tongue out at Tyree."
    s "Ugh. So rude."
    r sad "For once, I agree with her."

    show rohan neutral

    s happy "Aw thanks, Rohan. I appreciate it."
    s annoyed "But also. Rude."
    m "(Hm…)"

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
    show sabie happy

    r "Rohan's expression instantly deflates. In the meantime, Sabie does a fist pump."
    s "Aha, yes! Someone understands where I'm coming from."
    n "Masami gives her a pointed look."
    m "I'm not finished."
    s surprised "Oop."
    m "And I'm not letting you have full control over Rohan's phone."
    m "(Not going to make that mistake again after the flood of deep fried memes last time.)"
    s annoyed "Aw, dammit."
    m "Anyways, as I was saying, it helps to open up to people about stuff like this."
    m "Helps you accept yourself, too."
    m "I'm not going to force you to share, but I still think it would be good to."

    show rohan neutral
    show sabie neutral

    n "Rohan's shoulders relax the slightest bit."
    r sad "Yeah. I get that. But…"

    show sabie worried

    n "His voice trails off as he looks away."
    m "If you're worried about rejection, we already promised we wouldn't judge you for it, didn't we?"

    hide sabie
    hide rohan
    show tyree
    with Dissolve(0.1)

    t "Agreed."

    show sabie at left
    show rohan at right
    hide tyree
    with Dissolve(0.1)

    n "After a moment of hesitation, Rohan nods."
    r "Okay. I'll think about it."
    m "Cool. Er, Sabie?"
    s "Yeah?"
    m "Could you let go of his phone?"
    n "Sabie blinks at him uncomprehendingly for a moment before she realizes her hands are still clamped down tight around it."
    s surprised "Oh."
    n "She obediently lets go. The moment she does, Rohan quickly tucks it away, eyeing her with a healthy amount of distrust."
    n "Masami sighs in relief."
    m "(That was easier to take care of than usual.)"

    jump lunch_stable

# If Masami decides to help Rohan
label lunch_chaos_rohan:

    m "Sabie. Let go of his phone."
    s surprised "But - "
    m "Now. Or I'll make you do it myself."
    s annoyed "Ugh. Fine. Spoilsport."
    n "Sabie sticks out her tongue at him, but grudgingly complies."
    n "The moment she lets go, Rohan snatches up his phone and stuffs it hastily into his pocket."
    r happy "Phew. Thanks."
    m "Don't mention it."
    m "(It would be good for Rohan to get some confidence from sharing those photos, but I don't want to force him to do anything he's not comfortable with.)"

    jump lunch_stable

# If Masami decides to watch them both suffer
label lunch_chaos_tyree:

    m "I wash my hands of this."
    r embarrassed "What? You can't just - "
    s mischievous "Ohoho, you heard him. This one's between you and me, string bean."
    r annoyed "Urgh…"
    r "If that's what it's going to be, I am not going to let you have my phone."
    s "Bet!"
    n "With that, the two of them begin to struggle for control again. Or at least, Rohan is struggling, while Sabie bats lightly at his limbs, clearly toying with him."

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    n "Tyree catches Masami's eye." # TODO: Start here!
    t "Who do you think is going to win?"
    m "Hm, tough one, but I'm going with Sabie."
    m "(After all, there's only so much you can do against someone on the wrestling team. Even if they're only on JV.)"
    t "Same."

    show sabie at left
    show rohan sad at right
    hide tyree
    with Dissolve(0.1)

    r "Thanks for the vote of confidence."
    m "Sorry, Rohan, but I'm afraid I have to take into account prior experience."
    s mischievous "As you should. Those noodle arms got nothing on these guns."
    r annoyed "H-Hey! This time will be different."
    s happy "Sure. That's what you said last time."

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    t "Change your mind, Masami?"
    m "Nope."
    t "Good."

    show sabie mischievous at left
    show rohan sad at right
    hide tyree
    with Dissolve(0.1)

    n "As expected, it isn't even a minute before Sabie wrests control of the device away from him. Rohan lies spread eagle on the ground in defeat."
    s happy "Ehe. Now, let's see…"
    s surprised "Dammit. You changed the passcode again."

    show rohan happy

    n "Rohan's eyes glint back at her in triumph."
    r happy "Heh."
    s annoyed "Ugh. Maybe it’s the one from last week? Nope. Or the week before that? Nope again…"
    n "Sabie proceeds to check a flurry of combinations. After a couple of minutes, she stops."
    s neutral "Rohan, bestie, can you please - "
    r neutral "Nope."
    s worried "But - "
    r happy "Sucks to suck."
    m "Well. Why am I not surprised?"
    s annoyed "Hey! What did I do to deserve that attitude from you?"

    hide rohan
    hide sabie
    show tyree
    with Dissolve(0.1)

    t "Everything."

    show sabie annoyed at left
    show rohan at right
    hide tyree
    with Dissolve(0.1)

    s "Rude. I was not asking for your opinion."
    m "I mean, he does have a point. This is a weekly occurrence."
    r happy "Yeah. And now we're at the part where you give me my phone back?"
    n "Sabie purses her lips as her gaze bounces between Masami, Tyree, and Rohan."
    n "Then, she sighs and hands Rohan's phone back to him." # TODO: Add motion for this!
    s "Ugh. Fine. Thought I'd get lucky for once, but whatever."
    s "Guess I have no choice when everyone decides to gang up on me like that."

    show rohan neutral

    n "For his part, Rohan tucks the phone quickly into his pocket, eyeing Sabie with a healthy amount of distrust."
    n "Masami smiles quietly to himself."
    m "(Some things never get old, do they?)"

    jump lunch_stable

# Return to civil discussion
label lunch_stable:

    # TODO: Fix spacing and make move simultaneous
    show sabie neutral at center with move
    show rohan neutral at right with move
    show tyree at left with moveinleft

    n "Rohan and Sabie move back to sit at the table like proper civilized human beings. Tyree picks up his things to join them and Masami follows suit."
    n "Once they've all gathered, Sabie rubs her hands together."
    s happy "So. How's everyone doing?"
    r sad "Why this question all of a sudden? Can we like, you know, talk about the usual stuff?"

    show sabie neutral

    n "Sabie shrugs."
    s "We could."
    s mischievous "But I also kind of want to check in since {i}some{/i} people I don't share their feelings unless they're asked to."
    s happy "So. How about it?"
    r "Uh…"
    t "I'm doing fine."
    m "Same."
    r neutral "What they said."
    s annoyed "That's...not quite what I meant."
    n "Tyree shrugs."
    t "I answered your question."
    m "He's not wrong."
    n "Sabie rolls her eyes dramatically."
    s happy "Oh, my bad. It seems that I did. Let me specify."
    s "Are your classes less sucky than usual?"
    s "Are you saying your prayers so that your sad grades will get you into the Ivy League of your dreams?"
    s "Are your extracurricular overcommitments getting you down?"
    s "Are you counting down the days to Christmas carousing and {i}Dongzhi{/i} binge-eating like they're a lifeline from above?"
    s "Are you - "
    n "She stops when she sees Rohan raising his hand."
    s neutral "Yeah?"
    r "Question. What's {i}Dongzhi{/i}?"
    t "It's an East Asian holiday centered around reuniting with family and eating {i}tangyuan{/i}."
    s "Basically Thanksgiving with a better menu."
    m "(...And the assumption that you have the extended family to spend it with.)"
    r happy "Oh. Cool!"
    s "It is cool! You should look into making some of the traditional food."
    r neutral "Definitely thinking about it."
    s happy "Ayy, can't wait to see how it turns out!"
    s worried "Anyways, let's see, what else do I need to ask you emotionally constipated children to help you open up properly?"
    s happy "Oh yeah! Are you - "
    r sad "Um, I think we get the point."
    s mischievous "Great!"
    n "She puts elbows on the table, hands resting in her open palms as she leans forward."
    s "So. Got an answer?"
    r embarrassed "Uh - "

    show rohan neutral

    t "I can go."
    s happy "Okay, let's hear it."

    jump lunch_stable_tyree

# Tyree's turn
label lunch_stable_tyree:

    t "My classes and grades are fine. My extracurriculars are going well. I am looking forward to going on break."
    s annoyed "…"
    m "…"
    r happy "Pft."
    s worried "That was kind of vague."
    t worried "I'm not sure what else you want me to say."
    s "Uh, anything on recruiting for swimming, robotics co-captaining for build season? Stuff like that?"
    t neutral "Several schools seem interested in having me. Build season is going well."
    r sad "He means that MIT and Stanford have already talked about wanting to sign him on and that the robotics team is on track to go to Worlds again this year."
    r "And that he's passed his HSK 3 exam for Chinese last month."

    show sabie surprised

    n "Sabie stands up from her seat and plants her hands on the table."
    s "Wait, what the hell? That's a shit ton. Why didn't you say anything?"
    t worried "I thought it wasn't necessary to bring up."
    s annoyed "Well, that's exactly what I wanted you to bring up! Friends always celebrate each other's wins right?"
    t neutral "Um. Sure."
    s neutral "Now, that's the spirit!"
    n "Sabie then whirls on Rohan."
    s annoyed "And you, how did you know about this anyways when this kid over here won't open his mouth?"
    r happy "Uh, my parents?"
    s happy "Oh, right. Sorry I asked."
    s "Your parents are crazy. I don't know how they find the stuff they do."
    r "To be honest, me neither."
    r "It's okay though. I'm kinda numb to it at this point."

    jump lunch_stable_rohan

label lunch_stable_rohan:

    s "I felt that."
    s mischievous "Anyways, how are you? Wanna tell us about your life?"
    r sad "Dammit. I was hoping you'd forget."
    s "Not a chance. So, what do you have to say for yourself?"
    r neutral "Uh, my grades are probably good enough for me to go to the state university for medical school and my classes are kinda interesting?"
    r "...All of the ones except for the STEM ones at least. I hate bio."
    r "Most of my clubs have wound down for the year. We had a full house for our productions all last week, so that was nice."
    r sad "I still haven't done anything for Science Olympiad, though. Or HOSA. Or the Intel Research competition. I need to get on that."
    r neutral "Anyways, I am definitely very tired and looking forward to break."
    n "Rohan gives Sabie a nervous look."
    r "That was it, right? I didn't miss anything, did I?"
    s neutral "That. Was perfect. Exactly what I was looking for."
    n "Sabie points in Tyree's direction."
    s mischievous "You. Take note when I ask you next time."
    t "Okay."

    jump lunch_stable_masami

label lunch_stable_masami:

    s happy "Now, last one."
    s worried "..."
    s "Hey, Masami? You still there?"
    m "Huh?"
    n "Masami blinks and looks up. Everyone at the table is now staring at him."
    m "(Shit. How long have I zoned out for?)"
    s neutral "It's your turn for a group progress update."
    m "Oh."
    n "Masami stares at his hands, a lump forming in his throat."
    m "(Dammit.)"
    m "(Usually I wouldn't struggle with this sort of thing, but these past few days all I can think about is {i}jie{/i} and what she promised - )"
    m "(No. I have to focus. I can't think about that now.)"
    n "Masami looks up again and forces himself to smile, easing his shoulders into a more natural position."
    n "His fingers instinctively fish for a small object in his pocket, latching on tight when they find it."
    m "Well, you guys have already heard most of it before. Robotics pre-season is going well. So is theatre. And badminton, though I’m not getting recruited for that."
    m "Grades and classes are pretty good, though break is also nice."
    m "I…don't really have anything to complain about."
    m "(At least, in the sense that is acceptable for me to say, that is.)"
    r "Sounds like things are going as well as always for you then."
    t "That's good."
    s worried "Yeah, I suppose."
    n "Sabie stares at Masami for a moment longer, as she usually does when she's trying to fish the hesitancy out of him."
    n "Masami's grip tightens on the object in his pocket."
    m "(Shit. She noticed. What now?)"
    s "What about - "
    n "Just then the bell rings, cutting her off. Masami breathes an internal sigh of relief."
    m "(Phew.)"
    m "Looks like that's our cue to leave for class."
    r sad "Yeah, unfortunately."
    r neutral "Are we coming here again tomorrow?"
    s neutral "Yep!"
    s mischievous "Next time, I {i}will{/i} get my hands on those pictures. Just you wait."
    r "Sure, as long as you remember."

    show sabie surprised

    t happy "You won't."
    r happy "Oop."
    s annoyed "Hey!"
    m "He's not wrong."
    m "Anyways, I've really got to run. You know how chemistry is. See you all!"

    show tyree neutral
    show sabie neutral
    show rohan neutral

    r "See you!"
    t "Take care."

    jump lunch_end

# Sabie approaches Masami at the end of lunch in the hallway on the way to class
label lunch_end:

    scene # TODO: Replace with BG!

    n "Masami heads quickly into the building and down the hallway to chemistry."
    m "(Thank God for the indoor heating. I don't know why we sit outside.)"
    m "(Actually, I do know. Sabie is a masochist and we're too dead on the inside to contradict her.)"
    n "His hand twitches and he realizes his fingers are still tightly wrapped around the object in his pocket. After a moment of hesitation, he lets go."
    m "(After all this time, I still cling to an old relic like this. Even though I know it's not going to help me with the situation at hand.)"
    m "(Even knowing it's not going to bring {i}jie{/i} any closer to home.)"
    m "(I'm really some desperate fool, aren't I?)"
    m "…"
    m "(At least the only person who'd bother me for it isn't - )"
    s "{i}Ge{/i}!"
    n "Masami groans inwardly."
    m "(Well. Just when I thought she'd let up on me.)"
    n "Just to spite her, Masami picks up his pace."
    s "Oi! Halt, dumbass!"
    s "Don't make me run after you!"
    m "Hm?"

    show sabie annoyed with moveinleft

    n "Masami glances over his shoulder as if he's just noticed Sabie tearing down the sidewalk at full speed. He dramatically slows to a stop to let her catch up to him."
    m "Heh. Did you really think I wasn't going to wait?"

    show sabie neutral

    n "Sabie shrugs."
    s "Who knows."
    n "She goes up on her tiptoes and sticks out her right index finger to boop him on the forehead."
    s happy "There's still a lot of things going on in there that you aren't telling me, {i}ge{/i}."
    s neutral "Not even after these sixteen {i}long{/i} years of knowing each other."
    m "...And despite that, you're not going to stop calling me {i}ge{/i}, are you?"
    s mischievous "Nah. You being hung up over the fact that it’s \"culturally incorrect\" isn't going to stop me."

    show sabie neutral

    m "Heh. I’m not complaining anymore."
    m "Just thinking about how it’s sort of become \"our thing.\" Kind of like…"
    m "Never mind."

    # The more serious part of the conversation
    s worried "Is everything alright? You've been kind of stuck in that head of yours for days now."
    s "Like {i}stuck{/i}, stuck. The {i}not-just-a-mood{/i}, kind of stuck. You know what I mean?"
    s neutral "Wanna talk about it?"
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
    s worried "It's about Xinyi, right?"
    m "…"
    m "Yeah."
    s neutral "Don't worry so much. She'll be back, I'm sure of it."
    s "You know that better than anyone. Don't you?"
    m "I suppose."
    n "Sabie pats him reassuringly on the shoulder."
    s "Then, take it easy. That's what she'd want for you."
    m "Yeah. I'll try."
    m "(I know that you're just saying these things to make me feel better, but I'll take it.)"
    m "(For now, I guess.)"

    jump lunch_end_invite

# Masami chooses to be vague about the issue
label lunch_end_vague:

    m "Was it that obvious?"
    s neutral "Nah. I don't think anyone else noticed."
    s "Mm, now that I think about it, maybe Tyree did."
    s "Then again, who knows what he does or doesn't notice because he won't say anything."
    m "Well -"
    s happy "But, that's besides the point!"
    s mischievous "You need someone to talk to."
    m "And that person {i}has{/i} to be you. Right."
    s worried "Oh, come on! Who else is qualified enough?"
    m "Well - "
    s neutral "Don't get me wrong, your guy friends are great and all."
    s mischievous "But do you really think that you're going to bring up any of your {i}feelings{/i} with any of them?"
    m "That's - "
    s "And!"
    s "If the problem is what I think it is, if you're not going to be telling me about it, you're not going to be telling anyone at all."
    m "That's…"
    m "That's true."
    n "Masami sighs."
    m "(Damn. Why is it that she's always right about the most annoying things?)"

    show sabie neutral

    n "Sabie puts a hand on his shoulder, tilting her head a little as she looks him in the eyes."
    s "Hey."
    s "I just don’t wanna see you holding things in until you explode."
    s "Let me know when you're ready to talk, alright?"
    m "…"
    m "Alright."
    m "Thanks, Sabie."
    s happy "You got it!"
    m "(It's nice being reminded that someone has my back, but…)"
    m "(Well, it's probably too selfish of me to wish that there is someone who gets me a little better that I could talk to.)"

    jump lunch_end_invite

# Masami denies anything is wrong
label lunch_end_deny:

    n "Masami shrugs."
    m "I guess the schoolwork is getting to me."
    m "And all those extracurriculars, you know?"
    s worried "…If you say so."
    s neutral "Just tell me if you need anything, alright?"
    m "Uh…"
    m "Sure."
    m "(I hate keeping things from her, but she's still…)"
    m "(She's still Sabie.)"
    m "(There's only so much about this that she gets.)"

    jump lunch_end_invite

# Sabie invites Masami to the party
label lunch_end_invite:

    show sabie worried

    n "Sabie stares at him for a moment and blinks a couple of times."

    show sabie mischievous

    n "Then she snaps her fingers."
    s "Oh, I almost forgot! The head of the student council is hosting a Christmas party at his bougie house tomorrow. You should come!"
    s "I'm even dragging Tyree and Rohan along."
    s neutral "Well, Rohan was going anyways, but you get the point."
    n "Masami sighs."
    m "I've already told you that I don't go to parties. Especially not Christmas parties."
    s happy "I know. But you need a distraction."
    n "She waggles a finger mischievously in his face."
    s mischievous "And if someone doesn't give you a good one, you're never going to learn about how nice it is to just live in the moment instead of brooding all the time."
    m "I do not brood."
    s "You do brood. You're doing it right now."
    m "This isn't brooding. This is exasperation."
    n "Sabie waves her hand dismissively."
    s "Same difference."
    s neutral "Anyways. It doesn't hurt to start the weekend a little early, now does it?"
    m "We'll still have class the next day."
    s mischievous "Psh. Teachers know that break starts next week."
    s "They can't give us {i}that{/i} much more grief when finals are in January, can they?"
    m "That's not how - "
    s neutral "Come on. It's just one day."
    s "One singular day."
    s "You can relax, chat up some girls - "
    m "I can't chat up girls - "
    s mischievous "Please, I've seen you in your glory days."
    s happy "You had the stagehands swooning from second hand exposure. And that wasn't even the kiss scene!"
    m "That was in middle school. I run audio now."
    s neutral "Psh, whatever. What I {i}mean{/i} is that you have experience."
    s "Besides, what's the difference between flirting in improv and flirting in reality?"
    m "There is a difference! None of them were - "
    s happy "ALYSSA!"

    jump lunch_end_alyssa

# Alyssa walks on scene
label lunch_end_alyssa:

    m "Wha - "
    n "Masami whirls around to see Sabie waving wildly to an approaching figure at the other end of the hall."
    n "A very familiar figure."
    m "(Shit.)"
    m "(Shit. Shit. Shit.)"
    m "Sabie. What are you - "
    n "Sabie ignores him and starts jumping up and down."
    s "HEY ALYSSA, BESTIE - " # TODO: Add bounce and other movements to this general section!

    show sabie at left with move

    s surprised "Mpmf!"
    n "Sabie lets out a muffled cry of protest as Masami puts a hand lightly over her mouth and yanks them behind a corner."

    show sabie annoyed

    n "As soon as they're safely behind the wall, Sabie bats his hand away."
    s "What the hell was that for? I'm doing you - "
    m "Please. Just."
    n "Masami sighs."
    m "Why is it that you two have to be friends?"
    s worried "Are you questioning my bestie status with Alyssa?"
    m "No! Of course not - "
    m "Ugh, that's not what I meant, but whatever."
    m "I've already told you that I've stopped trying to \"get to know her better.\""
    s mischievous "Uh, you did not tell me that you've stopped trying. You told me it was complicated."
    s happy "Which means you should be trying harder! If someone like me can get on her good side, so can you."
    m "That's…not what I meant by \"complicated.\""
    s worried "Wait, did you already talk to her, piss her off, and not tell me anything because you were embarrassed?"
    m "What? No! I - "

    # Alyssa actually arrives on scene with Nasir in tow
    n "Masami freezes as Alyssa's voice drifts into earshot."
    n "He presses himself further against the wall and motions for Sabie to do the same."

    hide sabie with Dissolve(0.3)

    n "For once, Sabie actually follows through, albeit with a questioning look."
    s "Hey. Wouldn't now be a good - "
    m "Shhh."
    n "Remarkably, Sabie obediently purses her lips and falls silent."
    a "…That was weird. I thought I heard something."
    na "Really? What?" # TODO: Turn this into question marks!
    n "At the sound of the second voice, Masami's stomach drops."
    m "(Damnit. It's Nasir.)"
    m "(Of course he's with her.)"
    m "(I…I'm not jealous that she's such close friends with one of the most…{i}academically{/i} perfect students at our school.)"
    m "(Well, I'm not jealous anymore, at least.)"
    m "(But…)"
    n "Masami sighs."
    m "(This just makes the whole situation so much more awkward.)"
    m "…"
    m "(Sabie, why?)"
    m "(Why do you do things like this?)"
    n "As if on cue, Masami hears Sabie chuckle sheepishly."
    s "Sorry {i}ge{/i}. Guess I didn't account for that little detail."
    m "Mm. Whatever. It's…fine."
    m "(It's not fine.)"
    m "(...I still kind of want to listen into what's going on, though.)"
    m "(But should I?)"

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

    n "Masami shuts his eyes and tries to block out what's going on."

    show sabie at left with easeinleft

    n "Unfortunately, Sabie keeps nudging him."
    s "Pst. Pay attention."
    m "No."
    s worried "But aren't you the least bit curious?"
    m "No."
    s "Don't you want to talk to Alyssa the slightest bit?"
    m "…"
    m "No."
    s mischievous "Aha, I see that hesitation! I know you. I know you want to hear her voice…"
    m "Will you shut up?"
    s happy "Who do you think I am?"
    m "Please?"
    s neutral "Not until you put your eyes in the right place."
    m "Ugh, fine."
    m "I'll pay attention."
    m "But only because I know you won't stop otherwise."

    show sabie mischievous

    n "Sabie rubs her hands together."

    hide sabie with easeoutleft

    s "Good choice. Good choice…"
    n "Masami sighs."
    m "(I'm going to regret this.)"
    n "He peeks over his shoulder as inconspicuously as he can, trying to ignore the blood pounding in his ears and Sabie's triumphant cackling."

    jump lunch_end_nasir

label lunch_end_nasir:

    show nasir at right with Dissolve(0.3) # TODO: Fix as needed!

    na neutral "…Huh. Strange. I don't think I heard that."
    a "Really? That's a first."
    na sad "What do you mean?"
    a "Well, usually you're the one who catches the things I miss."
    na happy "Not really."
    a "Yes, you are."
    n "Alyssa gives Nasir a playful bump on the shoulder." # TODO: Add animation for this!
    a "Come on, Mr. I-Got-Into-MIT-Early-Action. Have more confidence in yourself!"

    hide nasir
    show sabie surprised at left

    n "Sabie exchanges glances with Masami before she leans over to stage whisper into his ear."
    m "I mean, I'm not surprised, but…"
    s "…how does the whole school not know about this yet when he's basically a celebrity?"
    m "Yeah."

    show sabie neutral

    n "Sabie shrugs."
    s "Beats me. Some people are just good at keeping things to themselves."
    m "Unlike you."
    s annoyed "Hey!"

    hide sabie
    show nasir happy at right # TODO: Fix as needed!

    n "In the meantime, Nasir chuckles, though it seems a little strained."
    na "That was luck. You know how college admissions are."
    a "What about being principal cellist of the National Youth Orchestra?"
    a "Or being on the International Physics Olympiad team?"
    a "Or being a nationally ranked Scrabble player?"

    hide nasir
    show sabie mischievous at left

    n "At the last one, Masami feels a nudge on his arm."
    s "Nationally ranked Scrabble player, huh?"
    s "Hey, {i}ge{/i}, maybe you finally have someone that could - "
    m "No."
    s worried "But - "
    m "No. Words with Friends is not Scrabble."
    s "But you still beat me every time by at least 200 points!"
    m "I hate to say it, but you're just not very good."

    show sabie annoyed

    n "Sabie sticks out her tongue at him."
    s "Meanie."

    # Nasir approaches
    n "Masami is about to make a retort when he feels a quick brush against his elbow."

    hide sabie
    show nasir at center

    n "He whirls around to find himself inches away from Nasir's face."
    n "Nasir looks briefly at Sabie before his gaze settles on Masami."
    m "Uh. Hi?"
    na sad "..."
    n "Masami swallows."
    m "(Shit. He definitely heard everything we said.)"
    n "For a moment, the two of them just stand there looking at each other."

    show nasir happy

    n "Then, to his surprise, Nasir's mouth breaks into a warm, encouraging smile."
    m "(???)"
    a "Uh, Nasir?" # TODO: Show Alyssa's sprite here at the edge of right
    na surprised "Huh?"
    a "You still there?"

    show nasir neutral at right with move

    n "Nasir turns sheepishly back to Alyssa, who seemed thankfully oblivious to the fact that Masami and Sabie were standing right behind him."
    na "Yeah."
    n "Masami sighs in relief."
    m "(Thank God he's tall enough to block Alyssa's view of us.)"
    na "Sorry, I saw a magpie outside and got a little distracted."
    a "A magpie? I thought they didn’t live around here."
    a "Or at least, I’ve never seen one that did."
    n "Nasir shrugs."
    na happy "They come by every once in a while."
    na neutral "You’ll find them. If you know where to look."
    a "Ah. Well, I’ll take your word for it."
    na sad "...Alright."
    a "What?"
    na happy "It’s nothing."
    a "Okay then…"
    na neutral "Anyways, what was I saying before?"

    hide nasir with easeoutright

    n "And then, just like that he's gone, swept up in the flow of students meandering down the hall."
    n "Masami's hand flies forward after him in spite of itself."
    m "Wha - W-Wait!"
    m "(What the hell was that about?)"
    m "(Why did he - )"

    show sabie mischievous at center with Dissolve(0.2)

    n "Sabie's giggling snaps him back to the present."
    s "Oo, so somebody does want to play a little Scrabble after all."
    m "I-I did not say that."

    show sabie neutral

    n "Sabie gives him a pat of mock consolation on the shoulder."
    s happy "Aw, it's okay to defend your butthurt little male ego sometime."
    n "Masami sighs."
    m "For the last time. I. Am. Not. Jealous. Of. Him."
    m "Okay?"

    show sabie neutral

    n "Sabie waves her hand dismissively."
    s "Yeah, yeah. You and your complicated everything. You really need to unwind that mind of yours."

    jump lunch_end_party

label lunch_end_party:

    # Back to the party
    s mischievous "Which brings me back to the Christmas party."
    s happy "You should come!"
    m "Ugh. This again?"
    s worried "What do you mean? Can't you appreciate a break when you see it?"
    s neutral "You'll have people you know there. Rohan. Tyree. Me."
    m "Well, yeah. But Rohan and Tyree are probably going to be playing Smash."
    m "And you're going to be - uh. Singing karaoke."
    s worried "Look I understand if you don't want to get drunk with me."
    s "But what's wrong with Smash? I thought you liked playing it."
    m "Uh…I don’t own a console."
    s "But you’ve played it before."
    m "Yeah, but..."
    n "Masami sighs."
    m "Look, I’m not Rohan. I don’t have practice."
    s "Neither does Tyree."
    m "Tyree is Tyree."
    s neutral "Eh, you’re not wrong. No Smash then."
    n "Sabie thinks for a moment."
    s mischievous "Okay. I've got it."
    m "What?"
    s happy "I'll just introduce you to some of my friends who also sit in the corner."
    s "And then you guys can sit in awkward silence together!"
    m "..."
    s neutral "Or play Scrabble or whatever else you nerds do."
    m "Aren't you also a nerd too?"
    s mischievous "Psh, you know what I mean."
    s happy "Anyways, it'll be fun!"
    s neutral "Whaddya say?"
    m "…"
    m "(She's not going to let up, is she?)"
    n "Masami throws his hands up in surrender."
    m "Fine, I'll think about it, okay?"
    m "Satisfied?"

    show sabie happy

    n "Sabie does a fist pump."
    s "Ayy! That's more like it. Glad you came around."
    m "What? That's not what I - "
    n "Before he can finish his sentence, Masami is conveniently cut off by the blare of the warning bell."
    # SEFF: Warning Bell
    s surprised "Shit!"
    s mischievous "Gotta run. Text me later when your answer is yes!"

    hide sabie with easeoutright

    m "Wait, Sabie - "
    m "(And she's gone.)"
    m "…"
    m "(What have I gotten myself into?)"
    m "…"
    n "He pulls out his phone, turning it over in his hands once. After a moment, he slips it back into his pocket."
    m "(I'll figure it out later.)"

    jump masami_home_3

# Scene cut to Masami's car
label masami_home_3:

    m "(I'm home.)"
    m "…"
    m "(It's been three whole hours and I still haven't figured out what I'm doing yet.)"
    m "(I usually wouldn't be too worried about something like this, but…)"
    n "As if on cue, Masami's phone starts buzzing again with new messages."
    m "(…and it's starting again.)"
    n "He sighs and sets his phone silent."
    m "(Finally. Peace and quiet for me to think. Should have done it earlier.)"
    m "…"
    n "Instinctively, Masami's eyes wander back to his car, where a pendant of a magpie hangs from his key ring."
    n "His eyes linger on it for a moment as it sways, before he goes back to staring at his tightly clenched hands."
    m "…"
    m "(Might as well head inside.)"

    jump masami_kitchen_3

# Scene cut to the kitchen
label masami_kitchen_3:

    scene bg kitchen

    n "A pungent aroma fills the air long before Masami reaches the kitchen."
    m "(Looks like we're having curry tonight.)"
    n "He hangs his coat on the rack near the door."
    m "{i}Ma{/i}. I'm home."
    mm "Masami!"
    n "Masami's mother leaves her cooking in an instant to sweep her son up into a warm hug, her eyes twinkling."
    mm "{i}Bagaimana harimu?{/i} Learn a lot today?"
    m "It went well."
    mm "Good, good. You keep working hard, you have good future."
    m "…"
    m "Yeah. I know."
    n "His mother doesn't notice his discomfort as she breaks away to give the pot a quick stir."
    n "Masami's gaze follows her, his expression a pleasant mask once more."
    mm "We have curry tonight. Warm for winter."
    m "It smells really good. Thanks for making it."
    n "His mother beams."
    mm "Of course!"
    n "She gestures towards the refrigerator."
    mm "If you not busy, you can help make {i}tangyuan{/i}. I buy ingredients today."
    m "{i}Tangyuan{/i}? Isn't it a little early to make that? {i}Dongzhi{/i} is in three days."
    n "His mother shifts quietly. Her lips purse briefly before they curve back into a bright smile."
    mm "Ah."
    mm "Not bad to start early, right?"
    mm "You grow up, you eat more! Also, more to save for later."
    mm "I buy sesame. More variety. You ask for that, right?"
    m "…"
    m "Yeah, I did."
    m "I'll get started on making the peanut ones after dinner and freeze them up. Probably should get warmed up with something familiar before I try anything new."
    m "Thanks for remembering."
    mm "You're welcome."
    n "She leans forward to tuck a stray lock of hair behind his ear."
    mm "Stay focused, okay?"
    mm "And remember family. We are always here for you. We stick together."
    m "You've told me that before."
    n "She smiles and pats his shoulder."
    mm "I know. I just don't want you to forget."
    m "…"
    m "Right."
    m "I've…got some homework to do. I'll be back down in a bit!"
    mm "Okay, I call you down for dinner. Remember, stay focused!"
    m "I will!"

    jump masami_room_3a

# Scene cut to Masami's room
label masami_room_3a:

    scene # TODO: Fix me!

    n "The moment that Masami sets foot in his room, he flops down face first on the bed with a groan."
    m "(Ugh…)"
    m "(What a day…)"
    m "(I don't feel like functioning any more.)"
    n "He rolls over onto his back to stare at the ceiling."
    m "(I should be doing homework, but I can't focus.)"
    m "(Sorry, Mom.)"
    m "(Sorry, God.)"
    m "(Sorry, life expectations.)"
    m "(Looks like I'm going to be failing you all today.)"
    n "Masami gently removes a small keychain in the shape of a magpie from his pants pocket, turning it over in his hands."
    m "(Heh. You'd never told me you'd be giving me so much trouble after you left.)"
    m "…"
    m "(Three days from now…)"
    m "(You said you'll be back to give me your answer then.)"
    m "(And I'd promised to give you mine. Even if neither of us had quite figured things out yet.)"
    m "…"
    m "(I don’t know if I’m more afraid of my answer or yours.)"
    m "(And I…I don't think I'm ready to let go of everything.)"
    m "(At least, not like you did, {i}jie{/i}. I'm not as brave as you.)"
    m "(But sometimes, I wonder…)"
    n "Masami sighs quietly to himself and leans over to set the keychain on his desk."
    m "(Maybe Sabie is right. I do need a distraction.)"
    n "He pulls out his phone, thumbing idly through the home screen before he decides to open the messaging app."

    jump phone_3b

# Brings up phone screen of Masami's phone
label phone_3b:

    m "Hey."
    m "I'm going."

    jump masami_room_3b

# Back to Masami's room
label masami_room_3b:

    n "Masami puts down his phone and flops onto the bed beside it."
    n "He can see the lights on the screen seeping into the covers as Sabie’s replies roll in."
    m "…"
    m "(I'll read it later.)"
    n "Masami rubs his eyes and turns to stare at the ceiling again."
    m "(What would you have thought of me if you'd known what I'd done, {i}jie{/i}?)"
    m "(I…hope that you're proud.)"

    jump masami_room2a