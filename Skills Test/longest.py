def longest(string):
    word_list = string.split()
    word_len = 0
    longest = ""
    for w in word_list:
        this_word_len = len(w)
        if this_word_len > word_len:
            longest = w
            word_len += this_word_len
    return (longest)
