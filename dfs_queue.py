class queue:
    
    def __init__(self) -> None:
        self.queue_list = []

    def enqueue(self, element) -> None:
        self.queue_list.insert(0, element)

    def dequeue(self) -> None:
        self.queue_list.pop();

    def get_length(self) -> int:
        return len(self.queue_list)
    
    def display_queue(self) -> None:
        print(self.queue_list)
