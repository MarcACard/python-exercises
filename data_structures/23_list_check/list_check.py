def list_check(lst):
    """Are all items in lst a list?

    >>> list_check([[1], [2, 3]])
    True

    >>> list_check([[1], "nope"])
    False
    """

    return len([item for item in lst if isinstance(item, list)]) == len(lst)
