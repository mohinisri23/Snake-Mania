import pygame
from .snake import Snake
from .food import Food
from .utils import screen, clock, font, C, bg, W, H

def main():
    snake = Snake()
    food = Food()
    score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN and game_over:
                    # restart game
                    snake = Snake()
                    food = Food()
                    score = 0
                    game_over = False

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_UP]:
                snake.turn((0, -C))
            elif keys[pygame.K_DOWN]:
                snake.turn((0, C))
            elif keys[pygame.K_LEFT]:
                snake.turn((-C, 0))
            elif keys[pygame.K_RIGHT]:
                snake.turn((C, 0))

            snake.move()

            # Check collision with food
            head = snake.get_head()
            if pygame.Rect(*head, C, C).colliderect(food.rect):
                snake.grow()
                score += 1
                food = Food()  # respawn new food

            # Check collision with walls or itself
            hx, hy = head
            if hx < 0 or hx >= W or hy < 0 or hy >= H or head in snake.body[1:]:
                game_over = True

        # --- Drawing ---
        screen.blit(bg, (0, 0))

        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if game_over:
            over_text = font.render("GAME OVER - Press Enter to Restart or ESC to Quit", True, (255, 0, 0))
            screen.blit(over_text, (W // 2 - over_text.get_width() // 2, H // 2))

        pygame.display.flip()
        clock.tick(10)  # snake speed

    pygame.quit()
