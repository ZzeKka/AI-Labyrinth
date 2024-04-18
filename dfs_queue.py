class queue:
    
    def __init__(self):
        self.queue_list = []

    def enqueue(self, element):
        self.queue_list.insert(0, element)

    def dequeue(self):
        self.queue_list.pop();

    def get_length(self):
        return len(self.queue_list)
    
    def display_queue(self):
        print(self.queue_list)
