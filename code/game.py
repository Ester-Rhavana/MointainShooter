#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print("Setup Start")
        pygame.init()
        screen = pygame.display.set_mode((600, 480))
        print("Setup End")

        print("Loop Start")
        while True:
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # Closing Window
                    quit()  # end pygame, testando alterações

