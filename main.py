import pygame
import random
import math
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
soundObject = pygame.mixer.Sound('1.wav')
pygame.display.set_caption("Space Invaders")
font = pygame.font.Font('freesansbold.ttf', 32)


player_surface = pygame.image.load('player.png')
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

friendly_bullets = []
unfriendly_bullets = []


def shoot_bullet(player, friendly_bullets):
    bullet_surface = pygame.image.load('bullet.png')
    bullet = {
        'blit_object': bullet_surface,
        'x': player['x'] + 50,
        'y': player['y'],
        'x_speed': 0,
        'y_speed': -4
    }
    soundObject.play()
    friendly_bullets.append(bullet)

def bad_guy_shoot_bullet(bad_guy, unfriendly_bullets):
    bullet_surface = pygame.image.load('bullet.png')
    bullet_surface = pygame.transform.rotate(bullet_surface, 180)
    bullet = {
        'blit_object': bullet_surface,
        'x': bad_guy['x'] + 50,
        'y': bad_guy['y'],
        'x_speed': 0,
        'y_speed': 4
    }
    unfriendly_bullets.append(bullet)

def blit_object(blittable_object):
    screen.blit(blittable_object['blit_object'], (blittable_object['x'], blittable_object['y']))

def move_object(blittable_object):
    blittable_object['x'] += blittable_object['x_speed']
    blittable_object['y'] += blittable_object['y_speed']

score = 0
def show_score():
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (0, 0))

lives = 3
def show_lives():
    lives_text = font.render("Score: " + str(lives), True, (0, 0, 0))
    screen.blit(lives_text, (0, 0))


running = True
r = 255
g = 255
b = 255
last_bullet_time = None
last_bad_guy_bullet_time = None
while running:
    clock.tick(70)
    screen.fill((r, g, b))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player['x_speed'] = -8
            if event.key == pygame.K_RIGHT:
                player['x_speed'] = 8
            if event.key == 13:
                if last_bullet_time == None or pygame.time.get_ticks() - last_bullet_time > 500:
                    shoot_bullet(player, friendly_bullets)
                    last_bullet_time = pygame.time.get_ticks()

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
    was_our_player_hit = False


    right_boundary = bad_guy['x'] + 50
    left_boundary = bad_guy['x'] - 50
    upper_boundary = bad_guy['y'] - 50
    lower_boundary = bad_guy['y'] + 50

    for bullet in friendly_bullets:
        bullet_x = bullet['x']
        bullet_y = bullet['y']
        if bullet_x > left_boundary and bullet_x < right_boundary and bullet_y > upper_boundary and bullet_y < lower_boundary:
            was_our_bad_guy_hit = True
            score += 1


    right_boundary = player['x'] + 130
    left_boundary = player['x']
    upper_boundary = player['y']
    lower_boundary = player['y'] + 98

    for bullet in unfriendly_bullets:
        bullet_x = bullet['x']
        bullet_y = bullet['y']
        if bullet_x > left_boundary and bullet_x < right_boundary and bullet_y > upper_boundary and bullet_y < lower_boundary:
            was_our_player_hit = True
            amount_of_lives -= 1
        
    if was_our_bad_guy_hit == False:
        blit_object(bad_guy)
        move_object(bad_guy)

        
    if was_our_player_hit == False:
        blit_object(player)
        move_object(player)


    for blittable_object in friendly_bullets:
        blit_object(blittable_object)
        move_object(blittable_object)
        temp_list.append(blittable_object)

    for blittable_object in unfriendly_bullets:
        blit_object(blittable_object)
        move_object(blittable_object) 
        temp_list.append(blittable_object)    

    
    if last_bad_guy_bullet_time == None or pygame.time.get_ticks() - last_bad_guy_bullet_time > 500:
        bad_guy_shoot_bullet(bad_guy, unfriendly_bullets)
        last_bad_guy_bullet_time = pygame.time.get_ticks()

    show_score()
    pygame.display.update()