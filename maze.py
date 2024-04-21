""" file that represents the Maze using Pygame, and calls methods from other files to
decifer the optimal path to clear said Maze """
# Python Native
from pathlib import Path
from time import sleep

# 3rd Party Libraries
import pygame
# pylint: disable=no-member

#____________________

# Size of each square of the Maze
MAZE_SQUARESIZE = 40

# Colors
GREEN = (34, 139, 34)
ROSERED = (180, 75, 95)
DARKGRAY = (69, 69, 69)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKPURPLE = (48, 25, 52)

# Block Coloring Grid
grid_width_and_color = {
    "#": (0, DARKPURPLE),
    " ": (1, WHITE),
    "A": (0, ROSERED),
    "B": (0, GREEN),
}

# Creates a Maze with pygame
class Maze:
    """
    A class that represents a Maze stored 
    in a text file using pygame.

    Attributes:
        cols (int): number of columns.
        rows (int): number of rows.
        maze_layout (str[][]): matrix representing the maze.
            Matrix contents can be:
                -> "#" a wall square;
                -> " " a path square;
                -> "A" starting square (unique);
                -> "B" goal square.
    """

    def __init__(self, filename: Path) -> None:
        with open(filename, mode="r", encoding="utf-8") as file:
            self.maze_layout = [list(line.rstrip('\n')) for line in file.readlines()]
            self.cols = len(self.maze_layout[0])
            self.rows = len(self.maze_layout)

    def display_maze(self, screen) -> bool:
        '''
        Functions that displays the screen where the Maze
        will be drawn.

        Parameters:
            screen (Surface): Complex variable from pygame with Width and height,
            that displays a screen.
        '''

        keep_displaying = True
        while keep_displaying:
            sleep(0.1)
            self.draw_maze(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_displaying = False
                    break
            pygame.display.update()

    # Drawing functions for maze
    def draw_maze(self, window) -> None:
        '''
        Functions that draws the Maze composed of squares depending on the type of
        block ("#"," ","A" or "B").

        Parameters:
            screen (Surface): Complex variable from pygame with Width and height
            that displays a screen.
        '''
        for x in range(self.rows):
            for y in range(self.cols):
                rect = pygame.Rect(y * MAZE_SQUARESIZE,
                                    x * MAZE_SQUARESIZE,
                                    MAZE_SQUARESIZE,
                                    MAZE_SQUARESIZE)
                if self.maze_layout[x][y] == "#":
                    pygame.draw.rect(window, DARKPURPLE, rect)
                elif self.maze_layout[x][y] == " ":
                    pygame.draw.rect(window, WHITE, rect, width=1)
                elif self.maze_layout[x][y] == "A":
                    pygame.draw.rect(window, ROSERED, rect)
                elif self.maze_layout[x][y] == "B":
                    pygame.draw.rect(window, GREEN, rect)
                else:
                    raise ValueError("Invalid character in Matrix layout, Exiting")

    def maze_graph(self, maze_layout) -> list:
        for x in range(self.cols):
            for y in range(self.rows):
                if self.maze_layout[x][y] not in '#':
                    node = Node()
                    node.position = (x,y)

def main() -> None:
    '''
    Main function Were functions to draw and solve the maze are called.
    '''
    pygame.init()
    maze = Maze(Path("maze1.txt")) #If file exists
    screen = pygame.display.set_mode((maze.cols * MAZE_SQUARESIZE, maze.rows * MAZE_SQUARESIZE))
    maze.display_maze(screen)
    pygame.quit()

if __name__ == "__main__":
    main()
