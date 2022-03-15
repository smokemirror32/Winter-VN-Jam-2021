label credits: # TODO: Fix text type to match GUI!

    scene bg black with Dissolve(2.0)

    pause(1.0)
    show text "{size=+15}{b}Credits{/b}{/size}" with Dissolve(1.5)
    pause
    hide text with Dissolve(1.0)
    show text "{b}Written and Directed by{/b}\nSmoke Mirror Studios" with Dissolve(1.5)
    pause
    hide text with Dissolve(1.0)
    show text "{b}Character & Phone GUI Artist{/b}\nChaniMK\n\n{b}CG Artist{/b}\nMx. RuK\n\n{b}Background & General GUI Artist{/b}\ncypher" with Dissolve(1.5)
    pause
    hide text with Dissolve(1.0)
    show text "{b}Audio Director{/b}\nEliana\n\n{b}Composers{/b}\nKelly Thiessen\nShar J\n\n{b}Editor{/b}\nAllie Vera" with Dissolve(1.5)
    pause
    hide text with Dissolve(1.0)
    show text "{b}Voice Actors{/b}\n{i}Masami{/i}                             Ryoma Ishizuka\n  {i}Xinyi{/i}                                  Megan Youmans\n{i}Sabie{/i}                                  Erica Chiem        \n{i}Rohan{/i}                                Pranshu Mishra\n{i}Tyree{/i}                                  Jay M.                   \n   {i}Nasir{/i}                                   Darius T. Jackson" with Dissolve(1.5)
    pause
    hide text with Dissolve(1.0)
    show text "Thanks for playing! :)" with Dissolve(1.5)
    $ renpy.pause(2.0)

    hide text with Dissolve(2.0)

    pause(0.5)

    show screen about
    $ renpy.pause(hard=True)

    return
