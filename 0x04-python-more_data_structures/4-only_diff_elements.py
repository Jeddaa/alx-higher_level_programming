def only_diff_elements(set_1, set_2):
    new = []
    if set_1 is not None and set_2 is not None:
        return set_1 ^ set_2
