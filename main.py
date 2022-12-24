import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 1050, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill("black")

pygame.display.set_caption("Algorhythms")

GAME_FONT = pygame.font.SysFont('Comic Sans MS', 15)
running = True
clock = pygame.time.Clock()

def generate_list():
	values = []
	for _ in range(50):
		values.append(random.randint(20, HEIGHT - 20))
	return values

i = 0
j = 0

def bubble_sort(arr, window):
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				draw_list(arr, window, [j, j + 1])
				yield True

def selection_sort(arr, window):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i + 1, len(arr)):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		draw_list(arr, window, [min_idx, i])
		yield True

sorting = False

def draw_list(arr, window, color_indices):
	window.fill("black")
	for idx, val in enumerate(arr):
		if len(color_indices) > 0:
			if idx == color_indices[0]:
				color = GREEN
			elif idx == color_indices[1]:
				color = RED
			else:
				color = WHITE
		else:
			color = WHITE
		pygame.draw.rect(window, color, ((idx+1)*20, HEIGHT - val, 10, val))

	pygame.display.update()

values = generate_list()
sorting_algorithm = bubble_sort
algorithm_name = 'BUBBLE SORT'

instructions = 'R - Reset | S - Selection Sort | B - Bubble Sort | SPACE - Start Sorting'
instructions_surface = GAME_FONT.render(instructions, 1, WHITE)

while running:

	clock.tick(30)
	if sorting:
		try:
			next(g)
		except StopIteration:
			sorting = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type != pygame.KEYDOWN:
			continue
		if event.key == pygame.K_r and not sorting:
			values = generate_list()
		if event.key == pygame.K_s and not sorting:
			sorting_algorithm = selection_sort
			algorithm_name = 'SELECTION SORT'
		if event.key == pygame.K_b and not sorting:
			sorting_algorithm = bubble_sort
			algorithm_name = 'BUBBLE SORT'
		if event.key == pygame.K_SPACE and not sorting:
			sorting = True
			g = sorting_algorithm(values, win)

	draw_list(values, win, [])
	status = GAME_FONT.render(f'{algorithm_name}', 1, WHITE)
	win.blit(status, (5, 5))
	win.blit(instructions_surface, (5, 25))
	pygame.display.update()

pygame.quit()
