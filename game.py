import util
import ai as AI
from time import sleep

def print_game_over(points):
    print("The worm died :(")
    print("Points: " + str(points))
    print()
    time.sleep(1)


def print_game_won(points):
    print("Perfect game!")
    print("Points: " + str(points))
    print()
    time.sleep(1)

    
def play(size,update_time):

    # -------- initialize game ---------
    worm = []
    worm.append(util.worm_first_cord(size))
    apple = util.apple_rnd_cord(worm,size)
    apple_caught = False
    points = 0

    # ----------- main loop -------------
    while True:
        util.print_frame(worm,apple,size)
        direction = AI.decide_direction(worm,apple)

        if util.check_collision(worm,direction,size) == True:
            print_game_over(points)
            break

        # If no more spaces left
        if len(worm) == size ** 2:
            print_game_won(points)
            break

        # If worm got the apple in the last frame we move just the head.
        # This way the worm grows.
        if apple_caught:
            util.move_head(worm,direction)
        else:
            util.move_worm(worm,direction)

        apple_caught = util.check_apple(worm,apple)
        if apple_caught:
            points += 1
            worm.insert(1,apple) 
            apple = util.apple_rnd_cord(worm,size)
        
        sleep(update_time)


