''' Stack '''
class Stack:
    '''
    Stack data strucute.

    Attributes:
        stacklist (list): list of elemnts of the stack.    
    '''
    def __init__(self) -> None:
        '''
        When initialized creates an array
        were elements will be stored as a stack.
        '''
        self.stack_list = []

    def stack_element(self, element):
        '''
        Adds element ot the stack

        Parameters:
            element (Any): element to be added to the stack.    
        '''
        self.stack_list.append(element)

    def remove_from_stack(self) -> None:
        '''
        Adds element ot the stack

        Parameters:
            element (Any): element to be added to the stack.    
        '''
        self.stack_list.pop(0)

    def get_length(self) -> int:
        '''
        Adds element ot the stack

        Returns:
            length (int): Current length of the stack.    
        '''
        return len(self.stack_list)

    def display_queue(self) -> None:
        '''
        Prints the current stack.
        If its empty print a message "Stack is Empty"  
        '''
        print("Stack:\n")
        if self.get_length() <= 0:
            print("Stack is Empty")
        else:
            for element in self.stack_list:
                print(f"| {element} |\n")
        print("\n")
