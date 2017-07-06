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

class BinarySearch(List): # searches to FIND A NUMBER WE WANT from the created or returned list using binary search
    def __init__(self, a, b):
        List.__init__(self, a, b)
    
    def search(self, value_to_find):
        self.count = 1 # incremented at each iteration
        self.list_to_search = self.create_list() # returned list. method inherited from List class
        """ Binary Search ALgorithm to find Index of Value """
        # keep in mind the list is sorted by default
        first_number = 0 # these are indicies
        last_number = len(self.list_to_search) - 1

        while first_number <= last_number:
            middle_number = (first_number + last_number) // 2 # find the middle item (dynamic. keeps on changing)
            if self.list_to_search[middle_number] == value_to_find:
                break # value found
            else:
                if value_to_find < self.list_to_search[middle_number]:
                    last_number = middle_number - 1
                else:
                    first_number = middle_number + 1
                self.count += 1 # increment count. more work to be done

        return {'work_done': self.count}