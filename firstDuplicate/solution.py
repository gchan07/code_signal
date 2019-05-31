def firstDuplicate(a):
    first_dict = {}
    for entry in a:
        if entry in first_dict:
            return entry
        first_dict[entry] = 1
    return -1
    