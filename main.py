import pygame
import random
import math
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

# mixer.music.load('')
# mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
font = pygame.font.Font('freesansbold.ttf', 64)
player_surface = pygame.image.load('spaceship.png')
player = {
    'blit_object': player_surface,
    'x': 250,
    'y': 500,
    'x_speed': 0,
    'y_speed': 0
}
bad_guy_surface = pygame.image.load('bad_guy.png')
bad_guy = {
    'blit_object': bad_guy_surface,
    'x': 250,
    'y': 100,
    'x_speed': 1,
    'y_speed': 0
}

def shoot_bullet(player, bullets_we_want_to_blit):
    bullet_surface = pygame.image.load('bullet.png')
    bullet = {
        'blit_object': bullet_surface,
        'x': player['x'] + 50,
        'y': player['y'],
        'x_speed': 0,
        'y_speed': -3
    }
    bullets_we_want_to_blit.append(bullet)

bullets_we_want_to_blit = []

def blit_object(blittable_object):
    screen.blit(blittable_object['blit_object'], (blittable_object['x'], blittable_object['y']))

def move_object(blittable_object):
    blittable_object['x'] += blittable_object['x_speed']
    blittable_object['y'] += blittable_object['y_speed']

score = 0
def show_score():
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0, 0))

running = True
r = 255
g = 255
b = 255
while running:
    clock.tick(120)

    # RGB: red green blue
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
                shoot_bullet(player, bullets_we_want_to_blit)
                sound = pygame.mixer.Sound('./weapon_sound_effect.mid')
                sound.play
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player['x_speed'] = 0
            if event.key == pygame.K_RIGHT:
                player['x_speed'] = 0

    if player['x'] <= 50:
        player['x'] = 50
    if player['x'] >= 500:
        player['x'] = 500

    if bad_guy['x'] <= 50:
        bad_guy['x_speed'] = bad_guy['x_speed'] * -1
    if bad_guy['x'] >= 500:
        bad_guy['x_speed'] = bad_guy['x_speed'] * -1

    temp_list = []
    was_our_bad_guy_hit = False
    right_boundary = bad_guy['x'] + 50
    left_boundary = bad_guy['x'] - 50
    upper_boundary = bad_guy['y'] - 50
    lower_boundary = bad_guy['y'] + 50

    for bullet in bullets_we_want_to_blit:
        bullet_x = bullet['x']
        bullet_y = bullet['y']
        if bullet_x > left_boundary and bullet_x < right_boundary and bullet_y > upper_boundary and bullet_y < lower_boundary:
            was_our_bad_guy_hit = True
            score += 1

    if was_our_bad_guy_hit == False:
        blit_object(bad_guy)
        move_object(bad_guy)

    blit_object(player)
    move_object(player)

    for blittable_object in bullets_we_want_to_blit:
        blit_object(blittable_object)
        move_object(blittable_object)
        temp_list.append(blittable_object)

    bullets_we_want_to_blit = []
    for blittable_object in temp_list:
        if blittable_object['x'] > 0 and blittable_object['y'] > 0 and blittable_object['x'] < 600 and blittable_object['y'] < 600:
            bullets_we_want_to_blit.append(blittable_object)


    show_score()

    pygame.display.update()
