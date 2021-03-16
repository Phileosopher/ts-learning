def combinator(*args):
    combo = args[0]
    for val in args[1:]:
        combo = combo + val
    return combo