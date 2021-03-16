def flatten(seq, list = None):
    """flatten(seq, list = None) -> list
 
    Return a flat version of the iterator `seq` appended to `list`
    """
    if list == None:
        list = []
    try:                          # Can `seq` be iterated over?
        for item in seq:          # If so then iterate over `seq`
            flatten(item, list)      # and make the same check on each item.
    except TypeError:             # If seq isn't iterable
        list.append(seq)             # append it to the new list.
    return list

