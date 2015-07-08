from rect import Rect
import pygame

class Bullet(Rect):

	Bullets = []
	Images = { "pistol" : pygame.image.load("images/bullet_pistol.png"),
				"pistol_two" : pygame.image.load("images/bullet_pistol_two.png"),
				"rifle" : pygame.image.load("images/bullet_rifle.png") }

	def __init__(self, x, y, damage, x_velocity, y_velocity, bullet_type):

		self.damage = damage
		self.x_velocity = x_velocity
		self.y_velocity = y_velocity
		self.type = bullet_type

		self.image = pygame.transform.rotate(Bullet.Images[bullet_type], 0 if x_velocity == 0 else 90)

		super(Bullet, self).__init__(x, y, 10, 10)

		Bullet.Bullets.append(self)

	def move(self):

		self.x += self.x_velocity
		self.y += self.y_velocity