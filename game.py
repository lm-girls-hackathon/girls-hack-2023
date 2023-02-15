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

        if self.direction:
            self.character.center_x += 1
        else:
            self.character.center_x -= 1
        self.cherry.center_y -= 1

        self.character.draw()
        self.cherry.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.character.turn_right(theta=180)
            self.direction = True
        else:
            self.character.turn_left(theta=180)
            self.direction = False

    def die(self):
        self.character = arcade.Sprite(
            "images/pacman/Pacman_Death_01.png",
            center_x=WINDOW_LEN // 2,
            center_y=self.character.center_y,
            scale=4
        )
        time.sleep(0.5)
        self.character = arcade.Sprite(
            "images/pacman/Pacman_Death_02.png",
            center_x=WINDOW_LEN // 2,
            center_y=self.character.center_y,
            scale=4
        )


def map_position(x):
    return x * SQUARE_LEN


def map_coord(x):
    return x // SQUARE_LEN
