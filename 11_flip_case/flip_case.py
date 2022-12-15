def flip_case(phrase, to_swap):
    """
    Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """

    # Just practicing list comprehension
    new_case_chars = [char.swapcase() if char.lower() == to_swap.lower()
                                      else char for char in phrase]

    return "".join(new_case_chars)
