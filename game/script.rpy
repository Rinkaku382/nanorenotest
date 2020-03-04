define slowfade = Fade(1.0, 0, 3.0)
define slowerfade = Fade (3.0, 0, 3.0)
define slowdissolve = Dissolve(1.0)
define fadehold = Fade(3.0, 1.0, 3.0)

define y = Character("You")
define n = Character("Narrator")
define s = Character("Sofia")
define m = Character("Strange Man")


label start:
    scene black
    n """
    Memories.

    Do you remember who you are? Or where you come from?

    Even the apartment where you lived seems to be blurring away from your memories.

    But don't worry, I'm here with you. To help you, or even guide you, we could say.
    """
    $ mood = 50
    scene room
    with fadehold

    """
    You slowly wake up in your room.

    The morning's soft colours linger through the whole apartment.
    """
    jump roomscreen

label roomscreen:
        call screen roomscreens

label window:
    $ mood += 10
    """
    The weather outside is nice.

    It's still early morning, so there are not many people around.
    """
    jump roomscreen
label computer:
    scene computer
    $ sofia = 50
    """
    You sit at your desk and discover that the PC is already turnedon.

    On the screen you see a young girl.

    She's watching you intensely and surprised.
    """
    s "You're awake, finally!"
    menu:
        "Sorry, but...who are you?":
            $ mood += 10
            s "Guess your memory still isn't alright, huh...?"
        "I don't feel like talking to a stranger.":
            $ mood -= 10
            s "A stranger? Well, I'm not a stranger, I'm your best friend!"
    s "Listen, I'm here to help you."
    y "Help?"
    s "Yes, of course. I've been trying to help you for along time, now, but you keep forgetting."

    menu:
        "Chat with friends.":
            $ mood += 10
            "Oh, hi Marc."
        "Read the comments.":
            $ mood -= 10
            "That's really depressing."
    jump roomscreen
label bed:
    """
    You are not tired, now.
    """
    jump roomscreen
label tv:
    $ mood += 10
    "There's a nice film."
    jump roomscreen
label door:
    if mood == 40:
        scene trauma
        "A bad day today too."
        jump roomscreen
    elif mood == 60:
        scene mem
        "Hello, world!"
        jump roomscreen
    else:
        "I can't get outside."
        jump roomscreen


    return
