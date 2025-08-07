import pygame
import sys
import random

# Initialize
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 5
FPS = 12
BORDER_WIDTH = 2

# Colors
BLACK = (122, 89, 1)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
RED = (199, 193, 12)
BLUE = (70, 130, 180)
GRAY = (128, 128, 128)
FLASH_COLORS = [RED, GREEN, BLUE, WHITE, GRAY, (255, 0, 255), (0, 255, 255)]

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Annoying Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Rotation timing
rotation_angle = 0
last_rotation_time = pygame.time.get_ticks()
ROTATE_INTERVAL_MS = 500  # 0.5 seconds

def reset_game():
    start_x, start_y = WIDTH // 2, HEIGHT // 2
    snake = [(start_x - i * CELL_SIZE, start_y) for i in range(10)]
    direction = (CELL_SIZE, 0)
    food = generate_food(snake)
    fake_food = generate_food(snake + [food])
    score = 0
    return snake, direction, food, fake_food, score

def generate_food(snake):
    while True:
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))
        if food not in snake:
            return food

def draw_snake(snake, surface):
    for i, segment in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(surface, color, (*segment, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, WHITE, (*segment, CELL_SIZE, CELL_SIZE), 1)

def draw_food(food, surface):
    pygame.draw.rect(surface, RED, (*food, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(surface, WHITE, (*food, CELL_SIZE, CELL_SIZE), 1)

def draw_border(surface):
    pygame.draw.rect(surface, WHITE, (0, 0, WIDTH, HEIGHT), BORDER_WIDTH)

def draw_score(score, surface):
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))

def draw_pause_screen(surface):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))
    pause_text = font.render("PAUSED", True, WHITE)
    continue_text = small_font.render("Press SPACE to continue", True, WHITE)
    surface.blit(pause_text, pause_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
    surface.blit(continue_text, continue_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))

def draw_game_over(score, surface):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))
    game_over_text = font.render("HE IS COMING, HE FEELS NO FEAR, ONLY YEET", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = small_font.render("Press R to restart or ESC to quit", True, WHITE)
    surface.blit(game_over_text, game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40)))
    surface.blit(score_text, score_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    surface.blit(restart_text, restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40)))

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    return [new_head] + snake[:-1]

def grow_snake(snake, segments=15):
    for _ in range(segments):
        snake.append(snake[-1])
    return snake

def check_collision(snake):
    head = snake[0]
    return (
        head in snake[1:] or
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    )

def get_opposite_direction(direction):
    return (-direction[0], -direction[1])

def move_food_away(food, snake_head):
    fx, fy = food
    hx, hy = snake_head
    dx = CELL_SIZE if fx < hx else -CELL_SIZE
    dy = CELL_SIZE if fy < hy else -CELL_SIZE
    new_food = ((fx + dx) % WIDTH, (fy + dy) % HEIGHT)
    return new_food

# Setup
snake, direction, food, fake_food, score = reset_game()
game_over = False
paused = False

running = True
while running:
    clock.tick(FPS)

    # Update rotation angle every 0.5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_rotation_time >= ROTATE_INTERVAL_MS:
        rotation_angle = (rotation_angle + 10) % 360
        last_rotation_time = current_time

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, fake_food, score = reset_game()
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif not paused:
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

    if not paused and not game_over:
        snake = move_snake(snake, direction)

        if snake[0] == food:
            snake = grow_snake(snake)
            score += 100
            food = generate_food(snake)
            fake_food = generate_food(snake + [food])

        if snake[0] == fake_food:
            score -= 300
            snake = snake[:-10] if len(snake) > 20 else snake
            fake_food = generate_food(snake + [food])

        food = move_food_away(food, snake[0])

        if check_collision(snake):
            game_over = True

        score -= 1

    # Draw everything to a surface
    game_surface = pygame.Surface((WIDTH, HEIGHT))
    bg_color = random.choice(FLASH_COLORS)
    game_surface.fill(bg_color)

    draw_border(game_surface)
    draw_snake(snake, game_surface)
    draw_food(food, game_surface)
    draw_food(fake_food, game_surface)
    draw_score(score, game_surface)

    if paused and not game_over:
        draw_pause_screen(game_surface)
    elif game_over:
        draw_game_over(score, game_surface)

    # Rotate and display
    rotated_surface = pygame.transform.rotate(game_surface, rotation_angle)
    rotated_rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(rotated_surface, rotated_rect.topleft)

    pygame.display.flip()

pygame.quit()
sys.exit()
