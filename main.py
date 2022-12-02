from tkinter import *
import keyboard
import time
from random import *

from collisionChecker import CollisionChecker
from doodler import Doodler
from gameplatform import GamePlatform

doodler_filename = "underwater-right@2x.png"
platform_filename = "greenplatform.png"

game_width = 500
game_height = 800
platform_cache = 12
height_threshold = 500
platform_distance = 125

####################
root = Tk()
root.title("Doodle Jump")
root.resizable(width=False, height=False)

canvas = Canvas(root, width=game_width, height=game_height)

doodler = Doodler(doodler_filename, game_width / 2, game_height - 50, canvas)

counter = canvas.create_text(40, 40, text="0", font='Helvetica 16 bold')
running = True

platform_record = 0
height_record = 0
destruction_mark = 0

platforms = []
for i in range(0, platform_cache):
    print(i)
    platforms.append(
        GamePlatform(platform_filename, randint(0, game_width), game_height - platform_distance * i, canvas))

#################
def destroy_last_platform():
    del (platforms[0])


def generate_platform():
    platforms.append(
        GamePlatform(platform_filename, randint(0, game_width), game_height - 100 * platform_cache, canvas))


def go_up(distance):
    for p in platforms:
        p.down(distance)
    doodler.down(distance)


def add_platform_for_count(platform_to_add):
    doodler.platforms_list.append(platform_to_add)
    if len(doodler.platforms_list) > platform_cache:
        del (doodler.platforms_list[0])


while running:
    if keyboard.is_pressed('a'):
        doodler.left()
    if keyboard.is_pressed('d'):
        doodler.right()
    # print("x: " + str(doodler.x) + " y: " + str(doodler.y))

    if doodler.is_going_up:
        doodler.on_platform = False
        doodler.jump()
    else:
        if not doodler.on_platform:
            doodler.fall()
        for game_platform in platforms:
            if CollisionChecker.check_collision(game_platform, doodler):
                doodler.on_platform = True
                doodler.is_going_up = True
                if not doodler.platforms_list.__contains__(game_platform):
                    platform_record += 1
                    canvas.itemconfig(counter, text=str(platform_record))
                    add_platform_for_count(game_platform)
                doodler.current_jump_time = 0
                break

    if doodler.x < 0:
        doodler.to_right(game_width)
    if doodler.x > game_width:
        doodler.to_left(game_width)

    if doodler.y < game_height - height_threshold:
        height_record += game_height - height_threshold - doodler.y
        if height_record // platform_distance > destruction_mark:
            destruction_mark = height_record // platform_distance
            destroy_last_platform()
            generate_platform()

        go_up(game_height - height_threshold - doodler.y)

    if doodler.y > game_height:
        # game over
        break

    # print(platform_record)
    print("x: " + str(doodler.x))
    root.update()
    time.sleep(0.02)


##################

