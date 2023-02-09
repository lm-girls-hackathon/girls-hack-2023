import arcade

WINDOW_LEN = 512
BOARD_LEN = 64
SQUARE_LEN = WINDOW_LEN // BOARD_LEN


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Pac Man")
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.board = [[0 for _ in range(64)] for _ in range(64)]
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                if i == 50 or j == 50 or i == 20:
                    self.board[j][i] = 1

        self.character = arcade.Sprite(
            "images/character.png",
            center_x=WINDOW_LEN // 2,
            center_y=WINDOW_LEN // 2,
            scale=0.50,
        )

    def on_draw(self):
        arcade.start_render()
        self.draw_squares()
        self.character.draw()

    def draw_squares(self):
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                x = map_position(i)
                y = map_position(j)
                if self.board[j][i] == 1:
                    arcade.draw_lrtb_rectangle_filled(
                        x,
                        x + SQUARE_LEN,
                        y + SQUARE_LEN,
                        y,
                        color=arcade.color.BLACK,
                    )

    def on_key_press(self, symbol: int, modifiers: int):
        x_min = int(self.character.center_x - self.character.width / 2)
        x_max = int(self.character.center_x + self.character.width / 2)
        y_min = int(self.character.center_y - self.character.height / 2)
        y_max = int(self.character.center_y + self.character.height / 2)
        move = True
        if symbol in (arcade.key.RIGHT, arcade.key.UP):
            diff = 5
        else:
            diff = -5
        if symbol in (arcade.key.RIGHT, arcade.key.LEFT):
            for i in range(x_min + diff, x_max + diff):
                for j in range(y_min, y_max):
                    if self.board[map_coord(j)][map_coord(i)] == 1:
                        move = False
            if move:
                self.character.center_x += diff
        elif symbol in (arcade.key.UP, arcade.key.DOWN):
            for i in range(x_min, x_max):
                for j in range(y_min + diff, y_max + diff):
                    if self.board[map_coord(j)][map_coord(i)] == 1:
                        move = False
            if move:
                self.character.center_y += diff


def map_position(x):
    return x * SQUARE_LEN


def map_coord(x):
    return x // SQUARE_LEN
