label credits: # TODO: Fix text type to match GUI!

    scene bg black with Dissolve(2.0)

    pause(1.0)
    show text "{b}Credits{/b}" with Dissolve(2.0)
    $ renpy.pause(2.0)
    hide text with Dissolve(1.0)
    show text "{b}Written and Directed by{/b}\nSmoke Mirror Studios" with Dissolve(1.5)
    $ renpy.pause(2.75)
    hide text with Dissolve(1.0)
    show text "{b}Character/Phone GUI Artist{/b}\nChaniMK{b}\n\n{b}CG Artist{/b}\nMx. RuK\n\nBackground/General GUI Artist{/b}\ncypher" with Dissolve(1.5)
    $ renpy.pause(4.0)
    hide text with Dissolve(1.0)
    show text "{b}Audio Director{/b}\nEliana\n\n{b}Composers{/b}\nKelly Thiessen\nShar J" with Dissolve(1.5)
    $ renpy.pause(4.0)
    hide text with Dissolve(1.0)
    show text "Thanks for playing! :)" with Dissolve(1.5)
    $ renpy.pause(2.0)

    hide text with Dissolve(2.0)

    pause(2.0)

    return
