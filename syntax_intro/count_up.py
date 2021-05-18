def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

    should print:

        5\n
        6\n
        7\n
    """

    for num in range(start, stop + 1):
        print(num)


count_up(5, 7)        
