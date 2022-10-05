
def binary_search(lst, item):
    """
    Функция возвощает индекс элемента item в списке lst
    или -1 если элемент не найден.
    """
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = first + (last - first) // 2

        if lst[mid] == item:
            return mid

        if lst[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return -1
