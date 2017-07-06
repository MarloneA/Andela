class List(object): # creates the list to be searched by the binary search
    def __init__(self, a, b):        
        self.length = a # number of elements in list
        self.step = b # number of steps between elements
        self.created_list = []
    
    def create_list(self):
        counter = 1
        current_value = 2 # Let's set our starting element to be 2. we could make it random
        while counter <= self.length:
            self.created_list.append(current_value) # first append value
            current_value += self.step # increment value by step
            counter += 1

        return self.created_list