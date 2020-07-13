from playsound import playsound


def play_sound(kick, snare, hihat):


    if kick:
        playsound("sound/kick.mp3",0)

    elif snare:
        playsound("sound/snare.wav",0)

    elif hihat:
        playsound("sound/hihat.wav",0)
