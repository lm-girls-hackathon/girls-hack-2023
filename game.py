import arcade

WINDOW_LEN = 512


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_LEN, WINDOW_LEN, "Girls Hackathon")  # set up a screen with this width/length and title
        arcade.set_background_color(arcade.color.ASH_GREY)  # there are many colors to choose from!
        self.direction = True  # True if the character is moving forwards, False if moving backwards

        self.cherry = arcade.Sprite(
            "images/objects/Fruit_Cherry.png",  # path to the image you want your sprite to appear as
            center_x=WINDOW_LEN // 2,  # position on screen
            center_y=WINDOW_LEN,
            scale=4  # how big? scales less than 1 will make the sprite smaller
        )

        self.character = arcade.Sprite(
            "images/pacman/Pacman_right.png",
            center_x=WINDOW_LEN // 2,
            scale=4,
        )

        self.character.center_y = self.character.height // 2

    def on_draw(self):  # this function is called many times per second to display your screen
        arcade.start_render()

        self.character.draw()  # use the .draw() method to draw a sprite, otherwise it won't show up
        self.cherry.draw()

        arcade.draw_text(  # this is how you draw text on the screen!
            "Welcome to my game!",
            start_x=WINDOW_LEN // 2,
            start_y=WINDOW_LEN // 2,
            color=arcade.color.AIR_FORCE_BLUE,
            font_size=20,
            font_name="Kenney Blocks",
            anchor_x="center",
        )

        if self.character.collides_with_sprite(self.cherry):
            pass  # this is how you tell if two sprites are touching each other!

        # update the position of your sprites!
        if self.direction and self.character.center_x + self.character.width // 2 < WINDOW_LEN:  # checks that the sprite is not going off of the screen
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

