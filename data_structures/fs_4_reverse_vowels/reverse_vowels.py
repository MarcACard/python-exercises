def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    >>> reverse_vowels("aeiou")
    'uoiea'

    >>> reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """

    vowels = "aeiou"
    split_string = list(s)
    # Separate iterators to start from each end.
    start_i = 0
    end_i = len(s) - 1

    while start_i < end_i:
        if split_string[start_i].lower() not in vowels:
            start_i += 1
        elif split_string[end_i].lower() not in vowels:
            end_i -= 1
        else:
            split_string[start_i], split_string[end_i] = (
                split_string[end_i],
                split_string[start_i],
            )
            start_i += 1
            end_i -= 1

    return "".join(split_string)
