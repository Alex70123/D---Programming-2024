import random
import pygame as pg
# --CONSTANTS--
WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
NUM_COINS = 100
NUM_ENEMIES = 5  # Define the number of enemies
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/mario.webp")
        self.rect = self.image.get_rect()
    def update(self):
        """Updates the location of sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/bowser.png") # Example surface for the enemy sprite
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        self.vel_x = random.choice([-3, 3])  # Random initial x velocity
        self.vel_y = random.choice([-3, 3])  # Random initial y velocity

        GOOMBA_IMAGE = pg.image.load("./Images/bowser.png")

         # Scale the image down in half
        GOOMBA_IMAGE = pg.transform.scale(
        GOOMBA_IMAGE, (GOOMBA_IMAGE.get_width() // 10000, GOOMBA_IMAGE.get_height() // 10000)
        )


    def update(self):
        # Update position based on velocity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vel_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vel_y *= -1
def start():
    """Environment Setup and Game Loop"""
    pg.init()
    pg.mouse.set_visible(False)
    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()
    score = 0
    # Load background image
    background = pg.image.load("./Images/mariobg.jpg").convert_alpha()
    background = pg.transform.scale(background, SCREEN_SIZE)
    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    # Coin sprites
    coin_sprites = pg.sprite.Group()
    # Enemy sprites
    enemy_sprites = pg.sprite.Group()
    # Creating enemy sprites
    for _ in range(NUM_ENEMIES):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
    # Creating coin sprites
    for _ in range(NUM_COINS):
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)
    # Create a player and store it in a variable
    player = Player()
    all_sprites.add(player)
    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")
    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        # --- Update the world state
        all_sprites.update()
       


        # Collision between player and coin_sprites
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)
        for coin in coins_collided:
            # Increase the score by 1
            score += 1
            print(score)
        # If the coin_sprites group is empty, respawn all the coins
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COINS):
                coin = Coin()
                all_sprites.add(coin)
                coin_sprites.add(coin)
        # --- Draw items
        screen.blit(background, (0, 0))  # Draw background image
        all_sprites.draw(screen)
        # Update the screen with anything new
        pg.display.flip()
        # --- Tick the Clock
        clock.tick(60)  # 60 fps
def main():
    start()
if __name__ == "__main__":
    main()
