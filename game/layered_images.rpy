################################################################################
## Sprites
################################################################################

## Masami's layered image
define masami_glasses = True
layeredimage masami:

    always:
        "Masami/Masami_Base.png"

    group outfit:

        attribute casual default:
            "Masami/Masami_Casual.png"
        attribute party:
            "Masami/Masami_Party.png"
        attribute sweater:
            "Masami/Masami_Sweater.png"

    group mood:

        attribute angry:
            "Masami/Masami_Angry.png"
        attribute embarrassed:
            "Masami/Masami_Embarrassed.png"
        attribute exasperated:
            "Masami/Masami_Exasperated.png"
        attribute happy:
            "Masami/Masami_Happy.png"
        attribute neutral default:
            "Masami/Masami_Neutral.png"
        attribute sad:
            "Masami/Masami_Sad.png"
        attribute surprised:
            "Masami/Masami_Surprised.png"

    if masami_glasses:
        "Masami/Masami_Glasses.png"

## Nasir's layered image
define nasir_blush = False
layeredimage nasir:

    always:
        "Nasir/Nasir_Base.png"

    group outfit:

        attribute casual default:
            "Nasir/Nasir_Casual.png"
        attribute party:
            "Nasir/Nasir_Party.png"

    group mood:

        attribute embarrassed:
            "Nasir/Nasir_Embarrassed.png"
        attribute happy:
            "Nasir/Nasir_Happy.png"
        attribute mischievous:
            "Nasir/Nasir_Mischievous.png"
        attribute neutral default:
            "Nasir/Nasir_Neutral.png"
        attribute sad:
            "Nasir/Nasir_Sad.png"
        attribute surprised:
            "Nasir/Nasir_Surprised.png"

    if nasir_blush:
        "Nasir/Nasir_Blush.png"

## Rohan's layered image
layeredimage rohan:

    always:
        "Rohan/Rohan_Base.png"

    group outfit:

        attribute casual default:
            "Rohan/Rohan_Casual.png"
        attribute party:
            "Rohan/Rohan_Party.png"

    group mood:

        attribute annoyed:
            "Rohan/Rohan_Annoyed.png"
        attribute embarrassed:
            "Rohan/Rohan_Embarrassed.png"
        attribute happy:
            "Rohan/Rohan_Happy.png"
        attribute neutral default:
            "Rohan/Rohan_Neutral.png"
        attribute sad:
            "Rohan/Rohan_Sad.png"

## Sabie's layered image
layeredimage sabie:

    always:
        "Sabie/Sabie_Base.png"

    group outfit:

        attribute casual default:
            "Sabie/Sabie_Casual.png"
        attribute party:
            "Sabie/Sabie_Party.png"

    group mood:

        attribute annoyed:
            "Sabie/Sabie_Annoyed.png"
        attribute happy:
            "Sabie/Sabie_Happy.png"
        attribute innocent:
            "Sabie/Sabie_Innocent.png"
        attribute mischievous:
            "Sabie/Sabie_Mischievous.png"
        attribute neutral default:
            "Sabie/Sabie_Neutral.png"
        attribute surprised:
            "Sabie/Sabie_Surprised.png"
        attribute worried:
            "Sabie/Sabie_Worried.png"

## Tyree's layered image
layeredimage tyree:

    always:
        "Tyree/Tyree_Base.png"

    group outfit:

        attribute casual default:
            "Tyree/Tyree_Casual.png"
        attribute party:
            "Tyree/Tyree_Party.png"

    group mood:

        attribute happy:
            "Tyree/Tyree_Happy.png"
        attribute neutral default:
            "Tyree/Tyree_Neutral.png"
        attribute worried:
            "Tyree/Tyree_Worry.png"

## Xinyi's layered image
layeredimage xinyi:

    always:
        "Xinyi/Xinyi_Base.png"

    group outfit:

        attribute casual default:
            "Xinyi/Xinyi_Casual.png"

    group mood:

        attribute happy:
            "Xinyi/Xinyi_Happy.png"
        attribute neutral default:
            "Xinyi/Xinyi_Neutral.png"
        attribute sad:
            "Xinyi/Xinyi_Sad.png"

## Alyssa's layered image
layeredimage alyssa:

    always:
        "Alyssa/Alyssa_Base.png"

    group mood:

        attribute happy:
            "Alyssa/Alyssa_Happy.png"
        attribute nervous:
            "Alyssa/Alyssa_Nervous.png"
        attribute neutral default:
            "Alyssa/Alyssa_Neutral.png"
        attribute sad:
            "Alyssa/Alyssa_Sad.png"

    group glasses:

        attribute glass default:
            "Alyssa/Alyssa_Glasses.png"

################################################################################
## Glitch Filter
################################################################################

layeredimage glitch_filter:

    group scan:

        attribute normal default:
            "bg/scanlines.webp"

        attribute normal2:
            "bg/scanlinesmellow.webp"

    always:

        "bg/vignette.webp"
