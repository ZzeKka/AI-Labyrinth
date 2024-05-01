""" Stack """

from node import Node

class FrontierStack:
    """Stack data strucute."""

    def __init__(self) -> None:
        """
        When initialized creates an array
        were elements will be stored as a stack.
        """
        self.frontier_stack = []

    def stack_element(self, element):
        """
        Adds element to the stack

        Parameters:
            element (Any): element to be added to the stack.
        """
        self.frontier_stack.insert(0, element)

    def remove_from_stack(self) -> Node:
        """
        Removes from the stack, most recent added

        Return:
            element (Node): returns removed element.
        """
        if self.get_length() == 0:
            raise IndexError("Stack is Empty")
        return self.frontier_stack.pop(0)

    def get_length(self) -> int:
        """
        return length of stack

        Returns:
            length (int): Current length of the stack.
        """
        return len(self.frontier_stack)

    def display_stack(self) -> None:
        """
        Prints the current stack.
        If its empty print a message "Stack is Empty"
        """
        print("Stack:\n")
        if self.get_length() <= 0:
            print("Stack is Empty")
        else:
            for element in self.frontier_stack:
                print(f"| {element} |\n")
        print("\n")

    # Node only methods, for Node's with parameter state
    def contains_state(self, state) -> bool:
        """
        Checks if any Nodes in the stack contains given state

        Parameters:
            state (tuple) - location of a certain square

        Returns:
            (bool) - true if the state is in any node in the stack
        """
        return any(node.state == state for node in self.frontier_stack)
