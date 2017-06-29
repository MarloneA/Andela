def is_isogram(w):
    if type(w) is not str:
        raise TypeError("Argument should be a string")
    elif not w or w == " ":
        return (w, False)
    else:
        for c in w:
            if w.count(c) > 1:
                return (w, False)
        return (w, True)
