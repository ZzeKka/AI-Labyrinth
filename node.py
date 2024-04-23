'''File with Node strucure'''
class Node:
    ''' Each Node represents a square of the maze '''
    def __init__(self, state, action, cost, parent=None):
        '''
        Node Creation

        Attributes:
            state (tuple): represents the coordentes in matrix layout when travelling to this node.
            action (str): represents the actions that can be made in these corrent node state.
            cost (int): Cost to reach these path from initial mode.
            parent (Node): Parent Node from were we travelled to reach these current node.
        '''
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent
        

    def __str__(self):
        '''
        Outputs Node information
        '''
        return f'''Current state of these node is {self.state}'''

    def __repr__(self):
        return f'Node({self.state}, {self.action})'
