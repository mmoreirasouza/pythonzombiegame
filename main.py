import pygame
import sys
import math
import functions
from surface import Surface
from level1 import Level1
from player import Player
from enemy import Enemy
from astar import AStar
from pistol import Pistol
from bullet import Bullet
from bomb import Bomb
from life import Life
from key import Key
from end import End

#print(sys.version)


SURFACE_SIZE = (800, 640)
TILE_SIZE = (32, 32)
FPS = 20

pygame.init()
pygame.font.init()
pygame.mixer.init()

dynamite = pygame.image.load("images/dynamite.png")
key_image = pygame.image.load("images/key.png")
life_image = pygame.image.load("images/life.png")
open_door = pygame.image.load("images/open_door.png")
closed_door = pygame.image.load("images/closed_door.png")

dynamite_sound = pygame.mixer.Sound("sounds/bomb.wav")
key_sound = pygame.mixer.Sound("sounds/key.ogg")
door_sound = pygame.mixer.Sound("sounds/door_creak_closing.wav")

pygame.mixer.music.load("sounds/zombie_theme.wav")
pygame.mixer.music.play(-1)

level = Level1()

surface = Surface(SURFACE_SIZE, TILE_SIZE, level)

end_tile = Surface.get_tile_by_number(173)
level.end = End(end_tile.x, end_tile.y)

player_position = Surface.get_tile_by_number(level.player_position)

player = Player(player_position.x, player_position.y, TILE_SIZE)




bg = pygame.image.load("images/bg.png")

game_screen = pygame.display.set_mode(SURFACE_SIZE)

pygame.display.set_caption("Zombie")

clock = pygame.time.Clock()

total_frames = 0

door_sound_play = False

level_end = False


#Enemy(736,32 , player, "type5")

while True:

    clock.tick(FPS)

    total_frames += 1

    game_screen.blit(bg, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player.interaction(event)

    if level_end == True or player.health <= 0:

        functions.write_on_screen(game_screen, (SURFACE_SIZE[0]/2-80, SURFACE_SIZE[1]/2), "GAME OVER", 50)

        pygame.display.update()
        continue

    #for tile in Surface.Tiles:
        #pygame.draw.rect(game_screen, tile.color, (tile.x, tile.y, tile.width, tile.height))
        #functions.write_on_screen(game_screen, (tile.x, tile.y), tile.x, 15)
        #functions.write_on_screen(game_screen, (tile.x, tile.y+15), tile.y, 15)
        #functions.write_on_screen(game_screen, (tile.x, tile.y), tile.number, 15)

    if player.keys >= 4:
        if door_sound_play == False:
            door_sound_play = True
            door_sound.play()
        game_screen.blit(open_door, (level.end.x, level.end.y))

        if player.check_collision(level.end):
            level_end = True
    else:
        game_screen.blit(closed_door, (level.end.x, level.end.y))

    player.move(surface)

    player.draw(game_screen)

    functions.write_on_screen(game_screen, (0, 0), player.health, 15)

    for enemy in Enemy.Enemies:
        if enemy.check_collision(player):
            player.get_hit(enemy.damage)



    for enemy in Enemy.Enemies:
        #pass
        enemy.move()

    for enemy in Enemy.Enemies:
        enemy.draw(game_screen)

    for key in Key.Keys:
        game_screen.blit(key_image, (key.x, key.y))
        #pygame.draw.rect(game_screen, (255, 255, 255), (key.x, key.y, 32, 32))

        if key.check_collision(player):
            key_sound.play()
            player.keys += 1
            Key.Keys.remove(key)

    





    if total_frames % 30 == 0:
        #pass
        level.create_enemy(player)

    if total_frames % 600 == 0:
        if player.health <= 600:
            level.create_life()

    for life in Life.Lifes:
        life.total_frames += 1

        if life.total_frames % 400 == 0:
            Life.Lifes.remove(life)
        else:
            if life.check_collision(player):
                player.health += life.health
                Life.Lifes.remove(life)




    for life in Life.Lifes:
        game_screen.blit(life_image, (life.x, life.y))
        #pygame.draw.rect(game_screen, (0, 243, 0), (life.x, life.y, 32, 32))



    


    for bullet in Bullet.Bullets:
        bullet.move()




    for bullet in Bullet.Bullets:
        #pygame.draw.rect(game_screen, (0, 0, 0), (bullet.x, bullet.y, bullet.width, bullet.height))
        game_screen.blit(bullet.image, (bullet.x, bullet.y))



    for bullet in Bullet.Bullets:

        for tile in Surface.Tiles:

            if tile.walk == False:

                if bullet.check_collision(tile):
                    Bullet.Bullets.remove(bullet)
                    break

        for enemy in Enemy.Enemies:

            if bullet.check_collision(enemy):                
                enemy.get_hit(bullet.damage)
                try:
                    Bullet.Bullets.remove(bullet)
                except:
                    print ("erro: Bullet.Bullets.remove(bullet)")
                break

    #print len(Bullet.Bullets)

    
    for bomb in Bomb.Bombs:
        bomb.total_frames += 1
        game_screen.blit(dynamite, (bomb.x, bomb.y))

        if bomb.total_frames % 30 == 0:
            dynamite_sound.play()
            pygame.draw.circle(game_screen, (255, 0, 0), (bomb.x_center, bomb.y_center), 128, 1)

            enemy_near = []

            for enemy in Enemy.Enemies:
                
                distance = int(math.sqrt((bomb.x_center - enemy.x_center)**2 + (bomb.y_center - enemy.y_center)**2))
                if distance <= 128:
                    enemy_near.append(enemy)

            for enemy in enemy_near:
                enemy.get_hit(10000000)


            Bomb.Bombs.remove(bomb)

    

    #print total_frames

    pygame.display.update()

    

    
