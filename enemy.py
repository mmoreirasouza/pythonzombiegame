import pygame
from character import Character
from astar import AStar
from random import randint
from key import Key


class Enemy(Character):

    Enemies = []
    Images = { "type1" : pygame.image.load("images/zombie1.png"),
                "type2" : pygame.image.load("images/zombie2.png"),
                "type3" : pygame.image.load("images/zombie3.png"),
                "type4" : pygame.image.load("images/zombie4.png"),
                "type5" : pygame.image.load("images/zombie5.png") }

    Types = ["type1", "type2", "type3", "type4", "type5"]

    Died = 0

    def __init__(self, x, y, player, enemy_type):

        self.player = player
        self.player_last_position = (0, 0)
        self.path = []
        self.img = { "E" : Enemy.Images[enemy_type], 
                    "W" : pygame.transform.rotate(Enemy.Images[enemy_type], 180), 
                    "N" : pygame.transform.rotate(Enemy.Images[enemy_type], 90),
                    "S" : pygame.transform.rotate(Enemy.Images[enemy_type], -90) }

        if enemy_type == "type1":
            health = 500
            self.damage = 10
        elif enemy_type == "type2":
            health = 600
            self.damage = 15
        elif enemy_type == "type3":
            health = 700
            self.damage = 20
        elif enemy_type == "type4":
            health = 900
            self.damage = 25
            pygame.mixer.Sound("sounds/zombie_one.wav").play()
        elif enemy_type == "type5":
            health = 1200
            self.damage = 30
            pygame.mixer.Sound("sounds/zombie_two.wav").play()
        

        super(Enemy, self).__init__(x, y, 32, 32, health)

        Enemy.Enemies.append(self)

    def move(self):

        if self.next_step_x == None and self.next_step_y == None:

            if self.player.x != self.player_last_position[0] or self.player.y != self.player_last_position[1]:
                
                self.player_last_position = (self.player.x, self.player.y)

                if self.player.next_step_x == None and self.player.next_step_y == None:
                    self.path = AStar.get_path(self)


        if self.next_step_x == None and  self.next_step_y == None:

            if len(self.path) > 0:
                l = self.path.pop()
                self.next_step_x = l.x
                self.next_step_y = l.y

        else:

            if self.x > self.next_step_x:
                self.x -= 4
                self.direction = "W"
            elif self.x < self.next_step_x:
                self.x += 4
                self.direction = "E"

            if self.y > self.next_step_y:
                self.y -= 4
                self.direction = "N"
            elif self.y < self.next_step_y:
                self.y += 4
                self.direction = "S"

            if self.x == self.next_step_x and self.y == self.next_step_y:
                self.next_step_x = None
                self.next_step_y = None

    def draw(self, screen):        
        screen.blit(self.img[self.direction], (self.x, self.y))

    def get_hit(self, damage):

        self.health -= damage

        if self.health <= 0:

            Enemy.Died += 1

            if Enemy.Died >= 30:
                Enemy.Died = 0
                Key(self.x, self.y)

            Enemy.Enemies.remove(self)
