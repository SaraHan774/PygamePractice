import pygame as py

py.init()

win = py.display.set_mode((500, 500))

py.display.set_caption("First Game")

screen_width = 500
screen_height = 500

x = 50
y = 50
width = 40
height = 60
vel = 5  # how fast it moves

# main loop - check if you hit sth
run = True
# global variable
is_jump = False
jump_count = 10

while run:
    py.time.delay(100)  # clock for the game. 100ms
    # check for events

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    if keys[py.K_LEFT] and x > vel:
        x -= vel
    if keys[py.K_RIGHT] and x < screen_width - width - vel:
        x += vel
    if not is_jump:
        if keys[py.K_UP] and y > vel:
            y -= vel
        if keys[py.K_DOWN] and y < screen_height - height - vel:
            y += vel
        if keys[py.K_SPACE]:
            is_jump = True
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

    win.fill((0, 0, 0))
    py.draw.rect(win, (255, 0, 0), (x, y, width, height))  # everything is on the surface
    py.display.update()

py.quit()



