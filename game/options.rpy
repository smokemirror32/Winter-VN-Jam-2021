## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("And So, I Fall")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""

{size=+20}{b}Note from the Lead Developer{/b}{/size}

Hey there,

Thanks for playing the game we made for the 2021 Winter VN Jam. If you're interested in more related content on the story (including some epilogue tidbits), check out the development logs on our Itch page {a=https://smokemirror.itch.io/and-so-i-fall}here{/a}.

We also want to hear from you. Whether it's about things that you loved or things that we could improve upon for future releases, feel free to drop us a line. We don't bite. :)

Until next time!

Smoke Mirror Studios


{size=+20}{b}The Team{/b}{/size}

Lead Developer: {a=https://twitter.com/SmokeMirrorDev}Smoke Mirror Studios{/a}

Character/Phone GUI Artist: {a=https://twitter.com/ChaniMK_VN}ChaniMK{/a}

CG Artist: {a=https://twitter.com/mx_ruk}Mx. RuK{/a}

Background/General GUI Artist & GUI Programmer: cypher

Audio & Voice Director: {a=https://twitter.com/TheStorysinger}Eliana Zebro{/a}

Composers: {a=https://www.trashcatmusic.com/}Kelly Thiessen{/a}, {a=https://sharjcomposer.com/}Shar J{/a}

Editor: {a=https://twitter.com/theallievera}Allie Vera{/a}

Gallery Screen Programmer: {a=https://twitter.com/PumpkinSpike}Pumpkin Spike{/a}


{size=+20}{b}Voice Actors{/b}{/size}

Masami: {a=https://twitter.com/SumRGuy}Ryoma Ishizuka{/a}

Xinyi: {a=https://twitter.com/MeganRYoumans}Megan Youmans{/a}

Sabie: {a=https://twitter.com/EricaChiem}Erica Chiem{/a}

Rohan: {a=https://twitter.com/pranshuland}Pranshu Mishra{/a}

Tyree: {a=https://twitter.com/JtasticVA}Jay M.{/a}

Nasir: {a=https://twitter.com/WindLightHub}Darius T. Jackson{/a}


{size=+20}{b}Creative Commons Attributions{/b}{/size}

Our glitch code was derived from {a=https://github.com/Gouvernathor/renpy-ChromaGlitch}Gouvernathor{/a}

Our sound effects were derived from:

-- Free SFX
-- freesound
-- marker medium streep by badvibezproductionz (https://freesound.org/people/badvibezproductionz/sounds/178372/)

Our backgrounds were derived from the following images licensed under CC by 2.0 (https://creativecommons.org/licenses/by/2.0/):

-- Grunge Vignette Border PNG Transparent for Photoshop by Textures4Photoshop (http://www.textures4photoshop.com/tex/grunge-and-rust/grunge-vignette-border-png-transparent-for-photoshop.aspx)

-- Our Dallas Personal Injury Lawyers Care by Mullen & Mullen Law Firm (https://www.pinterest.ca/pin/323062973247629685/)

-- School Lockers Hallway High by elizabethaferry (https://pixabay.com/photos/school-lockers-hallway-high-school-417612/)

-- Courtyard, Lincoln-Sudbury Regional High SChoo, Sudbury MA by Wikimedia Commons (https://commons.wikimedia.org/wiki/File:Courtyard,_Lincoln-Sudbury_Regional_High_School,_Sudbury_MA.jpg)

-- Black Vehicle Interior by Mike (https://www.pexels.com/photo/black-vehicle-interior-244818/)

-- gray freestanding range oven by Becca Tapert (https://unsplash.com/photos/uGak0qtrphM)

-- Bedroom Room Youth by lrainero (https://pixabay.com/photos/bedroom-room-youth-design-1137939/)

-- black wooden table on rug by NeONBRAND (https://unsplash.com/photos/mGZX2MOPR-s)

-- Free Home Image by Francesca Tosolini (https://unsplash.com/photos/XcVm8mn7NUM)

-- Cairo in winter woods cat by Wikimedia Commons (https://commons.wikimedia.org/wiki/File:Cairo-in-winter-woods-cat.JPG)

-- Old railway carriages with graffiti by Chris F (https://www.pexels.com/photo/old-railway-carriages-with-graffiti-on-surface-under-cloudy-sky-4000251/)

-- bare tree under Milky Way at night by Jack B (https://unsplash.com/photos/Hg5dJF-ootQ)

-- brown brick wall during daytime by Marie-Michele Bouchard (https://unsplash.com/photos/9nQfpvQxQe0)

""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "AndSoIFall"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/music/finale.mp3"
define config.default_music_volume = 0.5


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Adding a layer ##
define config.layers = [ 'master', 'transient', 'screens', 'glitching', 'character','overlay']
define config.tag_layer = {'masami':'character'}  #tag it so every cohan image is automatically place on the 'character' layer. Alternatively, you can use "onlayer" to manually put him in there every time
define config.menu_clear_layers = ['character'] # clear it so the char will disappear when enter game screen, otherwise he will awkwardly stay there

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = Dissolve(.5)


## Used when entering the main menu after the game has ended.

define config.end_game_transition = Dissolve(.5)


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Getting images to strip properly
define config.automatic_images = ['/']
define config.automatic_images_strip = [ 'images' ]



## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 60


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "AndSoIFall-1639174892"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
