import pygame as py

py.init()

win = py.display.set_mode((500, 480))

py.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program
# list
# py.image.load('filename.extension')
# folder : py.image.load(py.path.join('folder name', 'filename . extension'))
# path : py.image.load('pics/p1.png')

walkRight = [py.image.load('Game/R1.png'), py.image.load('Game/R2.png'), py.image.load('Game/R3.png'), py.image.load('Game/R4.png'), py.image.load('Game/R5.png'), py.image.load('Game/R6.png'), py.image.load('Game/R7.png'), py.image.load('Game/R8.png'), py.image.load('Game/R9.png')]
walkLeft = [py.image.load('Game/L1.png'), py.image.load('Game/L2.png'), py.image.load('Game/L3.png'), py.image.load('Game/L4.png'), py.image.load('Game/L5.png'), py.image.load('Game/L6.png'), py.image.load('Game/L7.png'), py.image.load('Game/L8.png'), py.image.load('Game/L9.png')]
bg = py.image.load('Game/bg.jpg').convert()  # background image
char = py.image.load('Game/standing.png')  # sprite, still image - when just standing

screen_width = 500
screen_height = 500

clock = py.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5  # how fast it mo2es

# global variable
is_jump = False
jump_count = 10
left = False
right = False
walk_count = 0


def redraw_game_window():
    global walk_count  # take the var above and make it global
    win.blit(bg, (0, 0))
    if walk_count + 1 >= 27:
        walk_count = 0  # if we were to try greater than 27, index error

    if left:
        win.blit(walkLeft[walk_count // 3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walkRight[walk_count // 3], (x, y))
        walk_count += 1
    else:
        win.blit(char, (x, y))
        walk_count = 0
    py.display.update()


# main loop - check if you hit sth
run = True
while run:
    clock.tick(27)  # set FPS to 27
    py.time.delay(100)  # clock for the game. 100ms
    # check for events

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    if keys[py.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[py.K_RIGHT] and x < screen_width - width - vel:
        x += vel
        left = False
        right = True

    else:
        right = False
        left = False
        walk_count = 0 # how many steps

    if not is_jump: # disable up and down movement
        if keys[py.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= -10: # move the character up - hang - down
            neg = 1
            if jump_count < 0:
                neg = -1  # move downwards by * -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1 # move down slowly - 20 positions

        else:
            is_jump = False
            jump_count = 10

    redraw_game_window()  # make sure to call the drawing function


py.quit()



