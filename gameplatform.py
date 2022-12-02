from tkinter import *


class GamePlatform:

    def __init__(self, sprite_filename, x, y, master_canvas):
        self.canvas = master_canvas
        self.sprite = PhotoImage(file=sprite_filename)
        self.x = x
        self.y = y
        self.id = self.canvas.create_image(x, y, anchor=S, image=self.sprite)
        self.canvas.pack()

    #Возвращает левую границу, правую границу, верхнюю границу
    def get_borders(self):
        half_width = self.sprite.width()/2
        height = self.sprite.height()
        return self.x - half_width, self.x + half_width, self.y - height, self.y

    def down(self, distance):
        self.y +=distance
        self.canvas.move(self.id, 0, distance)
