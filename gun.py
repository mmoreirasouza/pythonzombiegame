from rect import Rect
from bullet import Bullet
import pygame

#pistol rifle

class Gun(Rect):

	Images = { "pistol" : pygame.image.load("images/pistol.png"), 
				"pistol_two" : pygame.image.load("images/pistol_two.png"),
				"rifle" : pygame.image.load("images/rifle.png") }             

	def __init__(self, damage, bullet_type):

		self.damage = damage
		self.bullet_type = bullet_type
		self.images = { "E" : pygame.transform.rotate(Gun.Images[bullet_type], -90),
						"W" : pygame.transform.rotate(Gun.Images[bullet_type], 90),
						"N" : pygame.transform.rotate(Gun.Images[bullet_type], 0),
						"S" : pygame.transform.rotate(Gun.Images[bullet_type], 180) }

		self.sound = pygame.mixer.Sound("sounds/shot.wav")
		self.sound.set_volume(0.1)


		super(Gun, self).__init__(0, 0, 0, 0)


	def draw(self, screen, player):

		if player.direction == "E":
			#self.width = 20
			#self.height = 5
			#pygame.draw.rect(screen, (0, 0, 0), (player.x_center + self.width / 2, player.y_center, self.width, self.height))
			screen.blit(self.images[player.direction], (player.x + self.images[player.direction].get_width() / 2, player.y))

		elif player.direction == "W":
			#self.width = 20
			#self.height = 5
			#pygame.draw.rect(screen, (0, 0, 0), (player.x - self.width / 2, player.y_center, self.width, self.height))
			screen.blit(self.images[player.direction], (player.x - self.images[player.direction].get_width() / 2, player.y))

		elif player.direction == "N":
			#self.width = 5
			#self.height = 20
			#pygame.draw.rect(screen, (0, 0, 0), (player.x_center, player.y_center - self.height, self.width, self.height))
			screen.blit(self.images[player.direction], (player.x, player.y - self.images[player.direction].get_height() / 2 ))

		elif player.direction == "S":
			#self.width = 5
			#self.height = 20
			#pygame.draw.rect(screen, (0, 0, 0), (player.x_center, player.y_center + self.height, self.width, self.height))
			screen.blit(self.images[player.direction], (player.x, player.y + self.images[player.direction].get_height() / 2))


	def shot(self, player):

		x_velocity = 0
		y_velocity = 0

		if player.direction == "E":

			x_velocity = 20
			y_velocity = 0

		elif player.direction == "W":

			x_velocity =  -20
			y_velocity = 0

		elif player.direction == "N":

			x_velocity = 0
			y_velocity = -20

		elif player.direction == "S":

			x_velocity = 0
			y_velocity = 20


		Bullet(player.x, player.y, self.damage, x_velocity, y_velocity, self.bullet_type)

		self.sound.play()