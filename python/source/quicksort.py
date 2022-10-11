

def quicksort(lst):
    if len(lst) < 2:
        return lst

    elem = lst[0]
    left = []
    right = []
    for n in lst[1:]:
        if n <= elem:
            left.append(n)
        else:
            right.append(n)
    return quicksort(left) + [elem] + quicksort(right)



