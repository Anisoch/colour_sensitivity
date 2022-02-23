"""шаблон Pygame"""
import pygame

#задаем параметры окна экрана
WIDTH = 800
HEIGHT = 800

# можно задать цвета
BLACK = (0,0,0)
WHITE = (255,255,255)

#ФПС
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("name")
clock = pygame.time.Clock()


cross = pygame.image.load('cross.png')

running = True
while running:
	screen.fill(BLACK)
	screen.blit(cross, (100,200))







	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False

	clock.tick(FPS)
	pygame.display.flip()


pygame.quit()
