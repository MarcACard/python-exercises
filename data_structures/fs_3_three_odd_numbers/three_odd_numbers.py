def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers([5, 2, 1])
    False

    >>> three_odd_numbers([1, 2, 3, 3, 2])
    False
    """
    for start_index in range(len(nums) - 3):
        if sum(nums[start_index : start_index + 3]) % 2 != 0:
            return True

    return False
