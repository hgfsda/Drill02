from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
cx = 0
sy = 270

while(1):
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(cx > -360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = 250 * math.cos(cx) + 400
        y = 210 * math.sin(sy) + 300
        character.draw_now(x, y)
        cx = cx - 0.05
        sy = sy + 0.05
        delay(0.01)

close_canvas()
