import arcade
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1060
WINDOW_TITLE = "TP4"

COLORS = []

class Cercle:
    def __init__(self, x, y):
        self.rayon = 15
        self.couleur = COLORS
        self.centre_x = x
        self.centre_y = y
        self.change_x = 15
        self.change_y = 15

    def on_update:
        cercle_x += 3
        cercle_y += 3

        if self.centre_x < 15:
            pass
        if cercle_x > SCREEN_WIDTH - rayon_cercle:
            pass
        if cercle_y < rayon_cercle:
            pass
        if cercle_y > SCREEN_HEIGHT - rayon_cercle:
            pass

    def setup(self):
        on_mouse_press: arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))
        pass


    def on_draw(self):
        arcade.start_render()

        pass

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercise #1")
        pass

    def setup(self):
        on_mouse_press: arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))
        pass


    def on_draw(self):
        arcade.start_render()

        pass


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()

