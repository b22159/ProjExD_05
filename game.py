import pygame as pg
import random
import sys
import os

pg.init()

WIDTH, HEIGHT = 400, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("車ゲーム")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height -20
player_speed = 5

obstacle_width, obstacle_height = 50, 50
obstacle_speed = 5


def draw_player(x, y):
    pg.draw.rect(screen, WHITE, [x, y, player_width, player_height])
def draw_obstacle(x, y):
    pg.draw.rect(screen, RED, [x, y, obstacle_width, obstacle_height])

def drop_gasolines(gasoline):
        """
        ガソリンを生成する
        """
        deplay = random.randint(1, 5)
        if len(gasoline) < 10 and random.randint(1, deplay) == 1:
            x_gass = random.randint(0, WIDTH - 30)
            y_gass = 0
            gasoline.append([x_gass, y_gass])

def draw_gasolines(gasoline):
    for gas in gasoline:
        img = pg.image.load("fig/oil.PNG")
        gasoline_img = pg.transform.scale(img, (50, 50))
        screen.blit(gasoline_img, (gas[0], gas[1]))

def game():
    clock = pg.time.Clock()

    obstacles = []
    score = 0
    global player_x
    gasoline = []

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        keys = pg.key.get_pressed()
        player_x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * player_speed

        player_x = max(0, min(WIDTH - player_width, player_x))

        if random.randint(1, 10) == 1:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y])

        for obstacle in obstacles:
            obstacle[1] +- obstacle_speed
            if(
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                print(f"Game Over! Score: {score}")
                pg.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        draw_player(player_x, player_y)

        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])
        
        drop_gasolines(gasoline)
        draw_gasolines(gasoline)

        score += 1

        pg.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    game()
        
