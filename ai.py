# Slightly improved version of the A.I.
# Can make a simple move to avoid collision with tail

def decide_direction(worm,apple):
    x = worm[0][1]
    y = worm[0][0]

    if x < apple[1]:
        if (y,x+1) not in worm:
            return "r"
        else:
            return "u"

    elif x > apple[1]:
        if (y,x-1) not in worm:
            return "l"
        else:
            return "d"

    elif y < apple[0]:
        if (y+1,x) not in worm:
            return "d"
        else:
            return "r"

    elif y > apple[0]:
        if (y-1,x) not in worm:
            return "u"
        else:
            return "l"
