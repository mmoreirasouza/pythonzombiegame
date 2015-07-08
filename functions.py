import pygame

def write_on_screen(screen, position, text, size = 15, color = (255, 255, 255)):

	text = str(text)
	font = pygame.font.SysFont(None, size)
	text = font.render(text, True, color)
	screen.blit(text, position)
