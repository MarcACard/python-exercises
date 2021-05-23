def counter(itr):
    count = {}

    for item in itr:
        count[item] = count.get(item, 0) + 1

    return count


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """

    num1_count = counter(str(num1))
    num2_count = counter(str(num2))

    return num1_count == num2_count
