from random import randint 

def apple_rnd_cord(worm,size):
    # Random coordinates for the apple
    while True:
        x = randint(0,size-1)
        y = randint(0,size-1)
        if (y,x) not in worm:
            return (y,x)


def worm_first_cord(size):
    # Random coordinates for the first piece of the worm
    return (randint(0,size-1),randint(0,size-1))


def print_frame(worm,apple,size):
    # Prints the frame, the worm and the apple
    for y in range(size):
        for x in range(size):
            if (y,x) in worm:
                if (y,x) == worm[0]: # Uppercase for head
                    print("O",end=" ")
                else:
                    print("o",end=" ")
            elif (y,x) == apple:
                print("X",end=" ")
            else:
                print("_",end=" ")
        print()
    print()


def move_head(worm,direction):
    # Gives new coordinates for the head
    y = worm[0][0]
    x = worm[0][1]

    if direction == "u":
        worm[0] = (y-1,x)
    elif direction == "d":
        worm[0] = (y+1,x)
    elif direction == "r":
        worm[0] = (y,x+1)
    elif direction == "l":
        worm[0] = (y,x-1)


def move_worm(worm,direction):
    # Gives new coordinates for each part of the worm and the head
    for i in range(len(worm)-1,0,-1):
        worm[i] = worm[i-1]

    move_head(worm,direction)


def check_collision(worm,direction,size):
    # Checks whether the worm will collide with a wall or its tail
    x = worm[0][1]
    y = worm[0][0]

    if direction == "u" and (y == 0 or (y-1,x) in worm):
        return True
    elif direction == "d" and (y == size-1 or (y+1,x) in worm):
        return True
    elif direction == "l" and (x == 0 or (y,x-1) in worm):
        return True
    elif direction == "r" and (x == size-1 or (y,x+1) in worm):
        return True
    else:
        return False


def check_apple(worm,apple):
    # Checks whether worm got the apple
    return worm[0] == apple


def ask_size():
    # Asks the size of board from user
    while True:
        try:
            size = int(input("Size of the board (e.g. 10): "))
            if size < 2:
                raise ValueError
            else:
                return size
        except ValueError:
            print("Please give proper size")
            print("An integer, bigger than 1")


def ask_update_time():
    # Asks the update time from the user
    while True:
        try:
            time = float(input("Update time between frames, in seconds (e.g. 0.1): "))
            if time <= 0:
                raise ValueError
            else:
                return time
        except ValueError:
            print("Please give proper time")
            print("A float, bigger than 0")


def ask_settings():
    size = ask_size()
    update_time = ask_update_time()
    return size,update_time



def print_options():
    print("1) Play again")
    print("2) Change settings")
    print("3) Quit")
    print()


def ask_command():
    # Asks what to do after a game finishes
    print_options()
    command = input(": ")
    if command not in ("1","2","3"):
        print("Invalid command")
        command = input(": ")

    return command



