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
SEA = (1, 18, 18)
WHITE = (255, 255, 255)
EEL = (196,156,8,255)
DARK_EEL = (114,113,47,255)
CRAB = (222, 101, 31    )
BLUE = (70, 130, 180)
GRAY = (128, 128, 128)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
<<<<<<< HEAD
pygame.display.set_caption("Eel Game 2")
=======
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 50)

def reset_game():
<<<<<<< HEAD
    """Reset game to initial eel with a long tail"""
=======
    start_x, start_y = WIDTH // 2, HEIGHT // 2
    eel = [(start_x - i * CELL_SIZE, start_y) for i in range(10)]  # Sets the tail size
    direction = (CELL_SIZE, 0)
    food = generate_food(eel)
    score = 0
    return eel, direction, food, score

def generate_food(eel):
    """Generate food that doesn't get created on the eel"""
    while True:
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))
        if food not in eel:
            return food

def draw_eel(eel):
    """Draw eel"""
    for i, segment in enumerate(eel):
        color = DARK_EEL if i == 0 else EEL
        pygame.draw.rect(screen, color, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, WHITE, (*segment, CELL_SIZE, CELL_SIZE), 1)

def draw_food(food):
    """Draw food with better visuals"""
    pygame.draw.rect(screen, CRAB, (*food, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, WHITE, (*food, CELL_SIZE, CELL_SIZE), 1)

def draw_border():
    """Draw game border"""
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT), BORDER_WIDTH)

def draw_score(score):
    """Draw current score"""
    score_text = small_font.render(f"Crabs Eaten: {score}", True, WHITE)
    # Place it on the display
    screen.blit(score_text, (10, 10))

def draw_pause_screen():
    """Draw pause overlay"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(SEA)
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
    overlay.fill(SEA)
    screen.blit(overlay, (0, 0))
    
    # Create the game over message
<<<<<<< HEAD
    game_over_text = font.render("GAME OVER", True, CRAB)
    score_text = font.render(f"Crabs Consumed: {score}", True, WHITE)
    restart_text = small_font.render("Press R to continue eating or ESC to flee", True, WHITE)
=======
    
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
    
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)

def move_eel(eel, direction):
    """Move eel forward"""
    head_x, head_y = eel[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    return [new_head] + eel[:-1]

def grow_eel(eel):
    """Grow eel by one segment"""
    return eel + [eel[-1]]

def check_collision(eel):
    """Check if eel collides with walls or itself"""
    head = eel[0]
    return (
        head in eel[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    )

def get_opposite_direction(direction):
    """Get opposite direction to prevent reverse moves"""
    return (-direction[0], -direction[1])

# Set up the game
eel, direction, food, score = reset_game()
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
                FPS = 12
                if event.key == pygame.K_r:
                    eel, direction, food, score = reset_game()
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif not paused:
                    # Get the direction from the keystroke event - up/down/left/right
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
<<<<<<< HEAD
        # Take the direction event and the snkae & move
        eel = move_eel(eel, direction)

        # If you get the food grow the eel
        if eel[0] == food:
            eel = grow_eel(eel)
            score += 10
<<<<<<< HEAD
            food = generate_food(eel)


        # If we hit the side of the screen end the game
        if check_collision(eel):
            game_over = True

    # Draw everything
    screen.fill(SEA)
    draw_border()
    draw_eel(eel)
    draw_food(food)
    draw_score(score)

    if paused and not game_over:
        draw_pause_screen()
    elif game_over:
        draw_game_over(score)

    pygame.display.flip()

pygame.quit()
sys.exit()
