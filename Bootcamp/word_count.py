def words(string_input):
    if type(string_input) is not str:
        raise TypeError('Input should be a string')
    elif not string_input or string_input == ' ':
        return False
    else:
        word_list = string_input.split()
        count_dict = {}
        for word in word_list:
            if word in count_dict:
                continue
            else:
                count_dict[word] = word_list.count(word)
        return count_dict