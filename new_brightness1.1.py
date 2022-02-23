import random
import copy
import pygame


import brightness_determination_2 as b
import test as t


d = {
    1 : (100, 100),
    2 : (100, 200),
    3 : (100, 300),
    4 : (200, 100),
    5 : (200, 200),
    6 : (200, 300),
    7 : (300, 100),
    8 : (300, 200),
    9 : (300, 300)
    }

d_2 = {
    1 : (100, 100),
    2 : (100, 200),
    3 : (100, 300),
    4 : (200, 100),
    5 : (200, 200),
    6 : (200, 300),
    7 : (300, 100),
    8 : (300, 200),
    9 : (300, 300),
    10 : (400,100),
    11 : (400,200),
    12 : (400,300),
    13 : (400,400),
    15 : (500,500)
    }




#задаем параметры окна экрана
WIDTH = 800
HEIGHT = 800

#задаем цвета
BLACK = (0,0,0)

#ФПС привязан к движку программы для старта - 60
FPS = 60

#создаем игру 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("lines1.0")
clock = pygame.time.Clock()

#создаем объекты
new_dot = b.INITIAL_DOTS(d, screen, FPS)
experiment = t.TEST(d_2, screen, FPS)


running = True
while running:
	screen.fill(BLACK)
	running = new_dot.go_on()


	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False
# проверяем нажате на ENTER
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_ENTER:
				running = False
				


	clock.tick(FPS)
	pygame.display.flip()

experiment.initial_brightness = new_dot.brightness
experiment.brightness = new_dot.brightness


running = True
while running:
	screen.fill(BLACK)
	experiment.go_on()

	for event in pygame.event.get():
# проверяем закрывшееся окно
		if event.type == pygame.QUIT:
		    running = False

# проверяем нажате на ENTER
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP_ENTER:
				running = experiment.response()
				

	clock.tick(FPS)
	pygame.display.flip()


pygame.quit()
l = experiment.results
print('\n\nполученные результаты: ')
for i in l:
	print(i)

 