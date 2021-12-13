## DAY 0
# This part doesn't need full voice over
# This part doesn't need full voice over, fully CGs
label tangyuan_cook:

    # Empty setup
    mm "Ready, Masami?"
    m "…Yeah. Let's do this."

    # Toast black sesame seeds in frying pan over low heat
    mm "Careful. Make sure they plump, but not overcooked."
    m "Got it."
    m "…I think they're good now."
    mm "Let me test."
    mm "Mm, it not break between my finger yet. Little bit longer."
    m "Okay."
    m "…How about now?"
    mm "That is perfect."

    # Grind with food processer with sugar into paste, add lard and refrigerate
    mm "Okay, we put in here. Let run for a little bit with some lard."
    m "I think it looks good."
    mm "You want to try?"
    m "Uh, I don't think that - hey! Dad, why'd you eat that?"
    md "Why not?"
    m "It's raw! Aren't you supposed to cook it first?"
    md "It taste good."
    m "Heh. Guess I can't say anything to the guy who ate dirt as a kid."
    m "Why are you laughing all of a sudden, Mom?"
    mm "Nothing. Just happy."
    m "Alright. I'm going to put this in the refrigerator and then we can get started on the dough."
    mm "Flour right here on counter. I put out earlier. I go boil water now."

    # Pour hot water into glutinous rice flour while stirring with a spatula, knead with hands until a smooth, soft dough forms
    m "Perfect, I'll pour it in. Dad, did you heat up the water for the dough?"
    md "Oh. Not yet. I'll go do that."
    m "Dad…"
    md "What? I was busy taste testing. It's an important step."
    m "And what do we learn from it?"
    md "That it will taste good."
    m "Whatever you say."
    md "Haha. Here is water. Anything else?"
    m "One moment, let me get this mixed first."

    # Flatten and wrap with filling in middle, boil in pot
    m "…Alright. I'm done. Could you help me roll these out?"
    md "Okay!"
    mm "You need filling, I put here. Your {i}tangyuan{/i} already made, I go ahead and put in water since it boiling."
    mm "Also, be gentle with dough. Add water if crack, okay?"
    m "Thanks, Mom. Got it."
    md "Are those peanut?"
    m "Yeah."
    md "Can I taste test?"
    m "No."
    md "Okay."
    m "What - Mom. You're laughing again."
    mm "Nothing, nothing!"
    m "Alright, if you say so."
    mm "I take finished one out, put new one in."
    m "Got it! One second, let me - "
    md "Hey! Why you taste test, too?"
    m "Why not? It's cooked."
    md "What's different? The lard just more melted."
    m "I dunno. Some bio stuff probably."
    md "Excuse."
    m "Hey, I’m just saying. I don’t do bio, but I’d rather be safe than sorry, alright?"
    mm "Oh! I think curry is done. I set to simmer. We can eat now if you ready."
    m "Uh, we should be ready. Dad and I should be able to finish the rest of these and freeze them up."
    md "I can finish by myself. You help your mom set the table."
    m "Alright, got it."

    # Set table CG
    mm "Okay, we all ready?"
    m "…Could we wait a little bit?"
    mm "Why?"
    m "Never mind. Let's just go ahead."
    md "Mm, the duck have more ginger than last year."
    mm "Good. You ask for it. {i}Tangyuan{/i} broth sweet enough?"
    md "Yes. Thank you!"
    mm "…Masami?"
    m "Hm?"
    mm "{i}Makan.{/i} You say you want, yes?"
    m "…Yeah. Right. I'll eat."
    mm "Good, good. It good right?"
    m "Yeah. It's very good. I…I like it. We did a good job."
    mm "I'm glad! Family spirit!"
    m "…Yeah. Family spirit."

    jump xinyi_appearance

# Full VO begins here, might need some pause or transition text if the transition is too quick
label xinyi_appearance:

    scene # TODO: Fix me!

    # Shadow appears in window
    m "{i}Jie?{/i}"
    # Shadow disappears
    m "{i}Jie{/i} - "
    m "I saw her out there, I know I did."
    m "But, why can't I seem to move?"
    m "Damn it. I have to - agh!"
    # Visuals/Sound Effects depict him breaking free, he calls after her as he runs

    scene bg nightsky

    m "{i}Jie{/i}! Wait!"
    x "Huh?"
    m "Please, I'm here now - "
    m "Your hands. T-They're like ice. And your face, your hair - " # Gasp at the begin
    m "W-Why are you so cold?"
    x "..." # A sigh
    x "Because I am not truly here."
    m "Huh?"

    jump house_reflect

# Looking back at the house
label house_reflect:

    m "No…"
    x "You are still there, Masami. Where you belong."
    x "And I am where I belong as well."
    x "There is no reason for me to take part in a reunion if I know that I will not stay."
    m "{i}Jie{/i}, I - "
    x "You do not need to feel pity for me. I know what it means to make the choice I did."
    x "If I am to be selfish, I shall be so until the end. And if I have hurt anyone for that decision, I will pay the price for it accordingly."
    m "That…wasn't what I was going to say."
    m "What I meant was, I understand."
    x "…"
    m "Not completely, of course. I still haven't figured out how to use a spray can properly."
    m "But I'm still watching the skies for the same birds as you. Trying to figure out what the hell they've got that makes them able to just {i}be{/i} when the rest of us are still struggling to figure out how."
    x "I suppose you've reached the same conclusion as me, then."
    x "They are just birds in the same way that we are just humans. There is nothing different. Nothing except for belief."
    x "And call that what you will, delusion or self-worth. It does not matter in the end if you cannot find it."
    m "…" # Sigh
    m "I'm not asking for you to change your answer, {i}jie{/i}. I don't think I ever could."
    m "But I - I do have something to ask."
    x "Yes?"
    m "Could you let me hold you?"
    x "I don't see what this will change for either of us."
    m "I - I know. But I want this."
    m "I want to be selfish. If only for a little while. If only for you."
    x "I - I don't want to hurt you more than I already have."
    # Masami starts choking up here
    m "No, {i}jie{/i}, you didn't…you never…"
    m "It was me. Just me. And I..."

    jump ending

# Ending cut scene - fade out Masami/Xinyi after last line
label ending:

    x "Shh…it's okay."
    m "Don't say that. Please don't say that when it's…it's…"
    x "I'm here."
    m "Please…don't…don't…"
    x "I'm still here, Masami. I'm still here."
    m "You’re…warmer now. So warm…"
    m "Don't let go. I don't want to forget you like everyone else. Please - "
    x "I promise."
    m "…" # Choked up sobbing
    x "I promise."

    return

# Idk how to end this thing but it's the ending! :D
