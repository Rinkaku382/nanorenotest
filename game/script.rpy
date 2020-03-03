
label start:
    $ mood = 50
    jump roomscreen

label roomscreen:
        call screen roomscreens

label window:
    "Nice weather"
    jump roomscreen
label computer:
    "Surfing the internet..."
    menu:
        "Chat with friends.":
            $ mood += 10
            "Oh, hi Marc."
        "Read the comments.":
            $ mood -= 10
            "That's really depressing."
    jump roomscreen
label bed:
    "..."
    jump roomscreen
label tv:
    "There's a nice film."
    jump roomscreen
label door:
    if mood == 40:
        "A bad day today too."
        jump roomscreen
    elif mood == 60:
        "Hello, world!"
        jump roomscreen
    else:
        "I can't get outside."
        jump roomscreen

##label roomscreen2:
    ##if mood <= 40:
    ##    call screen roomscreens2
    ##if mood >= 60:
    ##    call screen roomscreen3


    return
