import arcade
import time

WINDOW_LEN = 512
BOARD_LEN = 64
SQUARE_LEN = WINDOW_LEN // BOARD_LEN


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Pac Man")
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.direction = True

        self.character = arcade.Sprite(
            "images/pacman/Pacman_right.png",
            center_x=WINDOW_LEN // 2,
            scale=4,
        )

        self.cherry = arcade.Sprite(
            "images/objects/Fruit_Cherry.png",
            center_x=WINDOW_LEN // 2,
            center_y=WINDOW_LEN,
            scale=4
        )

        self.character.center_y = self.character.height // 2

    def on_draw(self):
        arcade.start_render()
        self.character.draw()
        self.cherry.draw()

        if self.direction and self.character.center_x + self.character.width // 2 < WINDOW_LEN:
            self.character.center_x += 1
        elif self.character.center_x - self.character.width // 2 > 0:
            self.character.center_x -= 1
        self.cherry.center_y -= 1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.character.turn_right(theta=180)
            self.direction = True
        else:
            self.character.turn_left(theta=180)
            self.direction = False


def map_position(x):
    return x * SQUARE_LEN


def map_coord(x):
    return x // SQUARE_LEN
