import pygame
import random

def newApple(snake):
    apple=(random.randrange(0, 40), random.randrange(0, 30))
    if apple in snake:
        return newApple(snake)
    else:
        return apple




pygame.init()



white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (186, 218, 85)

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')


def game_quit():
    pygame.quit()
    quit()

def game_over_screen(score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Score: '+ str(score), True, white, black)
    textRect = text.get_rect()
    textRect.center = (800 // 2, 600 // 2)
    over=False

    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over=True
                game_quit()
        display.fill(black)
        display.blit(text, textRect)
        pygame.display.update()



game_over = False

# x1 = 300
# y1 = 300

DOT_SIZE=20

x1_change = 0
y1_change = 0
dir='none';
old_dir='none';

clock = pygame.time.Clock()
snake = [(19, 14)]
apple = newApple(snake)

while not game_over:
    display.fill(black)
    # pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    old_dir=dir

    new_snake_head=(snake[0][0]+x1_change, snake[0][1]+y1_change) # New snake head

    if (new_snake_head in snake and x1_change!=0 or new_snake_head in snake and y1_change!=0):
        game_over=True
        game_over_screen(len(snake))
    elif new_snake_head[0]< 0 or new_snake_head[0]>=40 or new_snake_head[1]<0 or new_snake_head[1]>=30:
        game_over=True
        game_over_screen(len(snake))
    elif apple in snake:
        apple=newApple(snake)
        snake.insert(0, new_snake_head)
    else:
        snake.insert(0, new_snake_head)
        snake.pop(len(snake)-1)

    for body in snake: # Draw the snake
        pygame.draw.rect(display, green, [DOT_SIZE*body[0], DOT_SIZE*body[1], DOT_SIZE, DOT_SIZE])
    # Draw the apple
    pygame.draw.rect(display, red, [DOT_SIZE*apple[0], DOT_SIZE*apple[1], DOT_SIZE, DOT_SIZE])

    pygame.display.update()

    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            game_quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and old_dir != 'right':
                dir = 'left'
                x1_change = -1
                y1_change = 0
            elif event.key == pygame.K_RIGHT and old_dir != 'left':
                dir = 'right'
                x1_change = 1
                y1_change = 0
            elif event.key == pygame.K_UP and old_dir != 'down':
                dir = 'up'
                y1_change = -1
                x1_change = 0
            elif event.key == pygame.K_DOWN and old_dir != 'up':
                dir = 'down'
                y1_change = 1
                x1_change = 0

    # x1 += x1_change
    # y1 += y1_change


pygame.quit()
quit()

# Still need to add game over screen
