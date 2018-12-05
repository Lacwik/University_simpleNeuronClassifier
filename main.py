from objects import *
from neural_networks import *

points = init_points()

nn1 = Network1()
nn2 = Network2(const_signal=1)
nn3 = Network3()
nn4 = Network4(bias=1)

tmp = 0
activation = 'sigmoid'  # linear, unipolar, sigmoid


def color_point(point, function, tmp):
    if function == 'sigmoid':
        if 0.0 < tmp <= 0.25:
            point.color = YELLOW
        if 0.25 < tmp <= 0.5:
            point.color = BLUE
        if 0.5 < tmp <= 0.75:
            point.color = GREEN
        if 0.75 < tmp <= 1.0:
            point.color = RED
    if function == 'linear':
        if tmp == 1:
            point.color = RED
        if tmp == 0:
            point.color = BLUE
    if function == 'unipolar':
        if tmp <= -2:
            point.color = DARK_BLUE
        if -2 < tmp <= 0:
            point.color = BLUE
        if 0 < tmp <= 2:
            point.color = GREEN
        if 2 < tmp:
            point.color = RED


def quest1(function='sigmoid'):
    for point in points:
        tmp = nn1.compute(point.x, point.y, function)
        color_point(point, function, tmp)


def quest2(function='sigmoid'):
    for point in points:
        tmp = nn2.compute(point.x, point.y, function)
        color_point(point, function, tmp)


def quest3(function='sigmoid'):
    for point in points:
        tmp = nn3.compute(point.x, point.y, function)
        color_point(point, function, tmp)


def quest4(function='sigmoid'):
    for point in points:
        tmp = nn4.compute(point.x, point.y, function)
        color_point(point, function, tmp)



while not PROGRAM_END:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(PAUSED):
                print("-----START-----")
            else:
                print("-----STOP-----")
            PAUSED = not PAUSED
        if event.type == pygame.QUIT:
            PROGRAM_END = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            PROGRAM_END = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            main_screen.fill(BACKGROUND_COLOR)
            activation = 'linear'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            main_screen.fill(BACKGROUND_COLOR)
            activation = 'unipolar'
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            main_screen.fill(BACKGROUND_COLOR)
            activation = 'sigmoid'

    quest1(activation)
    #quest2(activation)
    #quest3(activation)
    #quest4(activation)
    for point in points:
        point.draw()
    function_text(activation)

    pygame.display.flip()
    clock.tick(framerate)
pygame.quit()



print("========== END MAIN ===========")