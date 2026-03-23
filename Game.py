#Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 800  # Set desired screen width
SCREEN_HEIGHT = 600  # Set desired screen height
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Comic Sans MS", 70)
font_small = pygame.font.SysFont("Franklin Gothic Medium", 40)
game_over = font.render("Game Over", True, BLACK)

# Load game over image and resize
game_over_image = pygame.image.load("gameoverss.png")
game_over_image = pygame.transform.scale(game_over_image, (450, 500))

# Load the background image
background = pygame.image.load("backgroundspace.png")

# Resize the background image to match the screen size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a resizable screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Space")

# Set up background music
pygame.mixer.music.load("ARCADE SOUNDS TRON.mp3")
pygame.mixer.music.play(-1)  # -1 to play the music in a loop


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = speed

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class NormalEnemy(Enemy):
    def __init__(self):
        super().__init__("EnemyA.png", 5) # Creates a NormalEnemy with the image "EnemyA.png" and health 5.



class FastEnemy(Enemy):
    def __init__(self):
        super().__init__("EnemyB.png", 8) # Creates a FastEnemy with the image "EnemyB.png" and health 8.




class SlowEnemy(Enemy):
    def __init__(self):
        super().__init__("EnemyC.png", 3) # Creates a SlowEnemy with the image "EnemyC.png" and health 3.


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and scale the player image
        self.image = pygame.image.load("yellow.png")
        self.image = pygame.transform.scale(self.image, (60, 100))

        # Set the initial position of the player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        # Get the currently pressed keys
        pressed_keys = pygame.key.get_pressed()

        # Move the player left if it's not at the left edge of the screen and the left arrow key is pressed
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Move the player right if it's not at the right edge of the screen and the right arrow key is pressed
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        # Move the player up if it's not at the top edge of the screen and the up arrow key is pressed        
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)

        # Move the player down if it's not at the bottom edge of the screen and the down arrow key is pressed
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                  


#Setting up Sprites        
P1 = Player()
E1 = NormalEnemy()
E2 = FastEnemy()  # Instantiate a FastEnemy object
E3 = SlowEnemy()  # Instantiate a SlowEnemy object

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)  # Add FastEnemy to the enemies group
enemies.add(E3)  # Add SlowEnemy to the enemies group

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)  # Add FastEnemy to the all_sprites group
all_sprites.add(E3)  # Add SlowEnemy to the all_sprites group

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Initializing the paused variable
paused = False

# Load the previous high score from a file
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Save the new high score to a file
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

# Load the previous high score
high_score = load_high_score()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == KEYDOWN:
            if event.key == K_p:
                paused = not paused  # Toggle the paused state

    if not paused:
        
        # Move and draw all entities in the game
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)

        DISPLAYSURF.blit(background, (0, 0))

        # Check for collision with enemies
        if pygame.sprite.spritecollideany(P1, enemies):
            # Play a sound effect and display game over message
            pygame.mixer.Sound('CRYING MEME.mp3').play()
            time.sleep(1)

            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over_image, (100, 200))
            DISPLAYSURF.blit(game_over, (30, 250))

            pygame.display.update()

            # Remove all entities and exit the game after a delay
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    else:
        # Display a paused message if the game is paused
        paused_text = font_small.render("Paused", True, RED)
        DISPLAYSURF.blit(paused_text, (160, 250))
        pygame.display.update()

    FramePerSec.tick(FPS)

    DISPLAYSURF.blit(background, (0, 0))

    # Display the score and high score
    scores = font_small.render(f"Score: {SCORE}", True, RED)
    high_score_text = font_small.render(f"High Score: {high_score}", True, RED)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(high_score_text, (10, 50))

    # Move and draw all entities in the game
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    # Update the high score if the current score is higher
    if SCORE > high_score:
        high_score = SCORE
        save_high_score(high_score)

    pygame.display.update()
    FramePerSec.tick(FPS)