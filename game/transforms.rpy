################################################################################
## Simple Transformations
################################################################################

##### Defining Shake #####

init python:
    define.move_transitions("shake", 1.7)

transform shake (rate=0.090):
    # xalign 0.5
    linear rate xoffset -15 yoffset 3
    linear rate xoffset 0 yoffset 0
    linear rate xoffset -10 yoffset 2
    linear rate xoffset 0 yoffset 0

##### Defining Bounce #####

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    #repeat

##### Defining Innerright #####

transform innerright:
    xalign 0.6

##### Defining Masami's Position #####

transform mc_pos:
    xpos -225
    ypos 450
    zoom 0.7

##### Defining Transition Text Position #####

transform trans_text:
    xalign 0.8
    yalign 0.8

##### Defining Glitched Transition Text Position #####

transform glitch_trans_text:
    xalign 0.7
    yalign 0.6

################################################################################
## General Glitch Definitions
################################################################################

transform chromatic_offset(child, chzoom=1.01):
    Fixed(
          Transform(child, alpha=.0),
          Transform(child, xalign=.0, xzoom=chzoom, gl_color_mask=(False, False, True, True)),
          Transform(child, xalign=.5, xzoom=chzoom, gl_color_mask=(False, True, False, True)),
          Transform(child, xalign=1.0, xzoom=chzoom, gl_color_mask=(True, False, False, True)),
          fit_first=True)
    crop (.0, .0, 1.0, 1.0)
    crop_relative True

init python:
    def glitch(child, randomobj=renpy.random.Random(), chroma=None, minbandheight=1, offset=25, crop=False):
        if chroma is None and renpy.display.render.models:
            chroma = True
        # child's width and height
        cwidth, cheight = renpy.render(child, 0, 0, 0, 0).get_size()
        if not (cwidth and cheight):
            return child
        lizt = [] # liste of strips
        offt = 0 # next strip's lateral offset
        theights = [randomobj.randint(0, cheight) for k in range(min(cheight, randomobj.randint(20, 40)//2))]
        theights.sort() # coordinates demarcating all the strips
        fheight = 0 # sum of the size of all the strips added this far
        while fheight<cheight:
            # theight is the height of this particular strip
            theight = max(theights.pop(0)-fheight, minbandheight) if theights else cheight-theight
            band = Transform(child,
                             crop=(-offt, fheight, cwidth, theight),
                             )
            if chroma:
                band = chromatic_offset(Flatten(band), chzoom=1.0+.5*offt/cwidth)
            lizt.append(band)
            fheight += theight
            if offt:
                offt = 0
            else:
                offt = randomobj.randint(-offset, offset)
        crop = crop or None
        return Fixed(Transform(child, alpha=.0),
                     VBox(*lizt),
                     fit_first=True,
                     crop_relative=crop or False,
                     crop=crop and (0, 0, 1.0, 1.0),
                     )

################################################################################
## Sabie's Glitch Code
################################################################################

##### Sabie Glitch Code #####
label sabie_glitch:
    show sabie at glitch:
        parallel:
            ease 1.0 zoom 1.025
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show sabie:
        parallel:
            ease 1.0 zoom 1.05
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show sabie at glitch:
        parallel:
            ease 1.0 zoom 1.1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show sabie:
        parallel:
            ease 1.0 zoom 1.15
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)

    return

##### Sabie Glitch Code #####
label sabie_glitch_big:
    show sabie at glitch:
        parallel:
            ease 1.0 zoom 1.2
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show sabie:
        parallel:
            ease 1.0 zoom 1.25
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show sabie at glitch:
        parallel:
            ease 1.0 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show sabie:
        parallel:
            ease 1.0 zoom 1.35
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)

    return

##### Sabie Spaz Code #####
label sabie_spaz():

    show sabie at glitch
    pause(0.1)
    show sabie
    pause(0.1)

    return

################################################################################
## Rohan's Glitch Code
################################################################################

##### Rohan Glitch Code #####
label rohan_glitch:
    show rohan at glitch:
        parallel:
            ease 1.0 zoom 1.025
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show rohan:
        parallel:
            ease 1.0 zoom 1.05
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.1)
    show rohan at glitch:
        parallel:
            ease 1.0 zoom 1.1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show rohan:
        parallel:
            ease 1.0 zoom 1.15
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.1)

    return

##### Rohan Spaz Code #####
label rohan_spaz():

    show rohan at glitch
    pause(0.1)
    show rohan
    pause(0.1)

    return

##### Rohan Glitch Code #####
label rohan_glitch_big:
    show rohan at glitch:
        parallel:
            ease 1.0 zoom 1.2
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show rohan:
        parallel:
            ease 1.0 zoom 1.25
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show rohan at glitch:
        parallel:
            ease 1.0 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show rohan:
        parallel:
            ease 1.0 zoom 1.35
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)

    return

################################################################################
## Tyree's Glitch Code
################################################################################

##### Tyree Glitch Code #####
label tyree_glitch:
    show tyree at glitch:
        parallel:
            ease 1.0 zoom 1.025
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show tyree:
        parallel:
            ease 1.0 zoom 1.05
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.1)
    show tyree at glitch:
        parallel:
            ease 1.0 zoom 1.1
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show tyree:
        parallel:
            ease 1.0 zoom 1.15
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.1)

    return

##### Tyree Spaz Code #####
label tyree_spaz():

    show tyree at glitch
    pause(0.1)
    show tyree
    pause(0.1)

    return

##### Tyree Glitch Code #####
label tyree_glitch_big:
    show tyree at glitch:
        parallel:
            ease 1.0 zoom 1.2
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show tyree:
        parallel:
            ease 1.0 zoom 1.25
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)
    show tyree at glitch:
        parallel:
            ease 1.0 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.3)
    show tyree:
        parallel:
            ease 1.0 zoom 1.35
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.5
    pause(0.2)

    return

################################################################################
## Alyssa's Glitch Code
################################################################################

##### Alyssa's Spaz Code #####
label alyssa_spaz():

    show alyssa at glitch
    pause(0.1)
    show alyssa
    pause(0.1)

    return

################################################################################
## Nasir's Glitch Code
################################################################################

##### Nasir's Spaz Code #####
label nasir_spaz():

    show nasir at glitch
    pause(0.1)
    show nasir
    pause(0.1)

    return
