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
    scene roomd
    with fadehold
    $ mood = 50
    $ menthealth = 0
    $ sofiatalk = False
    """
    You slowly wake up in your room.

    The morning's soft colours linger through the whole apartment.
    """
    jump roomdownscreen

label roomdown:
    scene roomu
    $ renpy.pause(0.5)
    scene roomd
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label roomdownscreen:
    scene roomd
    call screen roomdownscreen

label roomup:
    scene roomd
    $ renpy.pause(0.5)
    scene roomu
    with fade
    $ renpy.pause(1)
    jump roomupscreen
label roomupscreen:
    scene roomu
    call screen roomupscreen
label window:
    """
    The weather outside is nice.

    It's still early morning, so there are not many people around.
    """
    jump roomdownscreen
label bed:
    """
    You are not tired, now.
    """
    jump roomupscreen
label tv:
    """
    There's a nice film.

    Maybe it's a bit sad, but you've never seen it.
    """
    jump roomdownscreen

label computer:
    scene computerneut
    with slowfade
    """
    You sit at your desk and discover that the PC is already turned on.

    On the screen you see a young girl.

    She's watching you intensely and surprised.
    """
    s "You're awake, finally!"
    menu:
        "Sorry, but...who are you?":
            $ mood += 5
            scene computergood
            with dissolve
            s "Guess your memory still isn't alright, huh...?"
        "I don't feel like talking to a stranger.":
            $ mood -= 5
            scene computersad
            with dissolve
            s "A stranger? Well, I'm not a stranger, I'm your best friend!"
    s "Listen, I'm here to help you."
    y "Help?"
    s "Yes, of course. I've been trying to help you for a long time, now, but you keep forgetting."
    y "I...I didn't know..."
    s """
    Don't worry, like I said I'm here to help.

    First of all, as you already know, this is your computer. Here you'll be able to talk with me.

    Of course if you'll access to it, I'll be able to guide you or help you however I can if something...strange happens.
    """
    menu:
        "Something strange?":
            $ mood += 5
            if mood == 55:
                scene computergood
            if mood == 50:
                scene computerneut
                with dissolve
            s "Don't worry, there's nothing dangerous out there! Not for now, at least..."
        "What?! What should happen?":
            $ mood -= 5
            if mood <= 45:
                scene computersad
            if mood == 50:
                scene computerneut
                with dissolve
            s "Please, don't worry so much!"
    s """
    Well, how to explain it...

    You already know you've lost your memory.

    Imagine this apartment as your mind, a space from which your memories escaped.

    Now, all the most important memories you have are out there.

    I don't know if you tried, but you can't exit from your apartment's door, now.

    That's because you're stuck in your sentimental state, which is your apartment itself.

    We can say that your mood is influenced by your actions inside this apartment.

    In order to get out, you'll need intense levels of mood.

    Otherwise the door that leads to your memories won't open...
    """
    menu:
        "That's absurd! Are you kidding me or what?":
            $ mood -= 5
            if mood == 55:
                scene computergood
            if mood == 45:
                scene computersad
                with dissolve
            if mood == 40:
                scene computersad
            s """
            Listen, I'm not lying to you.

            I know it's something hard to believe, but it's the truth.

            And even if it wasn't, do you think you have better options? You're still trapped in that apartment!

            So, now, calm down and let me explain...

            You're trapped in there because you've lost some important memories, ok?

            To retrieve them you have to exit from the door and re-experience them.

            The most important thing to know is that everything you do or say will influence your mood.

            And, once you've reached a certain level, you'll be able to go out.

            I think you're good to go, now, the door should be open.

            And please...when you come back tell me how it was, ok?
            """
            menu:
                "I will.":
                    s "Thanks. Go now!"
                "Hmm, we'll see.":
                    s "Ok, it's fine..."
        "I'm not sure if I'm following you...":
            $ mood += 5
            if mood == 55:
                scene computergood
                with dissolve
                s "There's no problem, I'm glad that at least you're not sad."
            if mood == 60:
                scene computergood
                s "There's no problem, I'm glad that at least you're not sad."
            if mood == 45:
                scene computersad
                s "I know you're sad but don't worry..."
            s """
            The most important thing to know is that everything you do or say will influence your mood.

            And, once you've reached a certain level, you'll be able to go out.

            I think you're good to go, now, the door should be open.

            And please...when you come back tell me how it was, ok?
            """
            menu:
                "I will.":
                    s "Thanks. Go now!"
                "Hmm, we'll see.":
                    s "Ok, it's fine..."
    jump roomdownscreen
label computer2:
    if sofiatalk == True and mood >= 55:
        scene computergood
        s "I see you're doing fine, today!"
    if sofiatalk == True and mood <= 45:
        scene computerbad
        s "You look so sad..."
    jump roomdownscreen

label door:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen
    if mood <= 45:
        scene trauma
        with slowfade
        """
        You find yourself in a dark place, ruled by sad and heavy feelings.

        A garden, it seems, yet the entire place seems to be falling apart.

        In front of you there is a man. He's looking at you, his eyes glittering in the darkness.

        Suddenly, you feel a stabbing pain hitting you.

        You feel alone, somehow, and that black shadow seem to be connected to that feeling.

        He doesn't talk nor move. He just watches you silently as a strange sense of guilt caughts you.

        And so the memory ends, without a word spoken.
        """
        show black
        with fadehold
        $ persistent.passage_3 = True
        $ renpy.end_replay()

        return
    elif mood >= 55:
        scene mem
        with slowfade
        """
        There is a small and feeble garden ahead of you.

        A big tree casts his leaves towards the sky and all the colours are pale, as if you're in a dream.

        The wind blows softly, caressing your skin. It's a cold breeze, yet tender.

        In the middle of the garden there is a man, sitted on an old chair.

        He gives you his back, so you can't see his face, yet it reminds you of something.

        A memory that you thought was gone is silently appearing in front of you as a pale shadow,

        You don't know how, but you understand he's smiling even though you can't see it.

        He doesn't talk and not even move, yet there is a deep feeling of calmness that comes with the memory's end.
        """
        show black
        with fadehold
        $ persistent.passage_3 = True
        $ renpy.end_replay()

        return
