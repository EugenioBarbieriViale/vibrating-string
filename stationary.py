import pygame, sys
import numpy as np

pygame.init()
clock = pygame.time.Clock()

X, Y = 1000, 800
FPS = 30

screen = pygame.display.set_mode([X,Y])

class String:
    def __init__(self):
        self.nodes = 5
        self.initial_displacement = 200

        self.k = 6
        self.length = 800

        self.m = 4
        self.radius = 6
        self.n = self.length // self.radius

        self.x0 = X / 2 - self.length / 2
        self.y0 = Y / 2

        self.string = []
        for i in range(self.n):
            xi = self.x0 + i * self.radius
            yi = self.y0 - np.sin(self.nodes * i / self.n * np.pi) * self.initial_displacement

            self.string.append(pygame.math.Vector2(xi, yi))

        self.vys = [0.0 for i in range(self.n)]

        self.dt = 1 / FPS

    def move(self):
        for i in range(self.n):
            ay = - self.k * (self.string[i].y - self.y0) / self.m
            self.vys[i] += ay * self.dt

        for i in range(self.n):
            self.string[i].y += self.vys[i]

    def draw(self, screen):
        pygame.draw.circle(screen, (0,255,0), (self.x0, self.y0), self.radius*2)
        pygame.draw.circle(screen, (0,255,0), (self.x0 + self.length, self.y0), self.radius*2)

        for s in self.string:
            pygame.draw.circle(screen, (255,0,0), s, self.radius)

s = String()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    s.move()
    s.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
