"""
Author: Anthony Maniko, 
Date: 12/12/2022
Final Project Name: Snake Game
Assignment title: Final Project
"""

# Importing libraries
import pygame
import time
import random
import sys
from pygame.locals import *

# Class for creating a button
class Button:
    def __init__(self, x, y, width, height, color, title=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.title != '':
            font = pygame.font.SysFont('Arial', 50)
            text = font.render(self.title, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def click(self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        return False

# Function to show the start screen
def startScreen(color, game_window, window_x, window_y):
    """
    Shows a starting screen at the beginning of the game
    
    Parameters:
    color (pygame.Color): The color of the text over the background screen.
    game_window (pygame.Surface): The window where the start screen is displayed.
    window_x (int): The width of the game window.
    window_y (int): The height of the game window.
        
    Returns:
    None
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        my_font = pygame.font.SysFont('Arial', 50)
        game_start_surface = my_font.render('SNAKE', True, color)
        game_start_rect = game_start_surface.get_rect()
        startWindow = pygame.display.set_mode((window_x, window_y))
        pygame.display.set_caption('Menu Screen')
        game_start_rect = game_start_surface.get_rect()
        game_start_rect.midtop = (window_x/2, window_y/4)
        game_window.blit(game_start_surface, game_start_rect)

# Function to display the score
def show_score(choice, color, font, size, score, window_x, window_y, game_window):
    """
    Shows the score of the player throughout the game
    
    Parameters:
    choice (int): Determines where the score is displayed.
    color (pygame.Color): The color of the text over the background screen.
    font (str): The font used to display the score.
    size (int): The size of the font.
    score (int): The score of the player.
    window_x (int): The width of the game window.
    window_y (int): The height of the game window.
    game_window (pygame.Surface): The window where the score is displayed.
        
    Returns:
    None
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x/10, 15)
    else:
        score_rect.midtop = (window_x/2, window_y/1.25)
    game_window.blit(score_surface, score_rect)

# Function to show the game over screen
def game_over(score, window_x, window_y, game_window, color, bkrdColor):
    """
    Shows the ending screen when the player dies
    
    Parameters:
    score (int): The score of the player.
    window_x (int): The width of the game window.
    window_y (int): The height of the game window.
    game_window (pygame.Surface): The window where the game over screen is displayed.
    color (pygame.Color): The color of the text over the background screen.
    bkrdColor (pygame.Color): The color of the background of the screen.

    Returns:
    None
    """
    my_font = pygame.font.SysFont('Arial', 50)
    game_over_surface = my_font.render('SORRY, YOU DIE!  SCORE: ' + str(score), True, color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.fill(bkrdColor)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(10)
    pygame.quit()
    sys.exit()

# Play function
def play():
    """
    The function that runs everything related to the game
    
    Parameters:
    None
        
    Returns:
    None
    """
    snake_speed = 15  # Snake speed
    window_x = 800  # Window width
    window_y = 600  # Window height
    black = pygame.Color(0, 0, 0)  # Colors
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    score = 0  # Initial score
    pygame.init()  # Initialize pygame
    pygame.display.set_caption('~~DeE  ****  *** SNAKE FIELD ! ``~~`` ***   << >>    ***  YoU ArE WeLcOmE !! ')
    game_window = pygame.display.set_mode((window_x, window_y))  # Initialize game window

    # Start screen
    startButton = Button(300, 300, 200, 100, red, "START")
    rulesButton = Button(300, 500, 200, 100, red, "RULES")
    fps = pygame.time.Clock()  # FPS controller
    snake_position = [100, 50]  # Snake position
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]  # Snake body
    ball_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]  # Ball position
    ball_spawn = True  # Ball spawn flag
    direction = 'RIGHT'  # Snake direction
    change_to = direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == ball_position[0] and snake_position[1] == ball_position[1]:
            score += 5
            ball_spawn = False
        else:
            snake_body.pop()

        if not ball_spawn:
            ball_position = [random.randrange(1, (window_x//10)) * 10,
                             random.randrange(1, (window_y//10)) * 10]

        ball_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(ball_position[0], ball_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over(score, window_x, window_y, game_window, red, black)

        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over(score, window_x, window_y, game_window, red, black)

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score, window_x, window_y, game_window, red, black)

        show_score(1, white, 'Arial', 20, score, window_x, window_y, game_window)
        pygame.display.update()
        fps.tick(snake_speed)

# Main function
def main():
    play()

if __name__ == '__main__':
    main()
