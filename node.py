'''File with Node strucure'''
class Node:
    ''' Each Node represents a square of the maze '''
    def __init__(self):
        '''
        Node Creation

        Attributes:
            coordenates (tuple): x and y coordenates of the square in the maze
            color (tuple): tuple containing the RGB values representing a color
            explored (boolean): Store the node square was explored or not

        '''
        self.value = None
        self.position = ()
        self.explored = False
        self.adjacents = []

    def __str__(self):
        '''
        Outputs Node information
        '''
        return f'''These node is located at {self.position} with value of {self.value},
            exploration status is {self.explored}'''

    def __repr__(self):
        return f'Node({self.value}, {self.position},  {self.explored})'
