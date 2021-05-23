def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """

    counter = 0

    for paren in parens:
        if paren == "(":
            counter += 1
        elif paren == ")":
            counter -= 1

        if counter < 0:
            # Counter cannot go negative per final test condition ")()("
            return False

    return counter == 0
