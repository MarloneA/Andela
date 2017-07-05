def find_max_min(list_of_input):
    if isinstance(list_of_input, list):
        if len(list_of_input) > 0:
            sorted_list_of_inputs = sorted(list_of_input)
            return [sorted_list_of_inputs[0], sorted_list_of_inputs[-1]]
        else:
            return False
    else:
        return False