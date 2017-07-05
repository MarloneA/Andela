def find_max_min(list_of_input):
    if isinstance(list_of_input, list):
        if len(list_of_input) > 0:
            list_of_input.sort()
            min_max_list = [list_of_input[0], list_of_input[-1]]
            if list_of_input[0] == list_of_input[-1]:
                return [len(list_of_input)]
            else:
                return min_max_list
        else:
            return False
    else:
        return False