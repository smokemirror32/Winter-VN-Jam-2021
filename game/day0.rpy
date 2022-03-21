## DAY 0

label day0_transition:

    call screen day_change(332, 5, "Day 0") with Dissolve(2.0)
    pause(3.0)

    jump tangyuan_cook

# This part doesn't need full voice over
label tangyuan_cook:

    play music lighthearted fadein 2.0
    scene cg Cooking_Tangyuan_Empty with Dissolve(2.0)

    # Empty setup
    mm "Ready, Masami?"
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "…Yeah. Let's do this."

    scene cg Cooking_Tangyuan_Step1 with Dissolve(1.0)

    # Toast black sesame seeds in frying pan over low heat
    play sound "audio/sound/sizzle.mp3" loop
    mm "Careful. Make sure they plump, but not overcooked."
    m "Got it."
    m "…I think they're good now."
    mm "Let me test."
    mm "Mm, it not break between my finger yet. Little bit longer."
    voice "audio/voice/masami/masami_hm.mp3"
    m "Okay."
    m "…How about now?"
    mm "That is perfect."
    stop sound fadeout 2.0

    play sound "audio/sound/set_down.mp3"
    scene cg Cooking_Tangyuan_Step2 with Dissolve(1.0)

    # Grind with food processer with sugar into paste, add lard and refrigerate
    mm "Okay, we put in here. Let run for a little bit with some lard."
    play sound "audio/sound/blender.mp3"
    pause(6.0)
    m "I think it looks good."
    mm "You want to try?"
    m "Uh, I don't think that - "
    voice "audio/voice/masami/masami_huh.mp3"
    m "Hey! Dad, why'd you eat it?"
    md "Why not?"
    m "It's raw! Aren't you supposed to cook it first?"
    md "It taste good."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "Well, guess I can't say anything to the guy who ate dirt as a kid."
    md "Heh."
    m "Why are you laughing all of a sudden, Mom?"
    mm "Nothing. Just happy."
    voice "audio/voice/masami/masami_hm.mp3"
    m "Alright. I'm going to put this in the refrigerator and then we can get started on the dough."
    mm "Flour right here on counter. I put out earlier. I go boil water now."

    # Pour hot water into glutinous rice flour while stirring with a spatula, knead with hands until a smooth, soft dough forms
    m "Perfect, I'll pour it in. Dad, did you heat up the water for the dough?"
    md "Oh. Not yet. I'll go do that."
    voice "audio/voice/masami/masami_quietsigh.mp3"
    m "Dad…"
    md "What? I was busy taste testing. It's an important step."
    m "And what do we learn from it?"
    md "That it will taste good."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "Whatever you say."
    md "Haha. Here is water. Anything else?"
    m "One moment, let me get this mixed first."

    scene cg Cooking_Tangyuan_Step3 with Dissolve(1.0)

    # Flatten and wrap with filling in middle, boil in pot
    m "…Alright. I'm done. Could you help me roll these out?"
    md "Okay!"
    mm "Be gentle with dough. Add water if crack, okay?"
    m "Thanks, Mom. Got it."

    play sound "audio/sound/set_down.mp3"
    scene cg Cooking_Tangyuan_Step41 with Dissolve(1.0)

    voice "audio/voice/masami/masami_hm.mp3"
    m "Phew, I think that was the last one."
    mm "Your {i}tangyuan{/i} already made, I put here. Add to water when it boiling."
    md "Are those peanut?"
    m "Yeah."
    md "Can I taste test?"
    m "No."
    md "Okay."
    voice "audio/voice/masami/masami_huh.mp3"
    m "What - Mom. You're laughing again."
    mm "Nothing, nothing!"
    m "Alright, if you say so."

    play sound "audio/sound/boil.mp3" volume 0.2 fadein 3.0
    scene cg Cooking_Tangyuan_Step42 with Dissolve(1.0)
    mm "I take finished one out, put new one in."
    m "Got it! One second, let me - "
    md "Hey! I thought you say no taste test."
    voice "audio/voice/masami/masami_quietchuckle.mp3"
    m "Why not? It's cooked."
    md "What's different? The lard just more melted."
    m "I dunno. Some bio stuff probably."
    md "Excuse."
    m "Hey, I’m just saying. I don’t do bio, but I’d rather be safe than sorry, alright?"
    mm "Oh! I think dumpling is done. I set to simmer. We can eat now if you ready."
    voice "audio/voice/masami/masami_oh.mp3"
    m "Uh, we should be ready. I'll help set the table then."

    scene bg black with Dissolve(1.5)
    scene cg Family_Dinner_NoShadow with Dissolve(1.5)

    play sound "audio/sound/plates.mp3"
    queue sound "audio/sound/silverware.mp3"
    mm "Okay, we all ready?"
    m "…Could we wait a little bit?"
    mm "Why?"
    voice "audio/voice/masami/masami_nevermind.mp3"
    m "Never mind. Let's just go ahead."
    mm "..."
    play sound "audio/sound/silverware.mp3"
    md "Mm, the duck have more ginger than last year."
    mm "Good. You ask for it. {i}Tangyuan{/i} broth sweet enough?"
    md "Yes. Thank you!"
    mm "…Masami?"
    voice "audio/voice/masami/masami_huh.mp3"
    m "Huh?"
    play sound "audio/sound/slide.mp3"
    mm "{i}Makan.{/i} You say you want, yes?"
    m "…Yeah. Right. I'll eat."
    mm "Good, good. It good right?"
    voice "audio/voice/masami/masami_hm.mp3"
    m "Yeah. It's very good. I…I like it. We did a good job."
    mm "I'm glad! Family spirit!"
    m "…Yeah. Family spirit."

    jump xinyi_appearance

# Full VO begins here, might need some pause or transition text if the transition is too quick
label xinyi_appearance:

    stop music fadeout 2.0
    scene cg Family_Dinner with Dissolve(3.0)

    # Shadow appears in window
    voice "audio/voice/masami/masami_finalscene_jie1.mp3"
    m "{i}Jie?{/i}"
    # Shadow disappears
    play music finale fadein 2.0
    scene cg Family_Dinner_NoShadow with Dissolve(3.0)
    voice "audio/voice/masami/masami_finalscene_jie2.mp3"
    m "{i}Jie{/i} - "
    voice "audio/voice/masami/masami_finalscene_isawher.mp3"
    m "I saw her out there, I know I did."
    voice "audio/voice/masami/masami_finalscene_whycanti.mp3"
    m "But, why can't I seem to move?"
    show cg Family_Dinner_NoShadow at hpunch
    voice "audio/voice/masami/masami_finalscene_damniti.mp3"
    m "Damn it. I have to - agh!"
    scene bg black with Dissolve(0.1)
    scene bg nightsky
    show masami surprised at mc_pos
    with Dissolve(0.1)
    show bg nightsky at shake

    voice "audio/voice/masami/masami_finalscene_jiewait.mp3"
    m "{i}Jie{/i}! Wait!"

    show xinyi with Dissolve(0.4)

    voice "audio/voice/xinyi/xinyi_huh.mp3"
    x "Huh?"
    voice "audio/voice/masami/masami_finalscene_pleaseimhere.mp3"
    m neutral "Please, I'm here now - "
    show masami sad at shake, mc_pos
    voice "audio/voice/masami/masami_finalscene_yourhandstheyre.mp3"
    m "Your hands. T-They're like ice. And your face, your hair - " # Gasp at the begin
    voice "audio/voice/masami/masami_finalscene_whyareyou.mp3"
    m "W-Why are you so cold?"
    voice "audio/voice/xinyi/xinyi_...1.mp3"
    x sad "..." # A sigh
    voice "audio/voice/xinyi/xinyi_becauseiam.mp3"
    x "Because I am not truly here."
    show masami surprised at shake, mc_pos
    voice "audio/voice/masami/masami_finalscene_huh.mp3"
    m surprised "Huh?"

    jump house_reflect

# Looking back at the house
label house_reflect:

    scene bg black
    hide masami
    with Dissolve(2.0)
    scene cg Looking_Back with Dissolve(2.0)

    voice "audio/voice/masami/masami_finalscene_no.mp3"
    m "No…"
    voice "audio/voice/xinyi/xinyi_youarestill.mp3"
    x "You are still there, Masami. Where you belong."
    voice "audio/voice/xinyi/xinyi_andiam.mp3"
    x "And I am where I belong as well."
    voice "audio/voice/xinyi/xinyi_thereisno.mp3"
    x "There is no reason for me to take part in a reunion if I know that I will not stay."

    scene bg black with Dissolve(2.0)
    scene bg nightsky
    show xinyi sad
    show masami sad at mc_pos
    with Dissolve(2.0)

    voice "audio/voice/masami/masami_finalscene_jiei.mp3"
    m "{i}Jie{/i}, I - "
    voice "audio/voice/xinyi/xinyi_youdonot.mp3"
    x happy "You do not need to feel pity for me. I know what it means to make the choice I did."
    voice "audio/voice/xinyi/xinyi_ifiam.mp3"
    x "If I am to be selfish, I shall be so until the end. And if I have hurt anyone for that decision, I will pay the price for it accordingly."

    show xinyi neutral

    show masami exasperated at shake, mc_pos
    voice "audio/voice/masami/masami_finalscene_thatwasntwhat.mp3"
    m "That…wasn't what I was going to say."
    voice "audio/voice/masami/masami_finalscene_whatimeant.mp3"
    m sad "What I meant was, I understand."
    voice "audio/voice/xinyi/xinyi_...2.mp3"
    x sad "…"
    voice "audio/voice/masami/masami_finalscene_notcompletelyof.mp3"
    m neutral "Not completely, of course. I still haven't figured out how to use a spray can properly."
    voice "audio/voice/masami/masami_finalscene_butimstill.mp3"
    m "But I'm still watching the skies for the same birds as you. Trying to figure out what the hell they've got that makes them able to just {i}be{/i} when the rest of us are still struggling to figure out how."
    voice "audio/voice/xinyi/xinyi_isupposeyouve.mp3"
    x neutral "I suppose you've reached the same conclusion as me, then."
    voice "audio/voice/xinyi/xinyi_theyarejust.mp3"
    x "They are just birds in the same way that we are just humans. There is nothing different. Nothing except for belief."
    voice "audio/voice/xinyi/xinyi_andcallthat.mp3"
    x sad "And call that what you will, delusion or self-worth. It does not matter in the end if you cannot find it."
    voice "audio/voice/masami/masami_finalscene_...1.mp3"
    m sad "…" # Sigh
    voice "audio/voice/masami/masami_finalscene_imnotasking.mp3"
    m "I'm not asking for you to change your answer, {i}jie{/i}. I don't think I ever could."
    voice "audio/voice/masami/masami_finalscene_butiido.mp3"
    m neutral "But I - I do have something to ask."
    voice "audio/voice/xinyi/xinyi_yes.mp3"
    x neutral "Yes?"
    voice "audio/voice/masami/masami_finalscene_couldyoulet.mp3"
    m sad "Could you let me hold you?"
    voice "audio/voice/xinyi/xinyi_idontsee.mp3"
    x sad "I don't see what this will change for either of us."
    voice "audio/voice/masami/masami_finalscene_i-iknowbut.mp3"
    m "I - I know. But I want this."
    voice "audio/voice/masami/masami_finalscene_iwantto.mp3"
    m neutral "I want to be selfish. If only for a little while. If only for you."
    voice "audio/voice/xinyi/xinyi_i-idont.mp3"
    x "I - I don't want to hurt you more than I already have."
    # Masami starts choking up here
    voice "audio/voice/masami/masami_finalscene_nojieyou.mp3"
    m sad "No, {i}jie{/i}, you didn't…you never…"
    voice "audio/voice/masami/masami_finalscene_itwasme.mp3"
    m "It was me. Just me. And I..."

    jump ending

# Ending cut scene - fade out Masami/Xinyi after last line
label ending:

    scene bg black
    hide masami
    with Dissolve(1.0)
    scene cg Masami_Xinyi_Hug with Dissolve(2.0)

    voice "audio/voice/xinyi/xinyi_shhhitsok.mp3"
    x "Shh...it's...it's okay."
    voice "audio/voice/masami/masami_finalscene_dontsaythat.mp3"
    m "Don't say that. Please don't say that when it's…it's…"
    voice "audio/voice/xinyi/xinyi_imhere.mp3"
    x "I'm here."
    voice "audio/voice/masami/masami_finalscene_pleasedontdont.mp3"
    m "Please…don't…don't…"
    voice "audio/voice/xinyi/xinyi_imstillhere.mp3"
    x "I'm still here, Masami. I'm still here."
    voice "audio/voice/masami/masami_finalscene_yourewarmernow.mp3"
    m "You’re…warmer now. So warm…"
    voice "audio/voice/masami/masami_finalscene_dontletgo.mp3"
    m "Don't let go. I don't want to forget you like everyone else. Please - "
    voice "audio/voice/xinyi/xinyi_ipromise1.mp3"
    x "I promise."
    voice "audio/voice/masami/masami_finalscene_...2.mp3"
    m "..."
    voice "audio/voice/xinyi/xinyi_ipromise2.mp3"
    x "I promise."

    window hide dissolve
    pause(3.0)
    scene cg Masami_Xinyi_Hug_BGonly with Dissolve(2.5)

    pause(4.0)

    jump credits # TODO: Fix transition!
