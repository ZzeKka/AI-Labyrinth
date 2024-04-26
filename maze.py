""" file that represents the Maze using Pygame, and calls methods from other files to
decifer the optimal path to clear said Maze """

# Python Native
from pathlib import Path
from time import sleep

# 3rd Party Libraries
import pygame

# 1st Party Libraries
from frontier_stack import FrontierStack
from node import Node

# pylint: disable=no-member

# ____________________

# Size of each square of the Maze
MAZE_SQUARESIZE = 40

# Colors
GREEN = (34, 139, 34)
ROSERED = (180, 75, 95)
DARKGRAY = (69, 69, 69)
WHITE = (255, 255, 255)
DARKPURPLE = (48, 25, 52)
LIGHTYELLOW = (255, 255, 191)

# Block Coloring Grid
grid_width_and_color = {
    "#": (0, DARKPURPLE),
    " ": (1, WHITE),
    "A": (0, ROSERED),  
    "B": (0, GREEN),
    "*": (0, LIGHTYELLOW)
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
        begin_square_coordenates (tuple): coordenates of begin A square.
        end_square_coordenates (tuple): coordenates of end B square.
        maze_graph (dict): Graph the will store path Nodes (A, B and multiple #'s)
    """
    def __init__(self, filename: Path) -> None:
        with open(filename, mode="r", encoding="utf-8") as file:
            self.maze_layout = [list(line.rstrip("\n")) for line in file.readlines()]
            if self.maze_layout.count('A') != 1:
                raise ValueError("Maze-layout needs to have exactly on starting point (A)")
            if self.maze_layout.count('B') != 1:
                raise ValueError("Maze-layout needs to have exactly on goal point (B)")
            self.cols = len(self.maze_layout[0])
            self.rows = len(self.maze_layout)
            self.start_state = self.find_coordenates('A')
            self.goal_state = self.find_coordenates('B')

    #Find coordenates a maze square
    def find_coordenates(self, unique_symbol) -> tuple:
        '''
        Return the coordenates of a unique symbol, raises error if it isn't trying to find A or B

        Parameters:
            unique_symbol (str): Maze square symbol (A or B)

        Returns:
            coordenates (tuple): symbol coordenates on maze_layout
        '''
        if unique_symbol in ('A','B'):
            for x in range(self.rows):
                for y in range(self.cols):
                    if self.maze_layout[x][y] == unique_symbol:
                        return (x,y)
        else:
            raise ValueError("Method only alloed to search for unique symbols 'A' or 'B'")

    def display_maze(self, screen) -> bool:
        """
        Functions that displays the screen where the Maze
        will be drawn.

        Parameters:
            screen (Surface): Complex variable from pygame with Width and height,
            that displays a screen.
        """
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
        """
        Functions that draws the Maze composed of squares depending on the type of
        block ("#"," ","A" or "B").

        Parameters:
            screen (Surface): Complex variable from pygame with Width and height
            that displays a screen.
        """
        for x in range(self.rows):
            for y in range(self.cols):
                rect = pygame.Rect(
                    y * MAZE_SQUARESIZE,
                    x * MAZE_SQUARESIZE,
                    MAZE_SQUARESIZE,
                    MAZE_SQUARESIZE,
                )
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
                
    def select_neighbour_squares(self, state) -> set:
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        neighbours = set()
        for action, (x,y) in candidates:
            if x < self.cols and y < self.rows and self.is_a_wall((x,y)):
                neighbour_node = Node((x,y), action)
                neighbours.add(neighbour_node)
        return neighbours    
                
    def solve_maze(self, search_algorithm="dfs") -> list:
        if(search_algorithm is "dfs"):
            frontier = FrontierStack()
            start_node = Node(self.start_state)
            frontier.stack_element(start_node)
            self.explored = set()
            while True:
                if frontier.get_length() == 0:
                    raise ValueError("No solution found")
                current_node = frontier.remove_from_stack()
                if current_node.state == self.goal_state:
                    return #solution
                else:
                    self.explored.add(current_node.state)
                    neighbours = self.select_neighbour_squares(current_node.state) 
                    for neighbour in neighbours:
                        if neighbour not in frontier and neighbour.state not in self.explored:
                            new_square_node = Node(state=neighbour.state, action=neighbour.action, parent=current_node)
                            frontier.stack_element(new_square_node)
                    frontier.remove_from_stack()
    
        
    def is_a_wall(self, position) -> bool:
        if len(position) != 2:
            raise ValueError("Invalid location sent to check_walls function")
        else:
            if self.maze_layout[position[0]][position[1]] == '#':
                return True
            else:
                return False

def main() -> None:
    """
    Main function Were functions to draw and solve the maze are called.
    """
    pygame.init()
    maze = Maze(Path("maze1.txt"))  # If file exists
    screen = pygame.display.set_mode(
        (maze.cols * MAZE_SQUARESIZE, maze.rows * MAZE_SQUARESIZE)
    )
    maze.display_maze(screen)
    pygame.quit()

if __name__ == "__main__":
    main()


"""TODO"""
### NEXT
# finish #Solution in fucntion
# Debug DFS algorithm
# Make Pygame draw cycles

### GLOBAL TASKS
# COMPLETE DFS
# COMPLETE BFS
# COMPLETE GREEDY
# COMPLETE A*


