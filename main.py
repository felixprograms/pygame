import pygame
import random
import math
from pygame import mixer

pygame.init()


screen = pygame.display.set_mode((2000, 1569))


# mixer.music.load('')
# mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
font = pygame.font.Font('freesansbold.ttf', 64)

player = {
    'blit_object': pygame.image.load('spaceship.png'),
    'x': 500,
    'y': 1200,
    'x_speed': 0,
    'y_speed': 0
}

bad_guy = {
    'blit_object': pygame.image.load('bad_guy.png'),
    'x': 100,
    'y': 0,
    'x_speed': 10,
    'y_speed': 0
}

def shoot_bullet(player, objects_that_we_want_to_blit):
    bullet = {
        'blit_object': pygame.transform.rotate(pygame.image.load('bullet.png'), -90),
        'x': player['x'] + 150,
        'y': player['y'],
        'x_speed': 0,
        'y_speed': -10
    }
    objects_that_we_want_to_blit.append(bullet)


score = 100

objects_that_we_want_to_blit = [
    player,
    # bad_guy
]

def blit_object(blittable_object):
    screen.blit(blittable_object['blit_object'], (blittable_object['x'], blittable_object['y']))

def move_object(blittable_object):
    blittable_object['x'] += blittable_object['x_speed']
    blittable_object['y'] += blittable_object['y_speed']

# def show_score():
#     score_text = font.render("Score: " + str(score), True, (250, 250, 250))
#     screen.blit(score_text, (150, 100))

running = True
r = 255
g = 255
b = 255
while running:
    # rgb
    # red green blue
    screen.fill((r, g, b))

    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player['x_speed'] = -8
            if event.key == pygame.K_RIGHT:
                player['x_speed'] = 8
            if event.key == 13:
                shoot_bullet(player, objects_that_we_want_to_blit)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player['x_speed'] = 0
            if event.key == pygame.K_RIGHT:
                player['x_speed'] = 0

    if player['x'] <= 50:
        player['x'] = 50
    if player['x'] >= 1500:
        player['x'] = 1500

    if bad_guy['x'] <= 50:
        bad_guy['x_speed'] = bad_guy['x_speed'] * -1
    if bad_guy['x'] >= 1500:
        bad_guy['x_speed'] = bad_guy['x_speed'] * -1

    temp_list = []
    for blittable_object in objects_that_we_want_to_blit:
        blit_object(blittable_object)
        move_object(blittable_object)
        temp_list.append(blittable_object)

    objects_that_we_want_to_blit = []
    for blittable_object in temp_list:
        if blittable_object['x'] > 0 and blittable_object['y'] > 0 and blittable_object['x'] < 2000 and blittable_object['y'] < 1569:
            objects_that_we_want_to_blit.append(blittable_object)


    # show_score()

    pygame.display.update()
