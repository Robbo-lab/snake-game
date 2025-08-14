import pygame
import sys
import random

# Starts the game
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 12  # Controls motion
BORDER_WIDTH = 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
RED = (220, 20, 60)
BLUE = (70, 130, 180)
GRAY = (128, 128, 128)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 2")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
eat_sound = pygame.mixer.Sound("eat.wav")

def reset_game():
    """Reset game to initial snake with a long tail"""
    start_x, start_y = WIDTH // 2, HEIGHT // 2
    snake = [(start_x - i * CELL_SIZE, start_y) for i in range(10)]  # Sets the tail size
    direction = (CELL_SIZE, 0)
    food = generate_food(snake)
    score = 0
    return snake, direction, food, score

def generate_food(snake):
    """Generate food that doesn't get created on the snake"""
    while True:
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))
        if food not in snake:
            return food

def draw_snake(snake):
    """Draw snake"""
    for i, segment in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, WHITE, (*segment, CELL_SIZE, CELL_SIZE), 1)

def draw_food(food):
    """Draw food with better visuals"""
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, WHITE, (*food, CELL_SIZE, CELL_SIZE), 1)

def draw_border():
    """Draw game border"""
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), BORDER_WIDTH)

def draw_score(score):
    """Draw current score"""
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    # Place it on the display
    screen.blit(score_text, (10, 10))

def draw_pause_screen():
    """Draw pause overlay"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    pause_text = font.render("PAUSED", True, WHITE)
    continue_text = small_font.render("Press SPACE to continue", True, WHITE)
    
    # Centre everything
    pause_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
    continue_rect = continue_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    
    screen.blit(pause_text, pause_rect)
    screen.blit(continue_text, continue_rect)

def draw_game_over(score):
    """Draw game over screen"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    # Create the game over message
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = small_font.render("Press R to restart or ESC to quit", True, WHITE)
    
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
    
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)

def move_snake(snake, direction):
    """Move snake forward"""
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    return [new_head] + snake[:-1]

def grow_snake(snake):
    """Grow snake by one segment"""
    return snake + [snake[-1]]

def check_collision(snake):
    """Check if snake collides with walls or itself"""
    head = snake[0]
    return (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    )

def get_opposite_direction(direction):
    """Get opposite direction to prevent reverse moves"""
    return (-direction[0], -direction[1])

# Set up the game
snake, direction, food, score = reset_game()
game_over = False
paused = False

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score = reset_game()
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif not paused:
                    # Get tyhe direction from the keystroke event - up/down/left/right
                    new_direction = None
                    if event.key == pygame.K_UP:
                        new_direction = (0, -CELL_SIZE)
                    elif event.key == pygame.K_DOWN:
                        new_direction = (0, CELL_SIZE)
                    elif event.key == pygame.K_LEFT:
                        new_direction = (-CELL_SIZE, 0)
                    elif event.key == pygame.K_RIGHT:
                        new_direction = (CELL_SIZE, 0)

                    if new_direction and new_direction != get_opposite_direction(direction):
                        direction = new_direction

    # Game logic
    if not paused and not game_over:
        # Take the direction event and the snkae & move
        snake = move_snake(snake, direction)

        # If you get the food grow the snake
        if snake[0] == food:
            snake = grow_snake(snake)
            score += 10
            food = generate_food(snake)

        # If we hit the side of the screen end the game
        if check_collision(snake):
            game_over = True

    # Draw everything
    screen.fill(BLACK)
    draw_border()
    draw_snake(snake)
    draw_food(food)
    draw_score(score)

    if paused and not game_over:
        draw_pause_screen()
    elif game_over:
        draw_game_over(score)

    pygame.display.flip()

pygame.quit()
sys.exit()