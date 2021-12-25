## DAY 2 - BEFORE
# Masami and Alyssa meet in front of his house
label masami_room_2:

    play music lighthearted fadein 2.0
    scene bg bedroom with Dissolve(2.0)

    m "(Well.)"
    m "(Today's the day isn't it?)"
    m "…"
    m "(I still don't know why I agreed to attend this party.)"
    n "Masami fiddles with the zipper of his jacket, half-listening to Sabie and his mother converse in Indonesian in the kitchen below."
    m "(I can't understand everything they're saying, but I'm pretty sure they're talking about me again.)"
    m "(They always do.)"
    m "(Or at least, my mom always asks and Sabie just goes along with it because she takes an inhumane amount of satisfaction from airing my dirty laundry.)"
    n "He takes one last look over the room."
    m "(Let's see, I've got my keys, my phone…)"
    m "(That should be everything, right?)"
    m "…"
    m "(Yeah, that's everything. I should head out.)"

    jump masami_kitchen_2

label masami_kitchen_2:

    scene bg black with Dissolve(1.0)
    scene bg kitchen with Dissolve(1.0)

    n "Masami heads down the stairs and into the kitchen."
    show wsprite at right
    show sabie party at center
    with Dissolve(0.3)
    n "His mother is scooping the leftover fried noodles from dinner into a large bowl as she chats with Sabie, who stands primly out of the way."
    hide wsprite
    hide sabie
    show msprite at left
    with Dissolve(0.3)
    n "His father is washing the dishes in the corner, silent except for the occasional clack of the silverware and plates against the walls of the sink."
    hide msprite
    show sabie party at center
    show wsprite at right
    n "Sabie notices Masami immediately and waves him over."
    show sabie innocent at bounce
    s "Yo, {i}ge{/i}! Show your mom the outfit I - "
    show sabie annoyed at shake, center
    s "Seriously?"
    m "What?"
    s "Your jacket."
    m "What about my jacket?"
    show sabie at shake, center
    s "You're wearing it. Over the Christmas sweater I picked just for you."
    m "That was exactly the point."
    s neutral "At least, you'll be taking it off at the party, right?"
    m "No."
    show sabie at bounce, center
    s innocent "Aw, come on! I bet someone there {i}really{/i} wants to see you in that beautiful Christmas sweater."
    s "You won't let them down, will you?"
    n "At this, Masami's mom lays the spoon momentarily down in the pot."
    show wsprite at bounce, right
    mm "Masami, this is giving season. We have Christmas, we have {i}Dongzhi{/i}."
    show wsprite at bounce, right
    mm "Holiday spirit! We be with others and be happy."
    n "She pats him gently on the shoulder."
    mm "Sabrina tell me she work hard to find you a good gift. Think about she feel, okay?"
    m "…"
    n "Masami shoots a death glare at Sabie."

    show sabie innocent at bounce

    s "Ehe."
    m "…"
    mm "And I don't want you to overheat in thick jacket. Many people will be there. It will be very hot."
    s mischievous "Oh yeah. It'll be very hot."
    n "Masami sighs and rubs his temples."
    m "Fine, I'll think about it, okay?"
    show wsprite at bounce, right
    mm "Good, good."
    n "Masami's mother hums to herself as she puts a layer of saran wrap over the bowl and puts it in the refrigerator."
    show wsprite at shake, right
    mm "Oh, I almost forget!"
    show wsprite at bounce, right
    mm "Masami make {i}tangyuan{/i} yesterday. Peanut type!"
    mm "Do you want some, Sabrina?"
    m "Uh, Mom, I made those for - "
    s innocent "Oh no, it's fine. I couldn't!"
    mm "Are you sure? We cannot eat all by ourselves."
    s "Yeah, I'm sure. If there are leftovers, I can always come by to pick them up the day after."
    s "But, I think you all will be able to finish everything."
    s neutral "Right, Masami?"
    m "…"
    m "Yeah. I hope so."
    n "Masami's mother purses her lips together, but nods along anyways."
    mm "I keep forgetting Masami is growing boy. He eat much more now."
    n "Her eyes glaze over a little as she worries her hands together. Behind her, the clacking noises of the dishware grow noticeably more quiet."
    mm "He grow so fast."
    mm "One day he will leave for college."
    mm "I wonder if he will come back to see me…"
    s innocent "He will. I'm sure of it."
    n "Masami's mother smiles vacantly and shakes her head."
    mm "I hope. Family stay together important."
    mm "That way we can keep celebrate together. Love together. Stay strong. Year after year."
    n "She pats Sabie on the shoulder."
    mm "Take care of him okay?"
    show sabie neutral at bounce
    s "You can count on me!"
    show wsprite at bounce, right
    mm "Good, good."
    n "She adjusts the apron she's wearing and grins."
    show wsprite at bounce, right
    mm "You two have fun now! Don’t come back too late."
    m "Don't worry, Mom, we won't."
    mm "I know."
    n "She plants a kiss onto his forehead."
    mm "I love you."
    m "Love you too."

    jump masami_kitchen_leave

label masami_kitchen_leave:

    hide wsprite with Dissolve(0.3)
    show sabie at innerright with move
    show msprite behind sabie at shake, left

    n "Masami's dad elbows him as Masami and Sabie head for the door."
    m "Hm?"
    n "Masami's dad just smiles mischievously and leans in to whisper into Masami’s ear."
    show msprite at bounce, left
    md "If you find a girl, make sure to introduce her to us."
    m "What? I never said - "
    md "Okay."
    mm "What's going on?"
    md "Just giving Masami some last minute advice."
    show sabie innocent at bounce
    n "His dad winks at Sabie, who giggles."
    m "Sure. Advice."
    m "(Ugh, remind me never to have the two of them in the same space again.)"
    show sabie surprised at shake, innerright
    n "Masami grabs Sabie's hand."
    s "Hey, what are you - "
    m "We're going now or we're going to be late! Bye!"

    hide sabie with moveoutright # TODO: Figure out scene cheoreography!
    show bg kitchen at hpunch

    n "With that, Masami forcibly drags Sabie out the door with him."

    jump tyree_car

# Inside Tyree's car
label tyree_car:

    scene bg black with Dissolve(1.0)
    scene bg carevening with Dissolve(1.0)
    show sabie party innocent with moveinright
    show sabie at shake

    n "For better or worse, Sabie follows him to Tyree's car without issue, though she is cackling the entire time."
    n "She also doesn't protest when Masami takes shotgun."

    show sabie party at left with move
    show rohan party at right with Dissolve(0.1)

    n "Rohan is already waiting in the back seat, looking rather confused."
    r "What happened?"
    m "Nothing."
    s mischievous "Sure, nothing. Your dad giving me the green light was nothing."
    m "Tell that to my mom. She still thinks we're going to get married some day."
    show sabie neutral at bounce, left
    s "Psh, she'll come around."
    m "Clearly."
    r sad "…"

    hide sabie
    hide rohan
    show tyree party

    n "Tyree chuckles from the driver's seat."
    t "Ready to go?"
    m "Please. I just want to get this over with."
    t happy "You will be fine, don't worry."

    hide tyree

    n "Tyree starts up the engine and turns the radio to some Christmas music."

    show sabie party at left
    show rohan party at right
    with Dissolve(0.1)

    n "After a couple minutes of driving, Masami turns his head around towards the back."
    m "Sabie."
    s "Hm?"
    m "Why am I the only person in this car who is dressed up like this?"
    show sabie innocent at bounce, left
    s "Hey, there's no need to feel self-conscious about it."
    m "I'm not self-conscious!"
    m "I just want to know why you insisted on me wearing {i}this{/i} when I could have just worn what I usually wear."

    show sabie at shake, left

    s worried "Uh."
    s neutral "It's a Christmas party, so I thought you'd like something a little fun!"
    m "You're not answering my question."
    s worried "Uh…"

    show sabie at bounce

    s happy "Don't worry about it."

    show rohan at bounce

    r happy "…"

    hide sabie
    hide rohan
    show tyree party with Dissolve (0.1)

    n "Tyree clears his throat and turns up the music to an obnoxiously loud level."

    hide tyree

    m "(Great. There's something that they all know about and they're not going to tell me a thing.)"
    m "(I just love it when that happens.)"
    n "They ride the rest of the way with the speakers blaring over their silence."

    jump party_living_room

label party_living_room:

    stop music fadeout 1.0
    scene bg black with Dissolve(1.0)
    scene bg partyinsideedit with Dissolve(1.0)
    play music uptempo fadein 1.0

    n "When they arrive at the party, Rohan and Tyree predictably disappear upstairs to play Smash."

    show sabie party
    show bg partyinsideedit behind sabie at hpunch

    n "Masami moves to follow, but Sabie grabs him by the hand and drags him to the kitchen."
    show sabie at bounce
    s "Here."
    n "Sabie shoves a solo cup full of eggnog into his hands."
    s mischievous "For your nerves. Since you'll need a little push to get there."
    m "My nerves? What are you trying - "

    show sabie happy at bounce

    s "Oops, the dance floor calls!"
    s "Talk to you later, {i}ge{/i}! You got this!"

    hide sabie with moveoutright

    m "Sabie, could you please explain - "
    m "(And she's gone.)"
    m "…"
    m "(No use trying to chase her down when she doesn't want to be found.)"
    m "(No way am I getting near those speakers either. I've already got enough hearing damage from doing audio.)"
    n "Masami scans the living room, trying to find a friendly face."
    m "(Hm, I have seen most of these people before at one point or another.)"
    m "(A few people from the stage crew are here. A couple of robotics are people, too, though more of them are probably upstairs playing Smash.)"
    m "(But there's no one here that I - )"
    n "Masami freezes as he notices a small group of people sitting on the living room couch."
    m "(Shit. It's Alyssa.)"
    m "(I didn't expect to see her here.)"
    m "(I mean, I shouldn't be surprised since half the upperclassmen in the school are here.)"
    m "(But she's not the party type. Or, not at least that I know of.)"
    m "(Besides, wouldn't Sabie have - )"
    m "(Wait a second.)"
    n "He stares down at his jacket, already starting to feel warm as the realization dawns on him."
    m "(Dammit.)"
    m "(I should have stayed home today.)"
    m "…"
    m "(Then again, I did ask for this distraction.)"
    m "(...And knowing {i}jie{/i}, she would have wanted it for me, too.)"
    n "He sighs quietly."
    m "(Either way, I'm stuck here.)"
    m "(Probably should find some way to kill time while I'm at it.)"

    jump party_living_room_explore

# Explore the living room
label party_living_room_explore:

    call screen party

# Check Upstairs
label party_upstairs:

    $ alyssa_visit_first = False
    $ upstairs_check = False
    m "(They're probably playing Smash up there in the game room.)"
    m "(I could always go watch them.)"
    m "…"
    m "(Yeah, still no.)"
    m "(They're going to force me into the rotation if I go.)"

    jump party_living_room_explore

# Investigate the Kitchen
label party_kitchen:

    $ alyssa_visit_first = False
    $ kitchen_check = False
    m "(They're making some gingerbread cookies. I don't think they want me back there for that.)"
    m "(I'm no Rohan in the kitchen.)"
    m "(They smell really good, though. Maybe I'll have one later.)"

    jump party_living_room_explore

# Masami decides to chat with Alyssa
label party_alyssa_contemplate:

    $ alyssa_visit_first = True

    n "Masami sneaks another glance at the pocket of the room where Alyssa is."
    m "(I know I was set up for this, but…)"
    m "(I could go talk to her. I know the people with her and they seem pretty nice.)"
    m "(Nasir isn't there either.)"
    n "An odd lump forms in Masami's throat at the last thought. He forces it down."
    m "(This could be my chance.)"
    m "(This was what I wanted, didn't I?)"
    m "…"
    n "He stares at the drink that Sabie had unceremoniously pushed into his hands."
    m "(For my nerves, huh?)"
    m "(Probably means it's spiked.)"
    n "He chuckles to himself as he gives the eggnog an absentminded swirl."

    menu:

        "Drink the eggnog":
            jump party_eggnog_drink

# Masami drinks the eggnog
label party_eggnog_drink:

    m "(Couldn't hurt to try a little.)"
    n "Masami takes a tentative sip."
    m "(Yup, it's spiked.)"
    m "(It's…not bad, though. Probably because it's not straight up alcohol.)"
    n "He takes another sip. Then another."
    m "(Ah, to hell with it. Might as well go all the way.)"
    m "(I've already made enough bad decisions today. What more could this do?)"
    n "Without giving himself a moment to think about the consequences, he downs the rest of it in one go."
    m "…"
    m "(I…)"
    m "(I'll probably regret this later, but whatever.)"

    jump party_alyssa_chat

# Masami goes to chat with Alyssa
label party_alyssa_chat:

    n "Masami makes his way through the throngs of people towards where Alyssa and her friends are sitting."

    show alyssa nervous
    show msprite behind alyssa at left
    show wsprite behind alyssa at right
    with Dissolve(0.3)

    n "As he gets closer, he notices their voices grow increasingly hushed, their eyes flitting between Alyssa and Masami. Alyssa herself has gone stock still, her face the faintest shade of red."
    m "Um, hi. Alyssa?"

    show alyssa happy at bounce

    a "Ah! Yeah. That's me."
    a neutral "And you're Masami, right?"
    m "Mhm."
    m "(Great. Why can't I do words today?)"
    m "So, uh. What brings you here?"
    show msprite at shake, left
    n "Alyssa just stares until one of her friends elbows her."
    show alyssa nervous at bounce
    a "Oh! I, uh - "
    n "She giggles nervously."
    a happy "Actually, I wasn't planning on coming, but Nasir kind of insisted I did."
    m "Wait, what?"
    a neutral "Yeah, I know. Me too. Usually, I'm the one who drags him out to go do things."
    a "He's probably off in a corner somewhere trying to get some peace."
    m "Heh. Sounds like me and Sabie. Except Sabie was the one who dragged me here this time."
    a happy "I see. Well, I'm glad she did."
    m "You are?"
    a nervous "Uh, I - "
    n "Alyssa gives a slight cough."
    show wsprite at bounce, right
    n "The other one of her friends giggles and whispers something into the ear of the first friend. They both laugh."
    show msprite at bounce, left
    fa "She is. She's just shy about it."
    show alyssa at shake, center
    a "I am not shy about it! Masami and I are, well. Meeting for the first time."
    show msprite at bounce, left
    fa "Sure. We all know you've been giving him googly eyes since middle school."
    n "Alyssa's face turns bright red."
    show alyssa at shake
    a "What? No! I did not."
    show wsprite at bounce, right
    fb "You saw him once on stage and were instantly smitten. Wouldn't stop talking about him since."
    show wsprite at bounce, right
    fb "\"He's so smart\" this and \"he's so nice\" that."
    show wsprite at bounce, right
    fb "\"He can do the arts and sports and STEM. A triple threat!\""
    show wsprite at bounce, right
    fb "\"He's the perfect one to walk me down the aisle and have my babies.\""
    show alyssa at shake
    a "I-I did not say that! Not the last one at least."
    show msprite at bounce, left
    fa "You basically did."
    show wsprite at bounce, right
    fb "Yeah, you did."
    fb "Anyways, she framed you as the perfect, good-at-everything-guy who could do no wrong."
    n "The friend snickers."
    show wsprite at bounce, right
    fb "Ah, young love!"
    n "Masami feels his throat constrict. He takes a step back."
    m "Oh."
    show alyssa at shake
    n "Sensing his discomfort, Alyssa shifts and throws up her hands as if to shield herself."
    a "N-No! It's not like that."
    a "I-I talk about Nasir like that, too! It's the same thing."
    show msprite at bounce, left
    fa "You tell him that to his face. But you don't do the same thing to Masami. There's a difference."
    a "I - I…"
    show alyssa sad at shake
    n "Alyssa whirls on her friends."
    a "Ugh, just look how uncomfortable you're making him!"
    n "Both of her friends exchange glances then look at Masami. The more outspoken of the two laughs nervously."
    show wsprite at bounce, right
    fb "I thought we made it clear we were exaggerating?"
    show msprite at bounce, left
    fa "Yeah. At least I thought we were."
    show wsprite at bounce, right
    fb "But she does think very highly of you."
    show msprite at bounce, left
    fa "For sure."
    a happy "You did realize all that. Right?"
    m "…Of course. I did."
    m "I mean, I think well of you, too, Alyssa. Really."
    m "…"
    n "Masami looks away briefly."
    m "I - I'm probably going to grab something to drink. Then head upstairs and play Smash or something."
    m "It was nice chatting with you, though."
    a neutral "Yeah. I guess I'll see you around then?"
    m "Of course. See you!"

    hide alyssa
    hide msprite
    hide wsprite
    with Dissolve(0.1)

    n "Masami makes the quickest polite exit he can to the kitchen."
    n "He can hear Alyssa berating her friends as he fills his cup up with another round of eggnog."
    m "(That was rude of me. I should have stayed.)"
    m "(Right?)"
    m "…"
    n "Masami unceremoniously downs the whole cup in one go."
    m "(Ugh, I don’t want to think about this.)"
    m "(And it's so hot in here. That's not helping either.)"
    m "(I need…air. Yeah, that's what I need. I'll just head to the back porch for a little while. That should help.)"

    jump party_porch_initial

# Masami heads to the porch and finds Nasir
label party_porch_initial:

    stop music fadeout 1.0
    scene bg black with Dissolve(1.0)
    scene bg partyporch with Dissolve(1.0)
    play music lighthearted fadein 1.0

    n "He stumbles his way out the back door, hanging his coat on the rack nearby."
    n "A gentle winter breeze greets him as he steps outside. The door swings shut behind him, turning the roaring chatter of the party into a muted thrum."
    m "(Ahh…that's so much better.)"
    m "(Peace. Quiet. And no one to see me in this stupid sweater - )"
    n "Masami freezes at the sound of a sudden rustling behind him. He whirls around."
    m "Wha - "

    show nasir party

    n "There, sitting by the table with an empty solo cup and a plate full of gingerbread cookies is Nasir."
    m "(Oh. So that's where he went.)"

    show nasir party happy at bounce

    n "To Masami's surprise, Nasir gifts him another warm smile like the one from the day before."
    n "Except, this time, the smile has an odd vulnerability. The sight of it makes something in Masami's chest twist."
    m "(That's…weird.)"
    n "He gives his head a shake. His mind remains perfectly fogged."
    m "(Guess I'll make things easier on the both of us and just apologize and leave before things get too awkward - )"
    na mischievous "Ah, hello there, magpie. Didn't expect to see you out here so early in the night."
    n "Masami feels his face heat up in spite of himself."
    m "Magpie? Seriously?"
    m "Am I still some bird to you?"
    m "If you wanted to insult me properly, you should - "

    show nasir party happy at bounce
    $ nasir_blush = True

    n "Masami's stops when he hears Nasir's embarrassed laughter."
    m "What?"

    na embarrassed "Sorry, I should have known better than to call you something like that, but I couldn't help myself."

    na neutral "The look on your face was priceless. Still is."

    $ nasir_blush = False

    m "Really now. You have the guts to say that to someone you hardly know."
    na sad "Actually, I usually wouldn't have the courage to say anything at all."
    n "Nasir's gaze falls to his empty solo cup as he traces the rim with his finger."
    na happy "I guess I have a little push from the eggnog to thank for that."
    na "Softens the blow for experiments that fail more often than not."

    show nasir party neutral

    n "At this, his smile deepens into something more self-loathing, as does the tightening wrench in Masami's chest."
    n "Masami forces himself to stare at the bridge of Nasir's nose to keep himself from turning bright red."
    m "(This. Is. Not. What. I. Think. It. Is.)"
    m "…"
    m "(Damn the alcohol.)"
    n "After a moment, Nasir lifts his hand off the cup and looks back towards Masami, his expression placid once more."
    na "Don't worry. I do know who you are, Masami."

    show nasir happy at bounce

    na "With all of the stories I've heard about you, I'm glad we finally have the chance to talk."

    show nasir party neutral

    m "Huh? Stories?"
    m "You must be joking, right? I fail to see how I'm interesting enough to have stories told about me."
    na mischievous "Apparently Sabie would disagree."
    m "You're friends with Sabie?"
    na neutral "Who isn't?"
    m "Fair enough."
    n "Masami sighs and rubs his temples."
    m "I don't even want to know what she's been telling you."
    na "She hasn't told me very much. Just a couple things here and there about you and Alyssa."
    m "That was exactly what I'd hoped you wouldn’t say."
    m "…"

    jump party_porch_alyssa

label party_porch_alyssa:

    m "Ugh. You were helping Sabie plan this whole thing, weren't you?"
    m "That's why you weren't inside with Alyssa."

    show nasir happy at bounce

    na "Heh. Observant aren't you?"

    show nasir party neutral

    n "Masami shrugs."
    m "It's the only logical conclusion."
    na "Fair."
    na "But, yes. Sabie and I did arrange this."

    stop music fadeout 2.0

    m "Why would you even agree to do that in the first place? I thought you and Alyssa were close."
    m "Wouldn't I get in the way of that?"

    show nasir party sad
    play music emotional fadein 1.0

    n "Nasir looks away for a moment."
    na "…"
    na "To be honest, I'm not sure I know the answer to that either."
    na neutral "But Alyssa likes you and is open to a relationship. Once she gets to know you a little better, of course."
    na "And if that's how she feels, I'll do what I can to see it through."
    m "…"
    m "All this time, I thought you were being possessive or something when you're just self-sacrificing doormat."

    show nasir party happy

    n "Nasir chuckles."
    na "As her very platonic friend, I do want the best for her, after all."
    na sad "Even if that means putting aside my own feelings on the matter."
    m "…"
    na neutral "By the way, I saw you spoke with her just before this. Did you two have a nice chat?"
    m "Yeah, I suppose."
    m "Until I just sort of left."

    show nasir surprised at shake

    na "..."
    m "Yeah, I don't know what I was thinking, either."
    m "This was supposed to be what I've wanted for years and I just…"

    show nasir sad

    n "Masami stares at the ground."
    m "Damn, I really don't know."

    show nasir neutral

    n "Something plastic bumps against Masami's arm. He looks up to see Nasir holding out a plate of gingerbread cookies."
    na "Want some? Before I take the rest."
    m "Uh…"

    menu:

        "Take some":
            $ take_cookie = True
            jump party_porch_cookies_take
        "Refuse":
            $ take_cookie = False
            jump party_porch_cookies_refuse

# You take the cookies
label party_porch_cookies_take:

    m "Sure. Thanks."

    show nasir happy at bounce

    na "No problem! Happy to share."

    show nasir party neutral

    n "Masami takes two cookies from the plate and pops them into his mouth."
    m "These are really good. Real ginger."
    na "Heh. I like that part, too. They go quite well with the eggnog."
    m "Ugh, no need to remind me of my bad decisions."

    $ nasir_blush = True

    na sad "…My apologies. I often forget that self-deprecation isn't a two way street."
    m "I wasn't - "
    na neutral "I was referring to myself."

    $ nasir_blush = False

    m "Oh."

    jump party_porch_reflection

# You refuse the cookies
label party_porch_cookies_refuse:

    m "No thanks, I'm good."
    na "No worries. Just wanted to make sure I wasn't keeping them all for myself if you wanted any."
    n "Nasir sets down the plate on the table."

    jump party_porch_reflection


label party_porch_reflection:

    n "The two of them lapse into an awkward silence as Nasir finishes off the remaining cookies."
    na happy "You don't have to feel obliged to keep me company with conversation. We do, as you've said, hardly know each other."
    m "No, it's fine. You deserve an explanation anyways since you're friends with Alyssa and all."
    $ nasir_blush = True
    na sad "I wouldn't say I deserve it."
    na neutral "But if you want to share, I'm open to listening."
    $ nasir_blush = False
    m "…"
    m "Well, this is going to sound really bad."
    m "But honestly? I'm not sure how I feel about Alyssa anymore."
    na sad "What do you mean?"
    m "Don't get me wrong! I - I didn't mean it in a bad way."
    na neutral "No worries, I understand."
    n "Masami sighs."
    m "Thanks."
    m "I mean, she's still smart. Funny. Incredibly, incredibly sweet. All the things I first thought about her when we first met in sixth grade."
    m "But lately, I've been starting to wonder. Do I actually still like her that way?"
    m "Or have I been clinging to the feeling of always liking her because that's the only thing I know?"
    m "And I'm too scared to think otherwise?"
    na sad "…"
    m "Sorry. I've…just had a lot of things on my mind that I'm still trying to sort through."
    na neutral "That's alright. We've all been there."

    jump walk

# Nasir suggests to take a walk
label walk:

    na "Want to take a walk?"
    m "…What?"
    na "There's a greenway around here and I've found that bit of oxygen helps to clear the mind."
    $ nasir_blush = True
    na embarrassed "At least, that's what I've found works for me."
    show nasir neutral
    m "Yeah, I know. It works for me, too. But the last time I went out for a walk this late…"
    $ nasir_blush = False
    na sad "Did something bad happen?"
    m "I guess you could say that."
    m "(It's kind of hard to explain that I've only gone out at this time of night with my sister.)"
    m "(And she's not here anymore to share this moment with me, so this feels…)"
    m "..."
    na neutral "Well, we can be back before the party ends, if that's what you're worried about."
    na "And, if we go together, we can keep an eye out for each other. Make this experience a good, new one for the both of us."
    na "What do you say?"
    m "I - "
    m "…"
    m "I'll go."
    m "I probably need it."
    m "(I think {i}jie{/i} would have wanted me to do it, too.)"

    show nasir happy at bounce

    na "Great! Let's head out."

    jump walk_woods

label walk_woods:

    scene bg black with Dissolve(1.0)
    scene bg woods
    show nasir party
    with Dissolve(1.0)

    n "Nasir dumps his trash into the bin on the porch, while Masami waits at the edge of the steps, his own cup still at hand."
    n "Then, they walk down the path together."
    n "For someone of his height, Nasir walks with a surprisingly contemplative gait."
    n "His gaze lingers between the bare, frost-bitten branches of the trees as if committing them to memory."
    n "Masami concedes himself to shuffling awkwardly by his side, glancing apprehensively at Nasir's serene expression every so often."
    m "(Silence doesn't seem to bother him, does it?)"
    m "(Not like it bothers me, at least.)"
    m "…"
    m "(I can't stand anymore of this.)"
    n "Masami clears his throat as politely as he can."
    m "So. Uh. Sorry again wasting you and Sabie's efforts. And for keeping you from the party."

    show nasir party surprised at shake
    $ nasir_blush = True

    n "Nasir's head whips around, clearly startled."
    m "(Agh. That was smooth. Real smooth.)"
    na "What?"
    na happy "Oh, you don't need to worry about that. I don't mind. Parties don't suit me, anyways."
    $ nasir_blush = False
    na neutral "And I don't think you need to worry about Sabie, either. I'm sure she'll be glad that you've figured some things out for yourself."
    m "Eh. Maybe. Eventually."
    na "Hey, at least you have someone like her who worries about you."
    m "So she tells me."
    na happy "Heh. It's how you know she's a keeper."
    na neutral "A light to your world, if you will."
    m "I guess."
    n "Masami stares at his hands, watching as they tighten around the empty solo cup they're holding."
    m "But sometimes…the light isn't what you're looking for."
    m "Its brightness, its warmth, its, well, everything is taunting. It only displays the part of you that everyone else wants to see."
    m "Puts you on a pedestal for everyone to blindly admire."
    m "Which makes the parts decaying inside of you that it doesn’t reach feel all the more broken. Especially to yourself."
    n "The bend marks in the red plastic begin to whiten between Masami's fingers, contorted beyond the point of return."
    n "He barely notices."
    m "You want to smother the light, shove it as far out of the way as you can, because the sight of it makes you sick."
    m "It reminds you that you have no right to complain when you were blessed to appear so favorably in the eyes of others."
    m "That things are so much better for you than you have the right to deserve."
    m "But you also can't bring yourself to destroy it, because a part of you still longs to simply be what others see of you."
    m "So you just leave the light there."
    m "Let your thoughts about it fester."
    m "And, well. I haven't figured out what happens after that."
    na sad "…"
    m "Shit. That was so cringe."
    m "Sorry, forget that I ever - "
    na neutral "No need to apologize."
    n "Nasir's gaze drifts to the tree branches again."
    na sad "I get that. That's how I feel with Alyssa, too."
    m "Oh."
    n "Masami tosses his demolished solo cup into one of the trash cans along the trail."
    n "The two of them lapse back into silence, which has now become heavier than before."
    m "(Damn it. I messed up.)"
    m "(I need to lighten the mood with a different subject. But what?)"

    jump walk_woods_convo

# Conversation topics
label walk_woods_convo:

    menu:

        "Ask about Nasir's family":
            jump convo_family

        "Ask about Nasir's hobbies":
            jump convo_hobbies

        "Ask about Nasir's friendships":
            jump convo_friendships

# About Nasir's family
label convo_family:

    m "So, what's your family like? Got any siblings?"
    na neutral "I have a younger sister. She's two years below you, actually."
    m "Really? What's her name?"
    na "Sahar. I don't think you two would have met, though."
    m "Yeah, I don't think we have."
    na "Hm. Perhaps I should introduce the two of you sometime."

    show nasir happy at bounce

    na "I think you'd like her."
    m "What makes you say that?"
    na neutral "Well, she's a bit of a free spirit. She loves songwriting if that's an indicator for you. I'm hoping she can pursue it further one day."
    na "She's also a wonderful dungeon master for D&D."
    m "I've actually never played D&D, but it sounds fun."
    na "It's not my cup of tea, but it's definitely something that you should try at least once if you get the chance."
    m "That's fair."
    na "I should also warn you that she's, how do I put it, very straightforward and opinionated. Perhaps to a fault."
    m "What do you mean?"
    na sad "Well, let's just say that my parents can be a bit overbearing."
    na "It doesn't affect me as much since I conform to their demands rather easily. But sometimes I do worry for my sister, especially when I head off to college."
    na neutral "I have faith that they'll figure things out, though."
    m "Yeah…"

    jump convo_recognition

# About Nasir's hobbies
label convo_hobbies:

    m "What do you do for fun? Besides the extracurriculars everyone talks about you doing."
    m "Unless that is your fun, of course."
    na neutral "Hm, I do enjoy what I do."
    na sad "But it does get tiresome at times. Especially when it comes to the viola."
    m "Child prodigy syndrome?"
    na "I suppose so."
    m "How about Scrabble?"

    show nasir happy at bounce

    na "Oh, that is most certainly for fun."
    m "So you like words, then."
    na neutral "I guess you could say that. Though that's not the quite appeal of it to me. Scrabble is really a math puzzle if you think about it."
    m "Math. Interesting."
    na "Why ask? Do you play it as well?"
    m "Uh, I play Words with Friends sometimes. Not the same thing."
    na "It's similar enough that the skills should carry over."
    m "Well…it's more of the timer issue that gets me."
    na "Then we'll play untimed."

    $ nasir_blush = True
    na embarrassed "If you're open to playing with me, that is."

    show nasir party neutral
    $ nasir_blush = False

    m "Uh…"
    m "Sure. Why not."
    m "But don't expect anything much out of me."

    show nasir happy at bounce

    na "That's alright. I appreciate having new partners. There's always something you can learn from them."
    m "If you say so."

    show nasir party neutral

    jump convo_recognition

# About Nasir's friendships
label convo_friendships:

    m "So, how did you and Alyssa meet?"
    na neutral "We were in the same youth orchestra since elementary school."
    m "Ah, the classic childhood friends scenario."
    na "You could say that."
    na sad "It's not very interesting, I'm afraid."
    m "I'm sure you've got plenty of stories."
    na neutral "Rather mundane ones, but yes, I suppose I do."
    m "How about Sabie, then?"
    na "We were at the same table for Physics last year."
    m "Oh yeah. She mentioned that you carried her through that class. She really hates the subject."
    na "I don't blame her. The class wasn't exactly well taught."
    $ nasir_blush = True
    na embarrassed "If I'm being honest, I wasn't really paying attention either. I was playing Genshin."
    m "…"
    na happy "You're allowed to judge me."
    $ nasir_blush = False
    m "I really can't. Did Alyssa get you into it?"
    na neutral "Actually, I was a day one player of my own volition. But I do co-op with Alyssa and Sabie. Do you play as well?"
    m "No, though Sabie wants me to try. She insists that I'd really like the \"edgy, emotionally repressed dude\". Whatever that means."

    show nasir happy at bounce

    na "Heh. I think I'd agree with her on that one."

    show nasir party neutral

    m "…Not sure what to make of that, but okay."

    jump convo_recognition

# Masami recognizes where they're going
label convo_recognition:

    stop music fadeout 2.0

    n "Suddenly, Masami's eyes widen."

    play music reflective fadein 2.0

    m "Wait. I've been here before."

    show nasir surprised at shake

    na "You have?"
    m "Yeah. I think so."
    m "If we take a left beyond that tree right there. Holy shit - "
    n "Masami breaks into a run."

    show nasir at shake

    $ nasir_blush = True
    na "Masami, please, slow down, I can't - "
    n "Masami doesn't notice and continues sprinting full speed ahead."

    jump walk_splace

# Finding the special place
label walk_splace:

    scene bg black with Dissolve(1.0)
    scene bg railcars with Dissolve(1.0)

    n "A couple minutes later, he reaches the clearing and slows to a stop."

    show nasir party with moveinleft
    show nasir at shake

    n "Nasir comes up behind him shortly after, very much out of breath, but somehow relatively composed otherwise."
    m "Wow. It's still here."
    na "What is - "
    $ nasir_blush = False
    na surprised "Oh. Damn."
    m "Yeah. This…"
    m "…"
    m "This is the place where my sister used to take me."
    m "Well, one of the places. But we'd come here the most."
    m "I haven't been back since she disappeared three years ago, but…"
    na neutral "Want to show me around?"
    m "…"
    m "Sure. I'd like to."
    m "({i}Jie{/i} wouldn't mind, would she?)"

    jump walk_splace_explore

# Exploring the special place - all of this is unsprited
label walk_splace_explore:

    hide nasir

    if (graffiti_check or car_check or tracks_check):

        call screen railcar

    else:
        jump walk_splace_climb

# Explore the graffitti - unsprited
label walk_splace_graffiti:

    $ graffiti_check = False

    m "That's one of my sister's magpies. She took to them like Reminisce took to horses, if you know what I mean."
    na "Reminisce?"
    m "Oh. She was a well known writer back in the 90s. A graffiti artist, I mean."
    na "Ah, I see."
    m "I'm surprised no one's painted over it, yet."
    na "I don't blame them. It's beautiful."
    m "Yeah, she's always been good at that sort of thing."
    na "I can tell."
    na "Are any of these yours?"
    m "Me? Heh, no."
    m "My sister definitely handed me the can more times than I can count. Even offered to help me out, but I never quite got the courage to tag anything."
    m "I kind of wish I had now."
    na "Well, it's not too late to start."
    m "I guess. But…"
    na "It wouldn't be the same?"
    m "Yeah. Kinda stupid, but that's the reason."
    m "I also don't have anything on me, so maybe next time."

    jump walk_splace_explore

# Explore the train car - unsprited
label walk_splace_car:

    $ car_check = False
    m "Sometimes, we used to camp out in here, especially in the winter or rain, when a tent wouldn't be enough shelter."
    na "Ah. Wouldn't it still be rather cold?"
    m "Of course it was. But {i}jie{/i} got some good sleeping bags and a heater, and always insisted that I wear extra layers."
    na "That's still quite a bit. But I suppose that's because I'm not very cold-tolerant."
    m "Eh, you get used to it. Build up the immunity little by little."
    m "The kind of way you'd build up a spice tolerance, if you know what I mean?"
    na "That's true. Maybe I'll try it some day."
    m "You should. I've still got the heater somewhere in my room and I could easily go out to buy some fuel for it."
    m "It's definitely an experience."
    na "You're suggesting that we do this together?"
    m "Well, unless you want me to just hand you the equipment and hope you survive the night."
    na "…"
    m "What?"
    na "Ah, it's nothing."

    jump walk_splace_explore

# Explore the train tracks - unsprited
label walk_splace_tracks:

    $ tracks_check = False

    m "I don't remember anything running on these tracks before. And I don't think anything ever will."
    m "They're rusted beyond repair. I'd be surprised if anyone tries to fix them."
    na "Have you ever thought about what would have happened if something were to come by?"
    m "Yeah. I used to be scared of this place because of that. {i}Jie{/i} almost stopped coming out here because she couldn’t get me to come anywhere near it."
    m "But now? It's just a part of the landscape. Something that was here before me and will likely still be around when I go."
    na "That's quite a poetic way of putting it."
    m "…"
    m "I drank two cups of spiked eggnog. What else am I supposed to say?"
    na "Heh, don't worry. I'm not complaining."
    m "…"

    jump walk_splace_explore

# On top of the car
label walk_splace_climb:

    show nasir party neutral with Dissolve(0.5)

    n "Nasir makes a slow loop around the train car. Masami lingers behind, watching."
    na "This is...facinating. Is there anything else you'd like to show me?"
    m "Not that I can think of."
    m "...Well, actually, there is one more thing. If you're up for it."
    n "A curious burst of daring surges through Masami and he winks at Nasir."
    $ nasir_blush = True

    show nasir surprised at shake

    na "…"
    m "What?"

    show nasir embarrassed at bounce

    na "Nothing."
    $ nasir_blush = False
    na neutral "I'm just intrigued now. What are you thinking?"
    n "Masami gestures to the ladder on the side of the train car."
    m "We climb up and take in the view."

    show nasir surprised at shake

    na "Climb?"
    m "Yeah. It's not too bad. I've done it enough times that I could do it in my sleep. Watch."

    hide nasir

    n "Masami swings himself up the ladder. His limbs are less steady than they once were, but possess all the easy confidence of an old habit."
    n "At the roof of the car, he eases his legs over the edge into a sitting position and looks down."

    show nasir party surprised

    n "Nasir hasn't budged."
    m "Hey, come on. Where'd all the talk about trying new things go?"
    $ nasir_blush = True
    na embarrassed "Ah, well."
    n "Nasir nervously runs his fingers through his hair."
    na neutral "The alcohol's probably on its way out of my system, I suppose."
    m "That's bullshit."

    show nasir party surprised

    m "Here."
    n "Masami gets on his stomach and extends a hand out. Nasir just stares."
    na "I - "
    m "Hurry up or I'm going to freeze."
    na embarrassed "Ah. Sorry."
    n "Nasir's warm, trembling fingers immediately wrap themselves tightly around Masami's cold, stiff ones."
    n "His eyes cling to their clasped hands like a lifeline as he slowly makes his way up the ladder, one hand on holding onto Masami's extended one, the other on the freezing surface of the ladder."
    n "When Nasir reaches the top, he shuffles into a spot about a foot away from Masami, lowering his feet hesitantly downward to dangle freely."
    n "He then turns his gaze skyward and exhales softly, his breath a pillowy cloud in the winter air."
    n "Unconsciously or not, he still doesn't let go of Masami's hand, though his grip has loosened into something more tender."
    m "…"
    m "(I…don't exactly hate this.)"
    m "(Guess I'll leave him be.)"

    jump walk_splace_chat

# Leaving this part unsprited!
label walk_splace_chat:

    scene bg nightsky with Dissolve(1.0)
    $ nasir_blush = False

    n "Masami looks up, taking in the night sky."
    m "You really like the silence thing, don't you?"
    na "Hm? Oh. I suppose I do."
    m "Doesn't it bother you at all?"
    na "Not really, no. But if it does make you uncomfortable, I can try to help fill it."
    m "It's fine. It's just…"
    m "Well, for me at least, every time there's silence, it means that something is wrong."
    na "Oh."
    m "I know, I know. It's such a small thing that it isn't worth complaining about, really."
    m "But it bothers me. Been that way ever since my sister disappeared"
    m "Two days til the anniversary, actually. That's when she said that she'd come back with an answer about whether leaving was worth it."
    na "You're still holding out for her."
    n "Masami exhales quietly."
    m "Yeah. Yeah, I guess I am."
    m "She did leave me with this after all."

    jump walk_splace_charm

label walk_splace_charm:

    scene bg black with Dissolve(0.5)
    scene cg Magpie_Keychain with Dissolve(1.0)

    n "Masami fishes around in his pocket with his free hand for the magpie charm and holds it out for Nasir to see."
    na "Ah. It’s beautiful."
    m "Yeah."
    m "Or at least I think it is. I am biased, after all."

    scene bg black with Dissolve(0.5)
    scene bg nightsky with Dissolve(1.0)

    n "Masami puts the charm away with a sigh."
    m "I…think I'm the only one who still tries to think about her."
    m "Nobody will show it, but to everyone else who knew her, she's basically gone. Even my parents."
    m "But from the way that people talk around her, it's almost like she's still there. Like grating the edge of a wound so that it never heals properly."
    m "I hear it when they talk about how well I'm doing in school. How successful I am and how much more so I will be in the future."
    m "..."
    na "Unlike your sister?"
    m "Basically."
    m "I’m not sure what to make of it all, whether I should follow what the world wants out of me or reject everything like {i}jie{/i}."
    m "In both cases, I know I will feel guilty, like I was coerced into a decision. I know I will question what the point of it all is."
    m "Heh, the grass is always greener on the other side, isn’t it?"
    n "Masami notices that his grip has only been tightening Nasir's hand and lets go with a start."
    m "Ah, sorry. I didn't mean to - "
    na "It's alright. Take it if you need it. I don't mind."
    m "…"
    n "Masami tentatively laces his fingers into Nasir's again. He feels himself flush when Nasir gives him a little squeeze back."
    m "Sorry, I just - "
    na "You don't need to apologize so much. You haven't done anything wrong."
    m "I know, it's another bad habit. Like trying to get used to silence."
    na "Be gentle with yourself. Habits fix themselves with time, once you give yourself space for new ones to grow."
    na "Or at least, that's what I've been trying to tell myself."
    m "I know, it's just - "
    n "Masami sighs again and looks away."
    m "I'm getting there."

    jump walk_splace_magpie

label walk_splace_magpie:

    na "And that's okay. We all are."
    m "Heh."
    na "It's kind of why I look up to magpies."
    na "They're intelligent and represent many things to many people. Some of these things are good and some of these things not so much."
    na "Even so, they innately know who they are. Those external impositions don't matter to them."
    na "It's something that I wish I could say for myself. I'm still looking for it and I do hope I'll get there someday."
    m "{i}Jie{/i} said something similar before."
    na "Ah. It's nice to know I'm not alone in thinking so."
    m "I think she would have liked to know so, too."
    m "You would have liked her."
    m "I just wish she were here so I could introduce her to you."
    na "Maybe you could tell me about her, then. I know it's no substitute, but I'd still like to get to know her better in some way."
    m "I…would like to. It's been a while since I've talked about her."
    m "But probably on the way back since it's getting late."
    na "That sounds like a wonderful plan."
    na "Er, could you help me back down again?"
    m "Yeah, give me one second."

    jump walk_end

label walk_end:

    scene bg railcars with Dissolve(1.0)

    n "Masami hops right off the edge before holding out a hand to Nasir."

    $ nasir_blush = True
    show nasir party with Dissolve(0.1)
    show nasir at bounce

    n "After a moment of hesitation, Nasir follows suite. He stumbles on the landing, catching hold of Masami to steady himself."
    m "You good?"
    na happy "I believe so, thanks to you."
    na embarrassed "You really do make it look incredibly simple."
    m "Eh. Just takes a little practice. Nothing that you can't do."
    na neutral "Heh. I’ll take your word for it."
    m "C'mon let's head back. Don't want to keep everyone waiting on us, do we?"
    na embarrassed "Ah, yes. Of course."

    jump party_porch_end

label party_porch_end:

    stop music fadeout 2.0
    scene bg black with Dissolve(1.0)
    scene bg partyporch
    $ nasir_blush = False
    show nasir party
    with Dissolve(1.0)
    play music uptempo fadein 1.0

    n "They make it back to the porch half an hour later. The music inside the house is still cranked up at full blast."
    m "(Phew. At least the party is still going strong or this would have been a bit hard to explain.)"
    m "(Especially to Sabie and Alyssa.)"
    n "Beside him, Nasir shifts."
    na sad "I suppose this is where we part for the night."
    m "Yeah."
    $ nasir_blush = True
    na "I...rather enjoyed conversing with you."
    na embarrassed "Perhaps we could do so again after finals?"
    m "That'd be nice. Let me give you my number so you can get a hold of me."
    $ nasir_blush = False
    na neutral "Ah. Okay."
    n "Nasir pulls his phone out of his pocket and waits as Masami types his number in."
    m "Here you go."

    show nasir at bounce

    na "Thanks."
    m "Well, it was nice chatting with you. I guess I'll see you - "

    stop music fadeout 1.0

    na sad "Wait."

    play music emotional fadein 1.0

    n "Masami feels Nasir lightly catch his wrist. Again, he feels an odd warmth at the touch of skin on skin."
    m "Yeah?"
    $ nasir_blush = True
    n "Nasir swallows, his fingers unconsciously tightening around Masami's wrist."
    na "Remember what I said before about magpies? And not worrying about what others thought?"
    na "Well, I - "
    m "Hold up. Are you trying to justify yourself for calling me a magpie earlier?"
    m "Because I'm most definitely not one. No matter how hard I try, I still care what other people think of me."
    $ nasir_blush = False
    na neutral "I know you're not. Very few people are."
    na "But there are a lot of similarities that I do see in you. Things that I admire very much."
    m "Heh, that's funny. Good joke."

    show nasir party sad

    n "He looks over at Nasir, who has suddenly gone very still and is very much not looking at him anymore."
    m "That was a joke. Right?"
    n "Nasir mumbles something incoherent."

    jump kiss

label kiss:

    m "I didn't hear anything you said."
    $ nasir_blush = True
    na "It wasn't a joke. I stand by what I said."
    n "Nasir's gaze snaps back to look directly back at Masami."
    na neutral "I thought I knew you before, but you still surprised me."
    na happy "It truly has been a pleasure to spend time with you and I can think of no better way that this night could have gone."

    show nasir party neutral

    m "…Um, thanks?"
    m "This is flattering and all but if you want something out of me, then just get to the point and say it."

    show nasir party surprised at shake

    n "Nasir startles for a brief moment."

    show nasir party neutral:
        parallel:
            ease 3.0 zoom 1.1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5

    n "Then, he reaches up to cup Masami's cheek with his free hand, smiling nervously."
    n "Masami freezes, his heartbeat doing double time in his chest. He doesn't pull away."
    m "(What the hell is going on?)"
    na "Before, when I mentioned magpies, I wasn't just referring to you."
    na sad "I was talking about myself as well."
    n "His thumb runs gently against Masami's warming skin, dangerously close to the lip. Masami shivers."
    m "Oh."
    na "We've both done things to safeguard the feelings of our families and friends. We both struggle to define where society's wants end and where our own begin."
    na "I've always been so hesitant to break those boundaries for fear of the consequences, but tonight I wonder, can I allow myself to be selfish? Is it worth the cost to me?"
    na neutral "And I think I have my answer."

    scene bg black with Dissolve(1.0)

    n "Nasir’s hand shifts to cradle the back of Masami’s head. Masami's breath hitches, his eyes fluttering shut."
    n "He can feel Nasir slowly leaning in, giving him more than enough time to respond."
    m "(Shit. Shit. Shit.)"
    m "(This is actually happening.)"
    m "(He's getting closer.)"
    m "(What do I do, what do I do, what do I do - )"

    # Decide whether or not to go for the kiss
    menu:

        "Break away":
            $ kiss = False
            jump kiss_break

        "Let him in":
            $ kiss = True
            jump kiss_decide

# Masami chooses to break off
label kiss_break:

    scene partyporch at hpunch
    show nasir party surprised at shake:
        zoom 1.0

    n "In a panic, Masami pushes Nasir away. Nasir recoils immediately with a soft gasp, visibly stung."
    m "I - I'm sorry, I wasn't thinking, we're drunk and - "
    na neutral "Don't worry about it."
    na happy "The fault is mine. I shouldn't have assumed you felt the same."
    m "No! I just wasn't sure that - "
    na sad "I - I'll head back in."

    hide nasir with moveoutleft
    $ nasir_blush = False

    m "Nasir, wait!"

    jump party_living_room_end

# Masami chooses to kiss
label kiss_decide:

    m "(I - I know what I want. I think.)"
    m "(But is it worth it for me to act an instinct?)"
    m "(For something I don't entirely understand?)"
    m "(Is it worth - )"
    n "Suddenly, Nasir’s lips brush his own, warm and full."

    scene cg Masami_Nasir_Kiss with Dissolve(0.5)

    n "Masami's eyes snap open and he sees Nasir right in front of him, face flushed and eyes shut."
    m "(Holy. Shit.)"
    m "(What just - )"
    m "(What have I - )"

    jump kiss_break

label party_living_room_end:

    stop music fadeout 2.0
    scene bg black with Dissolve(0.5)
    scene bg partyinsideedit with Dissolve(0.5)
    play music uptempo fadein 1.0

    n "Masami catches the screen door before it closes, searching the sea of partygoers frantically for any trace of Nasir."
    m "Damn it. Where the hell did you - "
    show bg partyinsideedit at hpunch
    n "He backs up near the kitchen, colliding right into someone. The victim whirls angrily on him."
    show sabie party annoyed at shake
    s "Watch it, you stupid ass motherfucker! I'm gonna - "
    m "Sabie?"
    s surprised "Huh? How do you know - "
    s mischievous "Oh. It's you."
    s "Having fun chasing your girl around?"
    m "Uh, I've stopped."
    s annoyed "Ah, that's a shame. I put in so much work for you two to be together only for you to ruin everything with your goody-two-shoeness - "

    show sabie surprised at shake

    n "Sabie yelps as someone grabs her firmly by the arm."

    show rohan party at right behind sabie # TODO: Fix positioning!
    show tyree party at left behind sabie
    with Dissolve (0.1)

    n "Masami’s eyes search behind her to find Rohan standing there with a cup of water and a rather pained expression. Tyree lingers on the other side."
    r "Sorry, I should have gone to check on her much sooner or she wouldn’t be like this."
    m "It’s fine. She hasn’t been bothering me for long anyways."
    r happy "Phew, that’s a relief."

    show sabie annoyed at shake

    s "What the fuck are you talking about? I am a grown woman and I sure as hell have not been bothering - "
    r neutral "Yeah, yeah we know. C’mon, Sabie, let’s go upstairs."
    s surprised "Upstairs? I don’t know how to play Smash."
    r "Sabie, I know you do. Just take my spot in the bracket."
    s "But - "
    r "You’ll be fine."

    hide rohan
    hide sabie
    with moveoutright

    n "With that, he half drags her upstairs and away from the eggnog, leaving Masami alone with Tyree."

    jump tyree_chat

label tyree_chat:

    m "Well."

    show tyree party at center with move

    t "Looks like you made it back in time."
    m "Huh?"
    t "I was worried that we needed to send a search party out for you and Nasir since neither of you were picking up your phone."
    m "Shit! I must have forgotten to switch my phone off of silent from yesterday. I am so sorry - "
    m "Wait. How do you know Nasir?"
    t happy "I don’t. I just noticed Alyssa trying to call him after she couldn't find him about half an hour ago."
    t neutral "Don’t worry, I didn’t tell her or anyone else here that you’d left as well. And I’m not planning on telling, either."

    show tyree party neutral

    m "I know you wouldn’t. I trust you."
    n "Masami shifts, feeling the magpie charm in his pocket rub against the fabric of his pant leg."
    m "...You probably pieced together what happened, didn’t you?"
    m "Not like it took much effort to do so after the plans to set me up with Alyssa fell apart."
    t "Does it bother you if I did?"
    m "Less than I thought it would, honestly. I guess it’s because I have a lot of things on my mind right now."
    t "That’s understandable. Take the time that you need to think."
    n "Masami sighs."
    m "Frankly, I’ve tried thinking before. Many times before. But nothing’s come of it."
    m "And now after everything tonight that has happened, I’m even more confused."
    m "Tyree, how the hell do you simultaneously exceed everyone’s expectations and not give a shit about what people think of you?"
    m "Tell me your secret. At this point, I’d give anything if I could learn it for myself. I’m tired of pretending like all the shit in my head isn’t getting to me."
    t worried "Hm. What you described has never been a struggle for me, so I’m not sure how I would be able to explain my secret, if I had one."
    m "Ah. It’s fine, then."
    t "I’m sorry I can’t give you a better answer."
    t neutral "Are there any thoughts in particular that you would like assistance in parsing out, though?"
    m "...I think it would be best if I probably didn’t think about anything right now. I’m just drunk, tired, and rambling. I’ll be fine in the morning."
    m "And I’ve already messed up enough shit today."
    t "Then, how would you like to watch us upstairs for the last couple of rounds of the night? It would be good to improve your spirits."
    m "Is…{i}he{/i} there right now?"
    t "No. I do believe he left with Alyssa shortly before we found you. He seems to have recovered slightly, if you were concerned."
    m "Heh. Of course you noticed."
    m "Alright, I’ll go. Let’s see what Sabie’s gotten herself into."
    m "(At the very least, it’ll keep me from processing everything that happened.)"

    stop music fadeout 2.0
    scene bg black with Dissolve(2.0)

    jump masami_kitchen1
