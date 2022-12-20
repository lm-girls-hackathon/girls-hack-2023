import arcade

SQR_LEN = 35
SCREEN_LEN = 512
WINDOW_LEN = int(SCREEN_LEN * 1.25)
LIST_LEN = SCREEN_LEN // SQR_LEN
EDGE = SQR_LEN // 16


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Pac Man")
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_mouse_press(self, x, y, _button, _):
        if _button == arcade.MOUSE_BUTTON_RIGHT:
            print("pressed right")

