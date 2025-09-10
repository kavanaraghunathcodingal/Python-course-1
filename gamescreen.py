import pygame

pygame.init()
import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))  # corrected name
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # exit loop

    pygame.display.flip()

pygame.quit()  # quits after loop ends
