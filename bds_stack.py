class stack:
    
    def __init__(self):
        self.stack_list = []

    def stack_element(self, element):
        self.stack_list.append(element)

    def remove_from_stack(self):
        self.stack_list.pop(0);

    def get_length(self):
        return len(self.stack_list)
    
    def display_queue(self):
        print("Stack:\n")
        if self.get_length() <= 0:
            print("Stack is Empty")
        else:
            for element in self.stack_list:
                print(f"| {element} |\n")
        print("\n")


new_stack = stack()
new_stack.display_queue()
new_stack.stack_element(3)
new_stack.stack_element(2)
new_stack.stack_element(1)
new_stack.display_queue()
new_stack.remove_from_stack()
new_stack.display_queue()