import pygame
import random

# Constrants
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLOCK_SIZE = 20
SNAKE_SPEED = 8
class Snake:
    def __init__(self):
        self.snake_list = []
        self.snake_length = 1
        self.snake_head = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.snake_direction = "RIGHT"

    def move(self):
        if self.snake_direction == "RIGHT":
            self.snake_head[0] += BLOCK_SIZE
        elif self.snake_direction == "LEFT":
            self.snake_head[0] -= BLOCK_SIZE
        elif self.snake_direction == "UP":
            self.snake_head[1] -= BLOCK_SIZE
        elif self.snake_direction == "DOWN":
            self.snake_head[1] += BLOCK_SIZE

    def expand(self):
        self.snake_length += 1

    def draw(self, screen):
        for segment in self.snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

class Food:
    def __init__(self):
        self.food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.food_x, self.food_y, BLOCK_SIZE, BLOCK_SIZE])

def main():
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module
    # Load the sound file
    eat_sound = pygame.mixer.Sound("NomNomNom.mp3")

def main():
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer module
    # Load the sound file
    eat_sound = pygame.mixer.Sound("NomNomNom.mp3")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("saneks")
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.snake_direction != "RIGHT":
                    snake.snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.snake_direction != "LEFT":
                    snake.snake_direction = "RIGHT"
                elif event.key == pygame.K_UP and snake.snake_direction != "DOWN":
                    snake.snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake.snake_direction != "UP":
                    snake.snake_direction = "DOWN"

        # Move the sanek
        snake.move()
        # Check for collision with food
        if snake.snake_head[0] == food.food_x and snake.snake_head[1] == food.food_y:
            snake.expand()
            for x in range(100):
                food = Food()
            eat_sound.play()

          
        # Update sanek's body
        snake.snake_list.append(list(snake.snake_head))
        if len(snake.snake_list) > snake.snake_length:
            del snake.snake_list[0]

        # Check for collision with itself
        for segment in snake.snake_list[:-1]:
            if segment == snake.snake_head:
                game_over = True

        # Draw everything
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

        # Set game speed
        clock.tick(SNAKE_SPEED)
    pygame.quit()
    quit()
if __name__ == "__main__":
    main()














