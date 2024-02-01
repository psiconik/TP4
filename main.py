import arcade
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1060
WINDOW_TITLE = "TP4"

COLORS = [arcade.color.ARMY_GREEN, arcade.color.VIOLET, arcade.color.GREEN, arcade.color.RED, arcade.color.BLUE,
           arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.AFRICAN_VIOLET, arcade.color.AIR_SUPERIORITY_BLUE, arcade.color.AQUA, arcade.color.ANTIQUE_RUBY ]



class rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.color = random.choice(COLORS)
        self.height = random.randint(10, 30)
        self.width = random.randint(10, 30)
        self.angle = random.randint(0, 90)

    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < self.height:
            self.change_x *= -1
        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
        if self.y < self.height:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1


    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, color=self.color, tilt_angle=self.angle)

class Cercle:
    def __init__(self, x, y):
        self.rayon =30
        self.couleur = random.choice(COLORS)
        self.centre_x = x
        self.centre_y = y
        self.change_x = 15
        self.change_y = 15

    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < 15:
            self.change_x *= -1
        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *=-1
        if self.centre_y < self.rayon:
            self.change_y *= -1
        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1


    def on_draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.couleur)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercise #1")
        self.list_Cercles = []
        self.list_Rectangles = []

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            cercle = Cercle(x,y)
            self.list_Cercles.append(cercle)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangles = rectangle(x,y)
            self.list_Rectangles.append(rectangles)
    def on_draw(self):
        arcade.start_render()
        for i in self.list_Cercles:
            i.on_draw()
        for i in self.list_Rectangles:
            i.on_draw()

    def on_update(self, delta_time: float):
        for cercle in self.list_Cercles:
            cercle.on_update()
        for rectangles in self.list_Rectangles:
            rectangles.on_update()

def main():
    my_game = MyGame()


    arcade.run()


main()

