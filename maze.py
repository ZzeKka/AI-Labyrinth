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
LIGHTBLUE = (173, 216, 230)
WHITE = (255, 255, 255)
DARKPURPLE = (48, 25, 52)
LIGHTYELLOW = (255, 255, 237)

# Block Coloring Grid
grid_width_and_color = {
    "#": (0, DARKPURPLE),
    " ": (1, WHITE),
    "A": (0, ROSERED),  
    "B": (0, GREEN),
    "x": (0, LIGHTBLUE),
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
            self.maze_layout = []
            countA, countB = 0, 0
            for line in file.readlines():
                row = list(line.rstrip('\n'))
                countA += row.count('A')
                countB += row.count('B')
                self.maze_layout.append(list(line.rstrip('\n')))
            if countA != 1:
                raise ValueError("Maze-layout needs to have exactly on starting point (A)")
            if countB != 1:
                raise ValueError("Maze-layout needs to have exactly on goal point (B)")
            self.cols = len(self.maze_layout[0])
            self.rows = len(self.maze_layout)
            self.start_state = self.find_coordenates('A')
            self.goal_state = self.find_coordenates('B')

    # Find coordenates a maze square
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

    '''
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
    '''

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
                try:
                    width, color = grid_width_and_color[self.maze_layout[x][y]]
                    pygame.draw.rect(window, color, rect, width)
                except:
                    raise ValueError("Invalid character in Matrix layout, Exiting")
            
    def select_neighbour_squares(self, state) -> set:
        row, col = state
        # The first index represents the first move direction
        candidates = [
            ("up", (row - 1, col)),
            ("right", (row, col + 1)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1))   
        ] 
        neighbours = []
        for action, (x,y) in candidates:
            if x in range(0,self.rows) and y in range(0,self.cols) and not self.is_a_wall((x,y)):
                neighbours.append(((x,y), action))
        self.print_maze()
        return list(reversed(neighbours))
                
    def solve_maze(self,screen, search_algorithm="dfs") -> list:
        if search_algorithm == "dfs":
            frontier = FrontierStack()
            start_node = Node(self.start_state)
            frontier.stack_element(start_node)
            self.explored = set()
            while True:
                if frontier.get_length() == 0:
                    raise ValueError("No solution found")
                current_node = frontier.remove_from_stack()
                if current_node.state == self.goal_state:
                    solution = []
                    while True:
                        if self.close_window_event():
                            return
                        current_node = current_node.parent
                        if current_node.parent == None:
                            break
                        self.maze_layout[current_node.state[0]][current_node.state[1]] = '*'
                        solution.append((current_node.state, current_node.action))
                        sleep(0.5)
                        print(self.maze_layout)
                        self.draw_maze(screen)
                        pygame.display.update()
                    return list(reversed(solution))
                else:
                    if self.maze_layout[current_node.state[0]][current_node.state[1]] != 'A':
                        self.maze_layout[current_node.state[0]][current_node.state[1]] = 'x'
                    self.explored.add(current_node.state)
                    self.draw_maze(screen)
                    sleep(0.5)
                    if self.close_window_event():
                        return
                    neighbours = self.select_neighbour_squares(current_node.state)
                    for state, action in neighbours:
                        if not frontier.contains_state(state) and state not in self.explored:
                            frontier.stack_element(Node(state=state, action=action, parent=current_node))
                pygame.display.update()

    def is_a_wall(self, position) -> bool:
        if len(position) != 2:
            raise ValueError("Invalid location sent to check_walls function")
        else:
            if self.maze_layout[position[0]][position[1]] == '#':
                return True
            else:
                return False
        
    # Print Maze
    def print_maze(self) -> None:
        '''
        Prints each element of the maze in a readable way
        '''
        for row in self.maze_layout:
            print("".join(row))
        print() 
                
    @staticmethod   
    def close_window_event() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
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
    maze_solution = maze.solve_maze(screen, "dfs")
    print(maze_solution)
    while True:
        if maze.close_window_event():
            break
    pygame.quit()

if __name__ == "__main__":
    main()


"""TODO"""
### Next Tasks
# Solution
# Update documentation

### GLOBAL TASKS
# COMPLETE DFS
# COMPLETE BFS
# COMPLETE GREEDY
# COMPLETE A*


