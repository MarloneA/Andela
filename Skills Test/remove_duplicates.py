def remove_duplicates(string):
    new_string = ""
    duplicates = 0
    for c in string:
        if c in new_string:
            duplicates += 1
        else:
            new_string += c
    return (''.join(sorted(new_string)), duplicates)
