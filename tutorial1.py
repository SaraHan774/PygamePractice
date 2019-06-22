import pygame as py

py.init()

win = py.display.set_mode((500, 500))

py.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5  # how fast it moves

# main loop - check if you hit sth

run = True

while run:
    py.time.delay(100)  # clock for the game. 100ms
    # check for events

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    keys = py.key.get_pressed()

    if keys[py.K_LEFT]:
        x -= vel
    if keys[py.K_RIGHT]:
        x += vel
    if keys[py.K_UP]:
        y -= vel
    if keys[py.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    py.draw.rect(win, (255, 0, 0), (x, y, width, height))  # everything is on the surface
    py.display.update()

py.quit()



