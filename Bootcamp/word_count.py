def words(string_input):
    if type(string_input) is not str:
        raise TypeError('Input should be a string')
    elif not string_input or string_input == ' ':
        return False
    else:
        word_list = string_input.split()
        count_dict = {}
        for word in word_list:
            if word.isdigit():
                word = int(word)
            if word in count_dict.keys():
                count_dict[word] += 1
            else:
                count_dict[word] = 1
        return count_dict