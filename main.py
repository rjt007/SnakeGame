import pygame
import random
pygame.init()
#Creating window for game
screen_width = 900
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My Game")
pygame.display.update()
clock = pygame.time.Clock()
#colors
white = (255,255,255)
red = (255, 0, 0)
black = (0, 0, 0)
random_color = (200, 154, 20)

#To update score on gamewindow
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

#For increasing lenth of snake upon eating each time
def plotsnake(gamewindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x, y, snake_size, snake_size])


#Welcome Screen
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome To Snakes", red, 260, 150)
        text_screen("Press Space Bar To Start Game", red, 170, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(40)

#Creating Gameloop
def gameloop():
    # Game specific variables
    game_over = False
    exit_game = False
    snake_x = 65
    snake_y = 75
    veloc_x = 0
    veloc_y = 0
    init_velocity = 5
    food_x = random.randint(40, screen_width // 1.4)
    food_y = random.randint(40, screen_height // 1.4)
    snake_size = 15
    score = 0
    fps = 40
    snake_lst = []
    snake_length = 1
    clock = pygame.time.Clock()
    with open("highscore.txt","r") as f:
        highscore = f.read()
    while not exit_game:
        # pass
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter to continue", red, 100, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:   #K_RETURN means Enter key is pressed
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        veloc_x = init_velocity
                        veloc_y = 0
                    if event.key == pygame.K_LEFT:
                        veloc_x = -init_velocity
                        veloc_y = 0
                    if event.key == pygame.K_UP:
                        veloc_y = -init_velocity
                        veloc_x = 0
                    if event.key == pygame.K_DOWN:
                        veloc_y = init_velocity
                        veloc_x = 0

            snake_x += veloc_x
            snake_y += veloc_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(25, screen_height // 2)
                food_y = random.randint(25, screen_height // 2)
                snake_length += 5
                if score>int(highscore):
                    highscore = score


            gamewindow.fill(white)
            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("HighScore: " + str(highscore), red, 600, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            if len(snake_lst) > snake_length:
                del snake_lst[0]
            if snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0:
                game_over = True
            if head in snake_lst[:-1]:
                game_over = True
            plotsnake(gamewindow, black, snake_lst, snake_size)
            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()