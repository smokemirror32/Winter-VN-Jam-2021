## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Gallery") action ShowMenu("gallery")

        textbutton _("Music") action ShowMenu("music_gallery")

        textbutton _("Return"):

            yoffset 45

            action Return()

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label title

    use extras_navigation

### Image Gallery screen ############################################################

image cg3_button = Transform("images/cg/Cooking_Tangyuan_Empty.webp", zoom=0.2)
image cg4_button = Transform("images/cg/Family_Dinner.webp", zoom=0.2)
image cg5_button = Transform("images/cg/Looking_Back.webp", zoom=0.2)
image cg1_button = Transform("images/cg/Magpie_Keychain.webp", zoom=0.2)
image cg2_button = Transform("images/cg/Masami_Nasir_Kiss.webp", zoom=0.2)
image cg6_button = Transform("images/cg/Masami_Xinyi_Hug.webp", zoom=0.2)
image cg7_button = Transform("images/cg/Rohan_Mall.webp", zoom=0.2)

init python:
    g = Gallery()

    g.button("cg_3")
    g.unlock_image("images/cg/Cooking_Tangyuan_Empty.webp")
    g.unlock_image("images/cg/Cooking_TangYuan_Step1.webp")
    g.unlock_image("images/cg/Cooking_TangYuan_Step2.webp")
    g.unlock_image("images/cg/Cooking_TangYuan_Step3.webp")
    g.unlock_image("images/cg/Cooking_TangYuan_Step41.webp")
    g.unlock_image("images/cg/Cooking_TangYuan_Step42.webp")

    g.button("cg_4")
    g.unlock_image("images/cg/Family_Dinner.webp")
    g.unlock_image("images/cg/Family_Dinner_NoShadow.webp")

    g.button("cg_5")
    g.unlock_image("images/cg/Looking_Back.webp")

    g.button("cg_1")
    g.unlock_image("images/cg/Magpie_Keychain.webp")

    g.button("cg_2")
    g.unlock_image("images/cg/Masami_Nasir_kiss.webp")

    g.button("cg_6")
    g.unlock_image("images/cg/Masami_Xinyi_Hug.webp")

    g.button("cg_7")
    g.unlock_image("images/cg/Rohan_Mall.webp")

    g.transition = dissolve

screen gallery():

    tag menu
    use extras_menu(_("Gallery")):

        grid 3 2:
            #at truecenter
            spacing 20

            add g.make_button("cg_1","cg1_button","gui/gallery/locked.png")
            add g.make_button("cg_2","cg2_button","gui/gallery/locked.png")
            add g.make_button("cg_3","cg3_button","gui/gallery/locked.png")
            add g.make_button("cg_4","cg4_button","gui/gallery/locked.png")
            add g.make_button("cg_5","cg5_button","gui/gallery/locked.png")
            add g.make_button("cg_6","cg6_button","gui/gallery/locked.png")

        grid 1 1:
            #at truecenter

            ypos 470
            spacing 20

            add g.make_button("cg_7","cg7_button","gui/gallery/locked.png")

## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

init python:

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/chaos.mp3")
    mr.add("audio/music/emotional.mp3")
    mr.add("audio/music/finale.mp3")
    mr.add("audio/music/lighthearted.mp3")
    mr.add("audio/music/uptempo.mp3")
    mr.add("audio/music/reflective.mp3")

screen music_gallery():

    tag menu
    use extras_menu(_("Music")):

        vbox:
            xalign 0.5
            yalign 0.5

            # Title of Table
            grid 2 1:

                at truecenter
                spacing 350

                text "{b}Title{/b}":
                    size 50
                    color u'#073D6D'

                text "{b}Composer{/b}":
                    size 50
                    color u'#073D6D'

            null height 30

            grid 2 6:

                at truecenter
                xspacing 350

                # The buttons that play each track. TODO - Don't forget to say who did what track!

                textbutton "Reflective":
                    text_size 40
                    action mr.Play("audio/music/reflective.mp3")
                text "Shar J":
                    size 40
                    color u'#7B9DBA'

                textbutton "Chaos":
                    text_size 40
                    action mr.Play("audio/music/chaos.mp3")
                text "Shar J":
                    size 40
                    color u'#7B9DBA'

                textbutton "Emotional":
                    text_size 40
                    action mr.Play("audio/music/emotional.mp3")
                text "Kelly Thiessen":
                    size 40
                    color u'#7B9DBA'

                textbutton "Lighthearted":
                    text_size 40
                    action mr.Play("audio/music/lighthearted.mp3")
                text "Kelly Thiessen":
                    size 40
                    color u'#7B9DBA'

                textbutton "Uptempo":
                    text_size 40
                    action mr.Play("audio/music/uptempo.mp3")
                text "Shar J":
                    size 40
                    color u'#7B9DBA'

                textbutton "Finale":
                    text_size 40
                    action mr.Play("audio/music/finale.mp3")
                text "Kelly Thiessen":
                    size 40
                    color u'#7B9DBA'

            null height 60

            grid 3 1:

                at truecenter

                spacing 10

                # Buttons that let us advance through tracks.
                imagebutton auto "gui/music_room/previous_%s.png" action mr.Previous()
                imagebutton auto "gui/music_room/play_%s.png" action PauseAudio("music", value="toggle")
                imagebutton auto "gui/music_room/next_%s.png" action mr.Next()

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        on "replaced" action [mr.Stop(),Play("music", "audio/music/finale.mp3")]
