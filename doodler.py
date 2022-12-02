from tkinter import *

move_speed = 11
jump_speed = 15
fall_speed = 15

jump_time = 20

ground_length = 20


class Doodler:

    def __init__(self, sprite_filename, x, y, master_canvas):
        self.canvas = master_canvas

        self.sprite = PhotoImage(file=sprite_filename)
        self.x = x
        self.y = y
        self.id = self.canvas.create_image(x, y, anchor=S, image=self.sprite)
        self.canvas.pack()
        self.is_going_up = True
        self.current_jump_time = 0
        self.on_platform = True

        self.rect_collider = self.canvas.create_rectangle(self.x - ground_length, self.y - 2, self.x + ground_length,
                                                          self.y + 2, fill="white", outline="white")

        self.platforms_list = []

    def left(self):
        self.x -= move_speed
        self.canvas.move(self.id, -move_speed, 0)
        self.canvas.move(self.rect_collider, -move_speed, 0)

    def right(self):
        self.x += move_speed
        self.canvas.move(self.id, move_speed, 0)
        self.canvas.move(self.rect_collider, move_speed, 0)

    def jump(self):
        self.current_jump_time += 1
        self.y -= jump_speed
        self.canvas.move(self.id, 0, -jump_speed)
        self.canvas.move(self.rect_collider, 0, -jump_speed)
        if self.current_jump_time > jump_time:
            self.is_going_up = False

    def fall(self):
        self.current_jump_time -= 1
        self.y += fall_speed
        self.canvas.move(self.id, 0, fall_speed)
        self.canvas.move(self.rect_collider, 0, fall_speed)

    def down(self, distance):
        self.y += distance
        self.canvas.move(self.id, 0, distance)
        self.canvas.move(self.rect_collider, 0, distance)

    def to_right(self, game_width):
        self.x += game_width
        self.canvas.move(self.id, game_width, 0)
        self.canvas.move(self.rect_collider, game_width, 0)

    def to_left(self, game_width):
        self.x -=game_width
        self.canvas.move(self.id, -game_width, 0)
        self.canvas.move(self.rect_collider, -game_width, 0)


