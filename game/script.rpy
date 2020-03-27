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
    """
    Home.

    The safest place of all, isn't it?

    Well, maybe it is. Or maybe not.

    But one thing is certain...

    Home is where your memories linger.

    Your deepest memories.

    Be them happy memories or sad ones, that doesn't matter.

    They all stay there.

    Hidden in the shadows, perhaps.
    """
    scene roomd_dawn
    with fadehold
    $ mood = 50
    $ menth = 5
    $ sofiatalk = False
    """
    You open your eyes.

    The morning's soft colours linger from the window.

    A small apartment, with an upper floor. You...

    You don't recognize it.

    Or you do recognize it but something is different.

    Missing, maybe?

    Or perhaps there are things there weren't before...

    But there is something, in there.

    Something that attracts you, that calls you.

    Is it the door?

    The computer?

    Or something else?
    """
    jump roomdownscreen

label roomdown:
    scene roomu_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label sofiagoodfade:
    scene computergood
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label sofiasadfade:
    scene computerbad
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen
label roomdownscreen:
    scene roomd_dawn
    call screen roomdownscreen

label roomup:
    scene roomd_dawn
    $ renpy.pause(0.5)
    scene roomu_dawn
    with fade
    $ renpy.pause(1)
    jump roomupscreen
label roomupscreen:
    scene roomu_dawn
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

    Maybe later...
    """
    jump roomupscreen
label tv:
    """
    There's a film on the tv.

    Maybe it's a bit sad, but you've never seen it.

    It seems still at the beginning.

    A car advances through a thic fog and a boy is playing at the street's border.

    Then...a crash, and the boy turns around.

    You look away, feeling a soft pain in the head.
    """
    jump roomdownscreen
label books:
    """
    A library filled with books.

    They seem to be all classics.
    """
    jump roomdownscreen
label plant:
    """
    The first Spring's sprouts are starting to appear on this plant.

    You wonder which flowers will grow.
    """
    jump roomdownscreen
label trash:
    """
    Just a normal trash bin, nothing special about it.
    """
    jump roomdownscreen
label guit:
    """
    An old classic guitar.

    You faintly remember some chords...
    """
    jump roomupscreen

label computer:
    if sofiatalk == False:
        jump sofianeut
    if sofiatalk == True and mood >= 55:
        jump sofiagood
    if sofiatalk == True and mood <= 45:
        jump sofiasad
label sofiagood:
    scene computergood
    with slowfade
    s "I see you're doing fine, today!"
    jump sofiagoodfade
label sofiasad:
    scene computerbad
    with slowfade
    s "You look so sad..."
    jump sofiasadfade
label sofianeut:
    scene computerneut
    with slowfade
    $ sofiatalk = True
    """
    You sit at your desk and discover that the PC is already turned on.

    On the screen there's a young girl.
    """
    s "You're awake!"
    menu:
        "Sorry, but...who are you?":
            $ mood += 5
            scene computergood
            with dissolve
            s """
            Guess your memory still isn't alright, huh...?

            Well, anyway, my name is Sofia. I'm your...best friend.
            """
        "I don't feel like talking to a stranger.":
            $ mood -= 5
            scene computerbad
            with dissolve
            s "A stranger? Well, I'm not a stranger, I'm Sofia...your best friend!"
    s "I'm here to help you."
    y "Help?"
    s "Yes, of course. We know each other very well, but you've lost your memory, so..."
    y "Yeah, I don't remember..."
    s """
    Don't worry.

    Like I said, I'm here to help.

    First of all, as you already know, this is your computer.

    By interacting with it, you'll be able to talk with me.

    Now, second...have you already tried opening the door?
    """
    menu:
        "Yes.":
            s """
            Very well. Then you should have noticed it's close.
            """
        "No.":
            s """
            Well, doesn't matter since it's closed.
            """
    s """
    In all sincerity, I don't really know how to open it...

    But it seems to be related to that icon on this screen.

    It changes in relation to your mood.

    And when it does, I guess you should try to check on the door.

    Last time you did, something strange happened...
    """
    menu:
        "Something strange?":
            $ mood += 10
            if mood == 55:
                scene computergood
            if mood == 50:
                scene computerneut
                with dissolve
            s "Don't worry, there's nothing dangerous out there! Not that I know, at least..."
        "...What should happen?":
            $ mood -= 10
            if mood <= 45:
                scene computerbad
            if mood == 50:
                scene computerneut
                with dissolve
            s "Please, don't worry so much!"
    s """
    Well, how to explain it...

    The last time you managed to get out.

    But I haven't seen you for a lot of time, after that.

    And here you are now!

    ...without memory, as well as before.
    """
    menu:
        "Were you here all this time?":
            s """
            Yes, since before you lost your memory.

            In fact, I waited for some days, but...

            You're here, now, so that's the important thing, isn't it?
            """
        "So, how did we know each other?":
            s """
            It's been something like...five years.

            We were at school together.

            But then, we separated at University and kept contact only through this program, online.

            I see your room and you see mine,so we're...

            Connected? Sort of, at least.
            """
    s """
    In any case, why don't you try that door?

    I think it should be alright, by now...

    Oh and...I have some kind of request...?

    When you come back could you tell me how it was?
    """
    menu:
        "I will.":
            $ mood += 15
            if mood == 55:
                scene computergood
                with dissolve
            if mood == 60:
                scene computergood
            if mood == 45:
                scene computerbad
            s "Thanks. Go now!"
        "Hmm, we'll see.":
            $ mood -= 15
            if mood == 55:
                scene computergood
            if mood == 45:
                scene computerbad
                with dissolve
            if mood == 40:
                scene computerbad
            s "Ok, it's fine..."
    if mood >= 55:
        jump sofiagoodfade
    if mood <= 45:
        jump sofiasadfade

label door:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen
    if mood <= 45:
        scene trauma
        with slowfade
        $ menth -= 1
        """
        You find yourself in a dark place, ruled by sad and heavy feelings.

        A garden, it seems.

        Yet the entire place seems to be falling apart.

        In front of you there is a man. He's looking at you, his eyes glittering in the darkness.

        Suddenly, you feel a stabbing pain hitting you.

        You feel alone, somehow, and that black shadow seem to be connected to that feeling.

        He doesn't talk nor move. He just watches you silently as a strange sense of guilt caughts you.

        And so the memory ends, without a word spoken.
        """
        jump narrator2
    elif mood >= 55:
        scene mem
        with slowfade
        $ menth += 1
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
        jump narrator2
        show black
        with fadehold

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 2 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator2:
    show black
    with fadehold
    """
    Memories.

    Do you remember who you are? Or where you come from?

    Even the apartment where you lived seems to be blurring away from your memories.

    But don't worry, I'm here with you. To help you.

    Or even guide you, we could say.

    You've seen a glimpse of...memories, didn't you?

    Were them yours? Or someone else's?

    You're doubting, aren't you?

    That's good. Because doubt is the only certainty someone could obtain in this world.
    """
    scene roomd_dawn
    with fadehold
    $ mood = 50
    $ sofiatalk = False
    $ windowseen = False
    $ books= False
    $ trash = False
    $ plant = False
    if menth >= 6:
        """
        Waking up, you feel a bittersweet sensation in your heart.

        It lingers through your whole body, flowing towards your mind.

        It's a melancholic feeling, as if you've just seen an old friend whom you forgot.

        Lost in time, he's now nothing more than a pale figure in your head.

        The door...it's silently waiting for you to be ready.
        """
    if menth <= 4:
        """
        A strong headache wakes you up.

        Your mind is screaming for help, crowded with dark and horrific images.

        Pressing your fingers on the forehead, you try to calm it.

        The headache then suddenly disappears, leaving a deep emptiness behind.

        The door...you feel it calling to you, asking if you're ready to go out again.
        """
    jump roomdownscreen2

label sofiagoodfade2:
    scene computergood
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofiasadfade2:
    scene computerbad
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label sofianeutfade2:
    scene computerneut
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2

label roomdown2:
    scene roomu_dawn
    $ renpy.pause(0.5)
    scene roomd_dawn
    with fade
    $ renpy.pause(1)
    jump roomdownscreen2
label roomdownscreen2:
    scene roomd_dawn
    if mood >= 55 or mood <= 45:
        play sound "door.ogg"
        $ renpy.pause(0.1)
        "The door has opened..."
    call screen roomdownscreen2

label roomup2:
    scene roomd_dawn
    $ renpy.pause(0.5)
    scene roomu_dawn
    with fade
    $ renpy.pause(1)
    jump roomupscreen
label roomupscreen2:
    scene roomu_dawn
    call screen roomupscreen2
label window2:
    if sofiatalk == False:
        """
        The weather doesn't seem very nice.
        """
    if windowseen == True:
        """
        Everything outside really looks grim.
        """
    if sofiatalk == True:
        $ mood += 5
        $ windowseen = True
        """
        Looks like a gloomy day outside.

        Do you want to take a look?
        """
        menu:
            "Why not?":
                $ mood -= 5
                $ windowseen = True
                """
                Everything seems strangely empty.

                And the grey sky does not make you feel better.
                """
            "Not now.":
                "You step away from the window."
    jump roomdownscreen2
label bedpass2:
    """
    You can't sleep now.

    There are things you have to do.
    """
    jump roomupscreen2
label books2:
    if sofiatalk == False:
        """
        A library filled with books.

        Now that you pay more attention to it...

        You realize there are plenty of books about art.
        """
    if books == True:
        """
        You've already read.

        Maybe later...
        """
    if sofiatalk == True:
        $ mood += 5
        $ books = True
        "You look at the titles, unable to choose which book read."
        menu:
            "Choose one randomly.":
                $ mood += 5
                $ books = True
                """
                You pick and old essay about cinema.

                You remember the author's name, but not the title.

                'It's a film about you, your father, your grandfather.'

                'About someone who will live after you and who is still 'you'.'

                That seems to hit deep in your mind.
                """
            "You don't feel like reading.":
                "You leave the books be."
    jump roomdownscreen2
label plant2:
    if sofiatalk == False:
        """
        The leaves' green is brilliant...

        Yet there seems to be some dust on them.
        """
    if plant == True:
        """
        The plant is overflowing with joy.
        """
    if sofiatalk == True:
        "This plant sure needs some water."
        menu:
            "Water it.":
                $ mood += 5
                $ books = True
                "As you pour the water in the vase, the plant regains some light."
            "Maybe later...":
                """
                You don't really feel like it.

                Not now, at least.
                """
    jump roomdownscreen2
label trash2:
    if sofiatalk == False:
        """
        Trash seems to be piling up...
        """
    if trash == True:
        """
        Empty.

        It makes the house look cleaner.
        """
    if sofiatalk == True:
        "Maybe it's better to throw it away..."
        menu:
            "Empty the bin.":
                $ mood += 5
                $ trash = True
                "Now you feel better with yourself."
            "Leave it as it is.":
                "You don't really want to do that now."
    jump roomdownscreen2
label guit2:
    """
    This guitar...

    As you watch it, you remember playing it sometimes.

    But how much time has passed since then?
    """
    jump roomdownscreen2

label computer2:
    if sofiatalk == False:
        jump sofianeut2
    if sofiatalk == True and mood >= 55:
        jump sofiagood2
    if sofiatalk == True and mood <= 45:
        jump sofiasad2
label sofiagood2:
    scene computergood
    with slowfade
    s "It's nice seeing you smiling like this, you know?"
    jump sofiagoodfade2
label sofiasad2:
    scene computerbad
    with slowfade
    s """
    Is it me or you seem a little down?

    Please, take care of yourself...
    """
    jump sofiasadfade2
label sofianeut2:
    scene computerneut
    with slowfade
    $ sofiatalk = True
    s """
    You're finally back!

    Where were you?
    """
    menu:
        "I...got out of the door.":
            $ mood += 5
            scene computergood
            with dissolve
            s """
            Really?

            That...

            That is just incredible!

            And tell me, how did it go?
            """
        "Nowhere, just resting.":
            $ mood -= 5
            scene computerbad
            with dissolve
            s """
            Hmm, if you say so...

            Uhmm, you went out of the door, didn't you?

            Guess you don't want to talk about it...right?
            """
    if menth >= 6:
        menu:
            "I saw a strange man in a garden.":
                $ mood += 5
                if mood >= 55:
                    scene computergood
                if mood == 50:
                    scene computerneut
                    with dissolve
                if mood == 45:
                    scene computerbad
                s """
                That sounds very interesting!

                I think that was a piece of your memories...

                Unfortunately, I don't know much about it.

                How did that makes you feel?
                """
                menu:
                    "It was...sad.":
                        $ mood -= 5
                        if mood == 55:
                            scene computergood
                        if mood == 50:
                            scene computerneut
                        if mood <= 45:
                            scene computerbad
                            with dissolve
                        s """
                        Oh, I see...

                        Maybe it's not a very happy memory.

                        Or maybe it's somehow painful to remember about it.

                        Anyway, I have something important to tell you.
                        """
                    "Peaceful, I guess.":
                        $ mood += 5
                        if mood == 55:
                            scene computergood
                            with dissolve
                        if mood >= 60:
                            scene computergood
                        if mood == 50:
                            scene computerneut
                            with dissolve
                        if mood <= 45:
                            scene computerbad
                        s """
                        I'm glad to hear that!

                        It's nice to know it's a good memory for you.

                        That really is a good thing, don't you think?

                        Your smile tells me it is!

                        But anyway, ther's something important I forgot to tell you...
                        """
            "I prefer not to talk about it.":
                $ mood -= 5
                if mood >= 55:
                    scene computergood
                if mood == 50:
                    scene computerneut
                    with dissolve
                if mood == 45:
                    scene computerbad
                    with dissolve
                if mood <= 40:
                    scene computerbad
                s """
                Oh, I understand...guess it was too sad, right...?

                But anyway, I remembered to tell you something.
                """
    if menth <= 4:
        menu:
            "There was a scary man...":
                $ mood -=5
                if mood >= 55:
                    scene computergood
                if mood == 50:
                    scene computerneut
                    with dissolve
                if mood <= 45:
                    scene computerbad
                s """
                A scary man...?

                That sound really bad, doesn't it...

                And can you tell me something about him?
                """
                menu:
                    "I just want to forget him, now...":
                        $ mood += 5
                        if mood == 55:
                            scene computergood
                            with dissolve
                        if mood == 50:
                            scene computerneut
                            with dissolve
                        if mood <= 45:
                            scene computerbad
                        s """
                        I bet you do!

                        I guess I would do the same...

                        Well, let's change argument, then.

                        I just remembered about something, in fact!
                        """
                    "I think I'm still scared.":
                        $ mood -= 5
                        if mood == 55:
                            scene computergood
                            with dissolve
                        if mood == 50:
                            scene computerneut
                            with dissolve
                        if mood <= 45:
                            scene computerbad
                        s """
                        I can only imagine how terrible it could have been...

                        And I guess that's why you're so pale, huh?

                        But please, hang on in there, ok?
                        I'm with you!

                        Oh and now that I think about it...
                        """
            "I don't want to think about it.":
                $ mood += 5
                if mood == 55:
                    scene computergood
                    with dissolve
                if mood >= 60:
                    scene computergood
                if mood == 50:
                    scene computerneut
                    with dissolve
                if mood == 45:
                    scene computerbad
                s """
                I understand, I don't want to force you.

                Uhmm, well, guess it's better to change argument, huh?

                Oh, I know! I just remembered something that could be useful.
                """
    s """
    Last time I forgot to tell you about your room.

    Maybe you already noticed that there are plenty of interesting things, right?

    But, anyway, the thing is that they might be useful to keep you busy.

    You know, they say that distractions sometimes make us heppier, somehow.

    I think it's because by distracting ourselves we focus less on what's painful.

    Or what troubles us, anyway.

    But it's true that not all distractions can make us happier, isn't it?

    So be careful with your mood out there.
    """
    menu:
        "Ok, thanks for your help.":
            $ mood += 5
            if mood == 55:
                scene computergood
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                jump sofiagoodfade2
            if mood >= 60:
                scene computergood
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                jump sofiagoodfade2
            if mood == 50:
                scene computerneut
                with dissolve
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                jump sofianeutfade2
            if mood <= 45:
                scene computerbad
                s """
                Very well!

                I hope it's all clear...

                See you later, then!
                """
                jump sofiasadfade2
        "Uhmm yeah, right...":
            $ mood -= 5
            if mood == 55:
                scene computergood
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                jump sofiagoodfade2
            if mood >= 60:
                scene computergood
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                jump sofiagoodfade2
            if mood == 50:
                scene computerneut
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                jump sofiagoodfade2
            if mood == 45:
                scene computerbad
                with dissolve
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                jump sofiabadfade2
            if mood <= 40:
                scene computerbad
                s """
                Well, I hope it's all clear.

                See you later!

                And remember, whatever happens...I'm here.
                """
                jump sofiabadfade2

label door2:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen2
    if mood <= 45:
        scene trauma
        with slowfade
        $ menth -= 1
        """
        The red place again.

        It seems identic yet similar than last time.

        The strange, scary man is still there.

        He still watches you.

        Between the shadows, you have the impression he's pointing his finger at you.
        """
        m """
        You saw it...

        The fall of everything...

        You saw it...

        Didn't you?
        """
        """
        You don't understand what he's saying.

        You don't understand at all.

        What 'fall' is he talking about?

        What does it mean you saw it?

        You try to remember.

        Hard. Harder.

        But nothing comes to your mind.

        Absolutely nothing.

        And the memory starts to disappear.
        """
        show black
        with fadehold
        return
    elif mood >= 55:
        scene mem
        with slowfade
        $ menth += 1
        m """
        When we first met

        Our hands were cold

        The wind blew gently on the forest

        Silence, all around

        And a smile of happiness on my face.
        """
        """
        You look at the mysterious man in front of you.

        He just finished reading a passage from the book he's holding.
        """
        m """
        Do you remember this poem?

        It brings back so many memories...

        Yet, you don't seem to recall any of them...

        That makes me sad.

        So sad...
        """
        """
        You feel a tear falling slowly.

        Its warmth melts the ice that has frozen your heart.

        It's strange, but you feel as if an image is appearing in your mind.

        But it's still faded, as the scene that slowly disappears.
        """
        show black
        with fadehold
        return

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################START PASSAGE 3 #####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

label narrator3:
    show black
    with fadehold
    """
    AAA
    """
    scene roomd
    with fadehold
    $ mood = 50
    $ menthealth = 0
    $ sofiatalk = False
    $ windowseen = False
    $ books = False
    $ trash = False
    $ plant = False
    if menth >= 6:
        """
        AAA
        """
    if menth <= 4:
        """
        AAA
        """
    jump roomdownscreen3

label roomdown3:
    scene roomu
    $ renpy.pause(0.5)
    scene roomd
    with fade
    $ renpy.pause(1)
    jump roomdownscreen3
label roomdownscreen3:
    scene roomd
    call screen roomdownscreen3

label roomup3:
    scene roomd
    $ renpy.pause(0.5)
    scene roomu
    with fade
    $ renpy.pause(1)
    jump roomupscreen
label roomupscreen3:
    scene roomu
    call screen roomupscreen3

label window3:
    if sofiatalk == False or if windowseen == True:
        """
        The weather outside is nice.

        It's still early morning, so there are not many people around.
        """
    if sofiatalk == True:
        $ mood += 5
        $ windowseen = True
    jump roomdownscreen3
label bed3:
    """
    You are not tired, now.
    """
    jump roomupscreen3
label books3:
    if sofiatalk == False or if books == True:
        """
        A library filled with books.

        They seem to be all classics.
        """
    if sofiatalk == True:
        $ mood += 5
        $ books = True
    jump roomdownscreen3
label plant3:
    if sofiatalk == False or if plant == True:
        """
        The first Spring's sprouts are starting to appear on this plant.

        You wonder which flowers will grow.
        """
    if sofiatalk == True:
        $ mood += 5
        $ plant = True
    jump roomdownscreen3
label trash3:
    if sofiatalk == False or if trash == True:
        """
        Just a normal trash bin, nothing special about it.
        """
    if sofiatalk == True:
        $ mood += 5
        $ trash = True
    jump roomdownscreen3
label guit3:
    """
    An old classic guitar.

    You faintly remember some chords, but now it's not the time.
    """
    jump roomdownscreen3

label computer3:
    if sofiatalk == False:
        jump sofianeut3
    if sofiatalk == True and mood >= 55:
        jump sofiagood3
    if sofiatalk == True and mood <= 45:
        jump sofiasad3
label sofiagood3:
    scene computergood
    with slowfade
    s "I see you're doing fine, today!"
    jump sofiagoodfade3
label sofiasad3:
    scene computerbad
    with slowfade
    s "You look so sad..."
    jump sofiasadfade3
label sofianeut3:
    scene computerneut
    with slowfade
    $ sofiatalk = True

    if mood >= 55:
        jump sofiagoodfade3
    if mood <= 45:
        jump sofiasadfade3


label door3:
    if mood >= 46 and mood <= 54:
        "I can't get outside, it's tightly closed."
        jump roomdownscreen2
    if mood <= 45:
        scene trauma
        with slowfade
        $ trauma += 1
        """
        trauma
        """
    elif mood >= 55:
        scene mem
        with slowfade
        $ mem += 1
        """
        memory
        """
