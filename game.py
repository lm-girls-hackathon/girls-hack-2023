import arcade

SCREEN_LEN = 512
WINDOW_LEN = int(SCREEN_LEN * 1.25)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Pac Man")
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.character = arcade.Sprite(
            "images/character.png",
            center_x=WINDOW_LEN // 2,
            center_y=WINDOW_LEN // 2,
            scale=0.50,
        )

    def on_draw(self):
        arcade.start_render()
        self.character.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.character.center_x += 5
        elif symbol == arcade.key.LEFT:
            self.character.center_x -= 5
        elif symbol == arcade.key.UP:
            self.character.center_y += 5
        elif symbol == arcade.key.DOWN:
            self.character.center_y -= 5
