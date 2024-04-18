import pygame
import sys

# Size of each square on the Maze
MAZE_SQUARESIZE = 40
SCREEN = ()

# Colors
GREEN = (34, 139, 34)
ROSERED = (180, 75, 95)
DARKGRAY = (69, 69, 69)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKPURPLE = (48, 25, 52)

# Creates a Maze with pygame
class Maze:
    cols = 0
    rows = 0
    maze_layout = []

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.maze_layout = [list(line.rstrip('\n')) for line in file.readlines()]
            print(self.maze_layout)
            self.cols = len(self.maze_layout[0])
            self.rows = len(self.maze_layout)
    
    def display_maze(self):
        SCREEN = WIDTH, HEIGHT = self.cols * MAZE_SQUARESIZE, self.rows * MAZE_SQUARESIZE
        win = pygame.display.set_mode(SCREEN)
        
        self.draw_grid(win)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
    
    #Drawing functions fo maze
    def draw_grid(self, window):
        for x in range(self.rows):
            for y in range(self.cols):
                rect = pygame.Rect(y * MAZE_SQUARESIZE, x * MAZE_SQUARESIZE, MAZE_SQUARESIZE, MAZE_SQUARESIZE)
                if self.maze_layout[x][y] == "#":
                    pygame.draw.rect(window, DARKPURPLE, rect)
                elif self.maze_layout[x][y] == " ":
                    pygame.draw.rect(window, WHITE, rect, 1)
                elif self.maze_layout[x][y] == "A":
                    pygame.draw.rect(window, ROSERED, rect)
                elif self.maze_layout[x][y] == "B":
                    pygame.draw.rect(window, GREEN, rect)
                       
pygame.init()
maze = Maze("maze1.txt")
maze.display_maze()
pygame.quit()