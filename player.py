import pygame
from character import Character
from pistol import Pistol
from rifle import Rifle
from pistoltwo import PistolTwo
from bomb import Bomb

class Player(Character):

    def __init__(self, x, y, tile_size):


        self.key_pressed = False

        super(Player, self).__init__(x, y, tile_size[0], tile_size[0], 1000)

        self.images = { 
            "EAST" : pygame.image.load("images/hero_right2.png"),
            "WEST" : pygame.image.load("images/hero_left2.png"),
            "NORTH" : pygame.image.load("images/hero_up2.png"),
            "SOUTH" : pygame.image.load("images/hero_down2.png") }

        self.guns = [Pistol(), PistolTwo(), Rifle()]
        self.seted_gun = 0
        self.keys = 0


    def draw(self, screen):

        if self.direction == "E":
            screen.blit(self.images["EAST"], (self.x, self.y))
        elif self.direction == "W":
            screen.blit(self.images["WEST"], (self.x, self.y))
        elif self.direction == "N":
            screen.blit(self.images["NORTH"], (self.x, self.y))
        elif self.direction == "S":
            screen.blit(self.images["SOUTH"], (self.x, self.y))

        self.guns[self.seted_gun].draw(screen, self)

    def interaction(self, pygame_event):

        if pygame_event.type == pygame.KEYDOWN:

            if pygame_event.key == pygame.K_UP:

                self.key_pressed = True

                if self.direction == "N":

                    self.velocity_x = 0
                    self.velocity_y = -8

                else:
                    self.key_pressed = False
                    self.direction = "N"

            elif pygame_event.key == pygame.K_DOWN:

                self.key_pressed = True

                if self.direction == "S":

                    self.velocity_x = 0
                    self.velocity_y = 8

                else:
                    self.key_pressed = False
                    self.direction = "S"

            elif pygame_event.key == pygame.K_LEFT:

                self.key_pressed = True

                if self.direction == "W":

                    self.velocity_x = -8
                    self.velocity_y = 0

                else:
                    self.key_pressed = False
                    self.direction = "W"

            elif pygame_event.key == pygame.K_RIGHT:

                self.key_pressed = True

                if self.direction == "E":
                    self.velocity_x = 8
                    self.velocity_y = 0

                else:
                    self.key_pressed = False
                    self.direction = "E"

            elif pygame_event.key == pygame.K_a:
                self.shot()

            elif pygame_event.key == pygame.K_d:

                self.seted_gun += 1
                self.seted_gun %= 3
            elif pygame_event.key == pygame.K_s:
                self.bomb()

        elif pygame_event.type == pygame.KEYUP:

            if pygame_event.key == pygame.K_UP or \
               pygame_event.key == pygame.K_DOWN or \
               pygame_event.key == pygame.K_RIGHT or \
               pygame_event.key == pygame.K_LEFT:

               self.key_pressed = False

                #self.velocity_x = 0
                #self.velocity_y = 0


    def move(self, surface):

        if self.key_pressed == True:

            if self.next_step_x == None and self.next_step_y == None:

                if self.direction == "E":
                    future_tile = surface.get_tile_by_position((self.x + 32, self.y))
                elif self.direction == "W":
                    future_tile = surface.get_tile_by_position((self.x - 32, self.y))
                elif self.direction == "N":
                    future_tile = surface.get_tile_by_position((self.x, self.y - 32))
                elif self.direction == "S":
                    future_tile = surface.get_tile_by_position((self.x, self.y + 32))


                if future_tile.walk == True:

                    self.next_step_x = future_tile.x
                    self.next_step_y = future_tile.y

                    self.x += self.velocity_x
                    self.y += self.velocity_y
                else:
                    self.velocity_x = 0
                    self.velocity_y = 0

            else:

                self.x += self.velocity_x
                self.y += self.velocity_y  

                if self.x == self.next_step_x and self.y == self.next_step_y:

                    self.next_step_x = None
                    self.next_step_y = None



        else:

            if self.next_step_x != None and self.next_step_y != None:

                self.x += self.velocity_x
                self.y += self.velocity_y                      

                if self.x == self.next_step_x and self.y == self.next_step_y:

                    self.next_step_x = None
                    self.next_step_y = None   
                    self.velocity_x = 0
                    self.velocity_y = 0
  
    def shot(self):

        self.guns[self.seted_gun].shot(self)

    def bomb(self):
        Bomb(self.x, self.y)

    def get_hit(self, damage):

        self.health -= damage