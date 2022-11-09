
def linear_search(lst, element):
    for i, item in enumerate(lst):
        if item == element:
            return i

    return -1
