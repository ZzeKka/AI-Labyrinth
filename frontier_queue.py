""" Queue """

class FrontierQueue:
    """Queue data strucute."""

    def __init__(self) -> None:
        """
        When initialized creates an array
        were elements will be stored as a queue.
        """
        self.queue_list = []

    def enqueue(self, element) -> None:
        """
        Adds element to the queue on the first index (0)

        Parameters:
            element (Any): element to be added to the stack.
        """
        self.queue_list.insert(0, element)

    def dequeue(self) -> None:
        """
        Removes from the Queue, last index from Queue

        Return:
            element (Node): returns removed element.
        """
        self.queue_list.pop()

    def get_length(self) -> int:
        """
        returns length of queue

        Returns:
            length (int): Current length of the queue.
        """
        return len(self.queue_list)

    def display_queue(self) -> None:
        """
        Prints the current Queue.
        If its empty prints an empty list
        """
        print(self.queue_list)

    # Node only methods, for Node's with parameter state
    def contains_state(self, state) -> bool:
        """
        Checks if any Nodes in the queue contains given state

        Parameters:
            state (tuple) - location of a certain square

        Returns:
            (bool) - true if the state is in any node in the queue
        """
        return any(node.state == state for node in self.queue_list)
